/* Shared report store used by citizen, police, admin and policy-maker pages. */
const REPORTS_KEY = "nstrtsReports";
const LEGACY_REPORTS_PREFIX = "nstrtsReports:";

function currentUser() {
    try { return JSON.parse(localStorage.getItem("loggedInUser")) || {}; }
    catch (_) { return {}; }
}

function normaliseStatus(status) {
    const value = String(status || "").toLowerCase();
    if (value.includes("resolv") || value.includes("complet")) return "Resolved";
    if (value.includes("investig") || value.includes("review")) return "Investigation";
    return "Pending";
}

function migrateLegacyReports() {
    let reports;
    try { reports = JSON.parse(localStorage.getItem(REPORTS_KEY)) || []; } catch (_) { reports = []; }
    if (!Array.isArray(reports)) reports = [];
    for (let i = 0; i < localStorage.length; i += 1) {
        const key = localStorage.key(i);
        if (!key || !key.startsWith(LEGACY_REPORTS_PREFIX)) continue;
        try {
            const email = key.slice(LEGACY_REPORTS_PREFIX.length);
            const legacy = JSON.parse(localStorage.getItem(key)) || [];
            legacy.forEach((report) => {
                if (!reports.some((item) => item.id === report.id)) {
                    reports.push({ ...report, reporterEmail: report.reporterEmail || email, status: normaliseStatus(report.status) });
                }
            });
        } catch (_) { /* Ignore malformed browser data. */ }
    }
    localStorage.setItem(REPORTS_KEY, JSON.stringify(reports));
    return reports;
}

