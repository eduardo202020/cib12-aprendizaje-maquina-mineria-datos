const startButton = document.getElementById("startButton");
const stats = document.getElementById("stats");
const currentEvent = document.getElementById("currentEvent");
const brokerPanel = document.getElementById("brokerPanel");
const processorPanel = document.getElementById("processorPanel");
const sinkPanel = document.getElementById("sinkPanel");
const brokerTable = document.getElementById("brokerTable");
const decisionTable = document.getElementById("decisionTable");

async function fetchState() {
  const response = await fetch("/api/state");
  return response.json();
}

async function startSimulation() {
  startButton.disabled = true;
  await fetch("/api/start", { method: "POST" });
}

function renderStats(state) {
  const items = [
    ["Estado", state.status],
    ["Producidos", state.produced_count],
    ["En cola", state.queue_depth],
    ["Procesados", state.processed_count],
    ["Aprobadas", state.summary.aprobadas],
    ["Bloqueadas", state.summary.bloqueadas],
    ["Watermark", state.watermark ? state.watermark.slice(11, 19) : "--:--:--"],
  ];

  stats.innerHTML = items.map(([label, value]) => `
    <div class="stat">
      <div class="stat-label">${label}</div>
      <div class="stat-value">${value}</div>
    </div>
  `).join("");
}

function renderCurrentEvent(event) {
  if (!event) {
    currentEvent.innerHTML = `<p class="muted">Aun no hay evento en curso.</p>`;
    return;
  }

  currentEvent.innerHTML = `
    <div class="kv">
      <strong>event_id</strong><span>${event.event_id}</span>
      <strong>card_id</strong><span>${event.card_id}</span>
      <strong>monto</strong><span>${event.amount}</span>
      <strong>pais</strong><span>${event.country}</span>
      <strong>event_time</strong><span>${event.event_time.slice(11, 19)}</span>
      <strong>arrival_time</strong><span>${event.arrival_time.slice(11, 19)}</span>
    </div>
  `;
}

function renderBroker(state) {
  brokerPanel.innerHTML = `
    <div class="kv">
      <strong>cola actual</strong><span>${state.queue_depth} evento(s)</span>
      <strong>producidos</strong><span>${state.produced_count}</span>
      <strong>ultimo estado</strong><span>${state.status}</span>
    </div>
  `;

  brokerTable.innerHTML = `
    <table>
      <thead>
        <tr>
          <th>event_id</th>
          <th>tarjeta</th>
          <th>monto</th>
          <th>event_time</th>
          <th>arrival</th>
        </tr>
      </thead>
      <tbody>
        ${state.recent_broker.map(item => `
          <tr>
            <td>${item.event_id}</td>
            <td>${item.card_id}</td>
            <td>${item.amount}</td>
            <td>${item.event_time}</td>
            <td>${item.arrival_time}</td>
          </tr>
        `).join("")}
      </tbody>
    </table>
  `;
}

function renderProcessor(state) {
  processorPanel.innerHTML = `
    <div class="kv">
      <strong>watermark</strong><span>${state.watermark ? state.watermark.slice(11, 19) : "--:--:--"}</span>
      <strong>revisadas</strong><span>${state.summary.revisadas}</span>
      <strong>tardias</strong><span>${state.summary.tardios}</span>
      <strong>duplicados</strong><span>${state.summary.duplicados}</span>
    </div>
  `;
}

function renderSink(state) {
  const last = state.recent_decisions[0];
  if (!last) {
    sinkPanel.innerHTML = `<p class="muted">Aun no hay decisiones emitidas.</p>`;
    decisionTable.innerHTML = "";
    return;
  }

  sinkPanel.innerHTML = `
    <div class="kv">
      <strong>ultima decision</strong><span><span class="badge ${last.decision}">${last.decision}</span></span>
      <strong>tarjeta</strong><span>${last.card_id}</span>
      <strong>motivo</strong><span>${last.reasons.join(", ")}</span>
    </div>
  `;

  decisionTable.innerHTML = `
    <table>
      <thead>
        <tr>
          <th>decision</th>
          <th>event_id</th>
          <th>tarjeta</th>
          <th>monto</th>
          <th>detalle</th>
        </tr>
      </thead>
      <tbody>
        ${state.recent_decisions.map(item => `
          <tr>
            <td><span class="badge ${item.decision}">${item.decision}</span></td>
            <td>${item.event_id}</td>
            <td>${item.card_id}</td>
            <td>${item.amount}</td>
            <td>${item.reasons.join(", ")}</td>
          </tr>
        `).join("")}
      </tbody>
    </table>
  `;
}

function update(state) {
  renderStats(state);
  renderCurrentEvent(state.current_event);
  renderBroker(state);
  renderProcessor(state);
  renderSink(state);
  startButton.disabled = state.running;
}

startButton.addEventListener("click", startSimulation);

setInterval(async () => {
  const state = await fetchState();
  update(state);
}, 500);

fetchState().then(update);
