---
title: Chrome Quantum-resistant Root Program - CQRP Root Store
---

# CQRP Root Store

Below is the list of **MTC CA Cosigners** and **Mirror Cosigners** included in the Chrome Quantum-resistant Root Store.

Data is fetched from [`https://www.gstatic.com/mtcs/cosigners/v1/cosigners.json`](https://www.gstatic.com/mtcs/cosigners/v1/cosigners.json). Keys can be fetched from [`https://www.gstatic.com/mtcs/cosigners/v1/cosigners.pem`](https://www.gstatic.com/mtcs/cosigners/v1/cosigners.pem). The fields are described in [`https://www.gstatic.com/mtcs/cosigners/v1/cosigners_schema.json`](https://www.gstatic.com/mtcs/cosigners/v1/cosigners_schema.json).

The **Monitoring Prefix** (`base_url` in `cosigners.json`) is a URL prefix. Append the path of the resource you want:

- **MTC CA Cosigners:** `<monitoring prefix>/<log number>/checkpoint` and `<monitoring prefix>/<log number>/landmarks`, as defined by [mtc-tlog](https://c2sp.org/mtc-tlog). A CA keeps a numbered series of issuance logs, starting at 1, and moves to the next **log number** when it replaces a log. **Min Log Number** is the lowest log number Chrome accepts for that CA, and the **checkpoint** link in each row points at that log.
- **Mirror Cosigners:** `<monitoring prefix>/<hex SHA-256 of the log origin>/checkpoint`, as defined by [tlog-mirror](https://c2sp.org/tlog-mirror), where the log origin is `oid/1.3.6.1.4.1.<CA's Base ID>.0.<log number>`. A mirror only serves the logs it mirrors. The **Submission Prefix** (`submission_prefix`) is the separate prefix used to submit entries to the mirror.

The **Base ID** (`base_id`) identifies a cosigner: its signature on a checkpoint is labelled `oid/1.3.6.1.4.1.<Base ID>`.

<style>
/* Cosigner tables. These rules only apply to this page; the shared table styles are in crp.css. */
#cosigners-content table { width: 100%; min-width: 800px; }
#cosigners-content th { min-width: 0; padding: 2px 8px; }
#cosigners-content td { padding: 8px; vertical-align: top; white-space: nowrap; }
/* Only the prefix column wraps, and only where wrappableUrl() allows. */
#cosigners-content td.prefix { white-space: normal; }
#cosigners-content .prefix-pair { display: grid; grid-template-columns: max-content auto; gap: 2px 8px; }
#cosigners-content .table-scroll { overflow-x: auto; }

/* Wide windows: let the tables use the space to the right of the 800px text
   column. 1140px is where that space starts; 340px keeps clear of the
   navigation on the left and the scrollbar on the right. */
@media (min-width: 1140px) {
  #cosigners-content { width: max-content; min-width: 100%; max-width: calc(100vw - 340px); }
}

/* Narrower windows: a table that does not fit scrolls sideways on its own
   instead of making the whole page wider than the window. */
@media (max-width: 1139px) {
  #cosigners-content .table-scroll { contain: inline-size; }
}
</style>

<div id="loading-spinner" style="padding: 1.5em; font-weight: bold; color: #57606a; background: #f6f8fa; border-radius: 6px; margin: 1em 0;">
  ⏳ Loading cosigners data...
</div>

<div id="cosigners-content" style="display: none;">
  <p style="background: #e8f0fe; color: #1a73e8; padding: 0.75em 1em; border-radius: 6px; font-weight: 500;">
    <strong>Store Version:</strong> <span id="store-version">-</span> &nbsp;|&nbsp; 
    <strong>Last Updated:</strong> <span id="store-timestamp">-</span>
  </p>

  <h3>MTC CA Cosigners (Issuers)</h3>
  <div class="table-scroll">
  <table>
    <thead>
      <tr>
        <th>Name / Operator</th>
        <th>Monitoring Prefix</th>
        <th>Min Log Number</th>
        <th>Base ID</th>
        <th>Max Lifetime</th>
        <th>Key SHA-256</th>
      </tr>
    </thead>
    <tbody id="issuers-body"></tbody>
  </table>
  </div>

  <h3>Mirror Cosigners</h3>
  <div class="table-scroll">
  <table>
    <thead>
      <tr>
        <th>Name / Operator</th>
        <th>Monitoring / Submission Prefix</th>
        <th>Base ID</th>
        <th>State</th>
        <th>Key SHA-256</th>
      </tr>
    </thead>
    <tbody id="mirrors-body"></tbody>
  </table>
  </div>
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

// USABLE is green. Every other state uses the colors of the TEST badge.
function getStateBadge(state) {
  const colors = state === "USABLE"
    ? "background: #dafbe1; color: #1a7f37;"
    : "background: #fff8c5; color: #9a6700;";
  return `<span style="${colors} padding: 2px 6px; border-radius: 4px; font-weight: bold; font-size: 11px;">${state}</span>`;
}

function formatTimestamp(ts) {
  if (!ts) return "N/A";
  const d = new Date(ts);
  return d.toISOString().replace("T", " ").substring(0, 19) + " UTC";
}

// Returns url as HTML that can wrap after "://", before a "." in the host and
// before a "/" in the path, but nowhere else. <wbr> adds no characters when
// the URL is copied.
function wrappableUrl(url) {
  const pathStart = url.indexOf("/", url.indexOf("://") + 3);
  const host = pathStart < 0 ? url : url.slice(0, pathStart);
  const path = pathStart < 0 ? "" : url.slice(pathStart);
  return host.replace("://", "://<wbr>").replace(/\./g, "<wbr>.") +
    path.replace(/\/(?=.)/g, "<wbr>/");
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
        // base_url is a prefix, not a page. Link to the checkpoint of the
        // minimum log instead: <base_url>/<min_log_number>/checkpoint.
        const minLog = item.min_log_number;
        const prefix = (item.base_url || "").replace(/\/+$/, "");
        const checkpointLink = minLog
          ? `<br><a href="${prefix}/${minLog}/checkpoint" target="_blank" rel="noopener">checkpoint</a>`
          : "";
        const tr = document.createElement("tr");
        tr.innerHTML = `
          <td>${realmBadge} <strong>${item.friendly_name || ""}</strong><br>${opName}</td>
          <td class="prefix"><code>${wrappableUrl(item.base_url || "")}</code></td>
          <td>${minLog || "N/A"}${checkpointLink}</td>
          <td><code>${item.base_id || ""}</code></td>
          <td>${lifetime}</td>
          <td><code title="${item.key_sha256}">${(item.key_sha256 || "").substring(0, 12)}...</code></td>
        `;
        issuersBody.appendChild(tr);
      });
    } else {
      issuersBody.innerHTML = '<tr><td colspan="6">No issuer cosigners currently listed.</td></tr>';
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
          <td>${realmBadge} <strong>${item.friendly_name || ""}</strong><br>${opName}</td>
          <td class="prefix">
            <div class="prefix-pair">
              <span>Monitoring</span><code>${wrappableUrl(item.base_url || "")}</code>
              <span>Submission</span><code>${item.submission_prefix ? wrappableUrl(item.submission_prefix) : "N/A"}</code>
            </div>
          </td>
          <td><code>${item.base_id || ""}</code></td>
          <td>${getStateBadge(state)}</td>
          <td><code title="${item.key_sha256}">${(item.key_sha256 || "").substring(0, 12)}...</code></td>
        `;
        mirrorsBody.appendChild(tr);
      });
    } else {
      mirrorsBody.innerHTML = '<tr><td colspan="5">No mirror cosigners currently listed.</td></tr>';
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