function getReports() { return migrateLegacyReports().map((report) => ({ ...report, status: normaliseStatus(report.status) })); }
function saveReports(reports) { localStorage.setItem(REPORTS_KEY, JSON.stringify(reports)); }
function isCitizenPage() { return window.location.pathname.includes("/citizen/"); }
function visibleReports() {
    const reports = getReports();
    const email = String(currentUser().email || "").toLowerCase();
    return isCitizenPage() && email ? reports.filter((report) => String(report.reporterEmail || "").toLowerCase() === email) : reports;
}
function formatDate(value) {
    if (!value) return "—";
    const date = new Date(`${value}T00:00:00`);
    return Number.isNaN(date.getTime()) ? value : date.toLocaleDateString(undefined, { day: "2-digit", month: "long", year: "numeric" });
}
function statusClass(status) { return normaliseStatus(status) === "Resolved" ? "completed" : normaliseStatus(status) === "Investigation" ? "investigation" : "pending"; }
function statusNode(status) { const node = document.createElement("span"); node.className = statusClass(status); node.textContent = normaliseStatus(status); return node; }
function cell(value) { const node = document.createElement("td"); node.textContent = value || "—"; return node; }
function updateCards(reports) {
    document.querySelectorAll(".card").forEach((card) => {
        const label = card.querySelector("p")?.textContent.toLowerCase() || "";
        const value = card.querySelector("h3");
        if (!value) return;
        if ((label.includes("total") && (label.includes("report") || label.includes("case"))) || label.includes("all theft")) value.textContent = reports.length;
        else if (label.includes("pending")) value.textContent = reports.filter((r) => r.status === "Pending").length;
        else if (label.includes("investigation")) value.textContent = reports.filter((r) => r.status === "Investigation").length;
        else if (label.includes("resolved") || label.includes("completed")) value.textContent = reports.filter((r) => r.status === "Resolved").length;
        else if (label.includes("resolution rate")) value.textContent = reports.length ? `${Math.round(reports.filter((r) => r.status === "Resolved").length / reports.length * 100)}%` : "0%";
        else if (label.includes("mobile")) value.textContent = reports.filter((r) => r.category.toLowerCase().includes("mobile") || r.item.toLowerCase().includes("phone")).length;
        else if (label.includes("vehicle")) value.textContent = reports.filter((r) => r.category.toLowerCase().includes("vehicle") || r.item.toLowerCase().includes("car") || r.item.toLowerCase().includes("motor")).length;
    });
    document.querySelectorAll("[data-report-count]").forEach((element) => {
        const status = element.dataset.reportCount;
        element.textContent = status === "total" ? reports.length : reports.filter((r) => r.status === normaliseStatus(status)).length;
    });
}
function renderListTable(reports) {
    const table = document.querySelector("table:not(.details-table)");
    const body = document.getElementById("reportsTableBody") || table?.querySelector("tbody");
    if (!body) return;
    const headers = [...table.querySelectorAll("thead th")].map((header) => header.textContent.trim().toLowerCase());
    if (!headers.length || !headers.some((header) => header.includes("report id"))) return;
    body.replaceChildren();
    if (!reports.length) {
        const row = document.createElement("tr"), empty = document.createElement("td");
        empty.colSpan = headers.length; empty.textContent = "No theft reports available yet."; row.appendChild(empty); body.appendChild(row); return;
    }
    reports.slice(0, window.location.pathname.includes("dashboard") ? 5 : reports.length).forEach((report) => {
        const row = document.createElement("tr");
        headers.forEach((header) => {
            if (header.includes("report id")) row.appendChild(cell(report.id));
            else if (header.includes("citizen")) row.appendChild(cell(report.reporterName || report.reporterEmail || "Citizen"));
            else if (header.includes("region") || header.includes("location")) row.appendChild(cell(report.location));
            else if (header.includes("theft type") || header.includes("category")) row.appendChild(cell(report.category));
            else if (header.includes("item")) row.appendChild(cell(report.item));
            else if (header.includes("date")) row.appendChild(cell(formatDate(report.date)));
            else if (header.includes("officer")) row.appendChild(cell(report.assignedOfficer || "Unassigned"));
            else if (header.includes("status")) { const td = document.createElement("td"); td.appendChild(statusNode(report.status)); row.appendChild(td); }
            else if (header.includes("action")) { const td = document.createElement("td"), link = document.createElement("a"); const police = window.location.pathname.includes("/police/"); link.href = `${police ? "report-details.html" : "report-details.html"}?id=${encodeURIComponent(report.id)}`; link.textContent = "View"; td.appendChild(link); row.appendChild(td); }
            else row.appendChild(cell("—"));
        });
        body.appendChild(row);
    });
}
function reportFromUrl(reports) { return reports.find((report) => report.id === new URLSearchParams(location.search).get("id")) || reports[0]; }
function renderDetails(reports) {
    const report = reportFromUrl(reports); if (!report) return;
    const fields = { reportId: report.id, reportStatus: report.status, reportCategory: report.category, reportItem: report.item, reportDate: formatDate(report.date), reportLocation: report.location, reportDescription: report.description };
    Object.entries(fields).forEach(([id, value]) => { const element = document.getElementById(id); if (element) { element.textContent = value || "—"; if (id === "reportStatus") element.className = statusClass(value); } });
    document.querySelectorAll(".details-table tr").forEach((row) => {
        const label = row.querySelector("th")?.textContent.trim().toLowerCase(); const value = row.querySelector("td"); if (!label || !value) return;
        if (label.includes("report id")) value.textContent = report.id;
        else if (label.includes("citizen name")) value.textContent = report.reporterName || "Citizen";
        else if (label === "email") value.textContent = report.reporterEmail || "—";
        else if (label.includes("theft type")) value.textContent = report.category;
        else if (label.includes("incident date")) value.textContent = formatDate(report.date);
        else if (label.includes("location")) value.textContent = report.location;
        else if (label.includes("current status")) { value.replaceChildren(statusNode(report.status)); }
    });
    const descriptionHeading = [...document.querySelectorAll(".section h2")].find((h) => h.textContent.toLowerCase().includes("incident description"));
    const description = descriptionHeading?.parentElement.querySelector("p"); if (description) description.textContent = report.description || "—";
    document.querySelectorAll('a[href="update-status.html"]').forEach((link) => { link.href = `update-status.html?id=${encodeURIComponent(report.id)}`; });
}
function setupStatusForm(reports) {
    const form = document.getElementById("statusForm"); if (!form) return;
    const report = reportFromUrl(reports); if (!report) return;
    renderDetails([report]);
    const select = form.querySelector("select");
    if (select) select.value = report.status === "Investigation" ? "Under Investigation" : report.status;
    form.addEventListener("submit", (event) => {
        event.preventDefault(); if (!select?.value) return alert("Select a new status.");
        const all = getReports(), index = all.findIndex((item) => item.id === report.id);
        if (index < 0) return;
        all[index] = { ...all[index], status: normaliseStatus(select.value), assignedOfficer: form.querySelector('input[type="text"]')?.value.trim() || "Unassigned", policeNotes: form.querySelector("textarea")?.value.trim() || "" };
        saveReports(all); window.location.href = `report-details.html?id=${encodeURIComponent(report.id)}`;
    });
}

const reportForm = document.getElementById("reportForm");
if (reportForm) reportForm.addEventListener("submit", (event) => {
    event.preventDefault();
    const field = (id) => document.getElementById(id);
    const required = ["category", "itemName", "date", "time", "location", "description"];
    if (required.some((id) => !field(id)?.value.trim())) return alert("Please complete all required report fields.");
    const user = currentUser();
    const report = { id: `NST${Date.now()}`, category: field("category").value.trim(), item: field("itemName").value.trim(), serial: field("serial")?.value.trim() || "", date: field("date").value, time: field("time").value, location: field("location").value.trim(), description: field("description").value.trim(), witness: field("witness")?.value.trim() || "", evidenceName: field("evidence")?.files[0]?.name || "", reporterEmail: user.email || "guest", reporterName: user.username || user.email || "Citizen", status: "Pending" };
    const reports = getReports(); reports.unshift(report); saveReports(reports); location.href = "my-reports.html";
});

document.addEventListener("DOMContentLoaded", () => { const reports = visibleReports(); updateCards(reports); renderListTable(reports); renderDetails(reports); setupStatusForm(reports); });
