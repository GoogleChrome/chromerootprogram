---
title: Chrome Quantum-resistant Root Program - CQRP Root Store
---

# CQRP Root Store

Below is the list of **MTC CA Cosigners** and **Mirror Cosigners** included in the Chrome Quantum-resistant Root Store.

Data is fetched directly from [`https://www.gstatic.com/mtcs/cosigners/v1/cosigners.json`](https://www.gstatic.com/mtcs/cosigners/v1/cosigners.json).

<div id="loading-spinner" style="padding: 1.5em; font-weight: bold; color: #57606a; background: #f6f8fa; border-radius: 6px; margin: 1em 0;">
  ⏳ Loading cosigners data...
</div>

<div id="cosigners-content" style="display: none;">
  <p style="background: #e8f0fe; color: #1a73e8; padding: 0.75em 1em; border-radius: 6px; font-weight: 500;">
    <strong>Store Version:</strong> <span id="store-version">-</span> &nbsp;|&nbsp; 
    <strong>Last Updated:</strong> <span id="store-timestamp">-</span>
  </p>

  <h3>MTC CA Cosigners (Issuers)</h3>
  <table>
    <thead>
      <tr>
        <th>Environment</th>
        <th>Friendly Name</th>
        <th>Operator</th>
        <th>Base URL</th>
        <th>Base ID</th>
        <th>Max Lifetime</th>
        <th>Key SHA-256</th>
      </tr>
    </thead>
    <tbody id="issuers-body"></tbody>
  </table>

  <h3>Mirror Cosigners</h3>
  <table>
    <thead>
      <tr>
        <th>Environment</th>
        <th>Friendly Name</th>
        <th>Operator</th>
        <th>Base URL</th>
        <th>State</th>
        <th>Key SHA-256</th>
      </tr>
    </thead>
    <tbody id="mirrors-body"></tbody>
  </table>
</div>

<div id="error-message" style="display: none; color: #cf222e; padding: 1em; background: #ffebe9; border-radius: 6px; margin: 1em 0;">
  <strong>Failed to load data.</strong> You can view the raw JSON directly at <a href="https://www.gstatic.com/mtcs/cosigners/v1/cosigners.json" target="_blank">cosigners.json</a>.
</div>

<script>
function getRealmBadge(realm) {
  if (realm === "PUBLICLY_TRUSTED") {
    return `<span style="background: #dafbe1; color: #1a7f37; border: 1px solid #4ac26b; padding: 2px 8px; border-radius: 4px; font-weight: bold; font-size: 11px;" title="PUBLICLY_TRUSTED (Production)">PROD</span>`;
  } else if (realm === "UNTRUSTED_VALIDATION_ONLY") {
    return `<span style="background: #fff8c5; color: #9a6700; border: 1px solid #d4a72c; padding: 2px 8px; border-radius: 4px; font-weight: bold; font-size: 11px;" title="UNTRUSTED_VALIDATION_ONLY (Testing)">TEST</span>`;
  } else {
    return `<span style="background: #f6f8fa; color: #57606a; border: 1px solid #d0d7de; padding: 2px 8px; border-radius: 4px; font-weight: bold; font-size: 11px;">${realm || "UNSET"}</span>`;
  }
}

function formatTimestamp(ts) {
  if (!ts) return "N/A";
  const d = new Date(ts);
  return d.toISOString().replace("T", " ").substring(0, 19) + " UTC";
}

async function loadCosigners() {
  const loading = document.getElementById("loading-spinner");
  const content = document.getElementById("cosigners-content");
  const errorMsg = document.getElementById("error-message");

  let data;
  try {
    const response = await fetch("https://www.gstatic.com/mtcs/cosigners/v1/cosigners.json");
    if (!response.ok) throw new Error("HTTP " + response.status);
    data = await response.json();
  } catch (err) {
    console.warn("Direct fetch from gstatic failed (CORS). Falling back to relative static snapshot:", err);
    try {
      const fallbackUrl = new URL("../../static/cosigners_fallback.json", window.location.href).href;
      const fallbackResp = await fetch(fallbackUrl);
      if (!fallbackResp.ok) throw new Error("Fallback HTTP " + fallbackResp.status);
      data = await fallbackResp.json();
    } catch (fallbackErr) {
      console.error("Fallback fetch failed:", fallbackErr);
      loading.style.display = "none";
      errorMsg.style.display = "block";
      return;
    }
  }

  try {
    document.getElementById("store-version").textContent = data.version || "N/A";
    document.getElementById("store-timestamp").textContent = formatTimestamp(data.timestamp);
    
    // Build Issuers table
    const issuersBody = document.getElementById("issuers-body");
    issuersBody.innerHTML = "";
    if (data.issuers && data.issuers.length > 0) {
      data.issuers.forEach(item => {
        const opName = (item.operator_history && item.operator_history.length > 0) ? item.operator_history[0].name : "Unknown";
        const lifetime = item.max_cert_lifetime_seconds ? (item.max_cert_lifetime_seconds / 86400) + " days" : "N/A";
        const realmBadge = getRealmBadge(item.realm);
        const tr = document.createElement("tr");
        tr.innerHTML = `
          <td>${realmBadge}</td>
          <td><strong>${item.friendly_name || ""}</strong></td>
          <td>${opName}</td>
          <td><a href="${item.base_url}" target="_blank" rel="noopener">${item.base_url}</a></td>
          <td><code>${item.base_id || ""}</code></td>
          <td>${lifetime}</td>
          <td><code title="${item.key_sha256}">${(item.key_sha256 || "").substring(0, 12)}...</code></td>
        `;
        issuersBody.appendChild(tr);
      });
    } else {
      issuersBody.innerHTML = '<tr><td colspan="7">No issuer cosigners currently listed.</td></tr>';
    }

    // Build Mirrors table
    const mirrorsBody = document.getElementById("mirrors-body");
    mirrorsBody.innerHTML = "";
    if (data.mirrors && data.mirrors.length > 0) {
      data.mirrors.forEach(item => {
        const opName = (item.operator_history && item.operator_history.length > 0) ? item.operator_history[0].name : "Unknown";
        const state = (item.state_history && item.state_history.length > 0) ? item.state_history[0].state : "UNKNOWN";
        const realmBadge = getRealmBadge(item.realm);
        const tr = document.createElement("tr");
        tr.innerHTML = `
          <td>${realmBadge}</td>
          <td><strong>${item.friendly_name || ""}</strong></td>
          <td>${opName}</td>
          <td><a href="${item.base_url}" target="_blank" rel="noopener">${item.base_url}</a></td>
          <td><span style="background: #dafbe1; color: #1a7f37; padding: 2px 6px; border-radius: 4px; font-weight: bold; font-size: 11px;">${state}</span></td>
          <td><code title="${item.key_sha256}">${(item.key_sha256 || "").substring(0, 12)}...</code></td>
        `;
        mirrorsBody.appendChild(tr);
      });
    } else {
      mirrorsBody.innerHTML = '<tr><td colspan="6">No mirror cosigners currently listed.</td></tr>';
    }

    loading.style.display = "none";
    content.style.display = "block";
  } catch (renderErr) {
    console.error("Rendering error:", renderErr);
    loading.style.display = "none";
    errorMsg.style.display = "block";
  }
}

if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", loadCosigners);
} else {
  loadCosigners();
}
</script>
