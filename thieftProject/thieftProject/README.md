# NSTRTS (Nationwide Software-Based Theft Reporting and Tracking System) — Frontend

## Overview
**NSTRTS** is a web platform that enables citizens, police officers, administrators, and policy makers to report theft incidents and track case progress.

This repository currently contains **frontend-only** implementation (no connected backend/database). The UI demonstrates:
- Page navigation
- Role-based workflows
- Form validation and frontend interactions
- A system workflow suitable for later backend integration

Frontend scope is documented in [`PROJECT_FRONTEND_SCOPE.md`](./PROJECT_FRONTEND_SCOPE.md).

## Tech Stack
- **HTML**: page structure
- **CSS**: styling (`assets/css/`)
- **JavaScript**: interactivity and simulations (`assets/js/`)

## Project Structure (Main Pages)
- Landing / marketing:
  - `index.html`
- Authentication (UI simulation):
  - `login.html`
  - `register.html`
- Citizen:
  - `citizen/dashboard.html`
  - `citizen/report-theft.html`
  - `citizen/report-details.html`
  - `citizen/my-reports.html`
  - `citizen/profile.html`
- Police:
  - `police/dashboard.html`
  - `police/all-reports.html`
  - `police/report-details.html`
  - `police/update-status.html`
  - `police/profile.html`
- Administrator:
  - `admin/dashboard.html`
  - `admin/users.html`
  - `admin/reports.html`
  - `admin/statistics.html`
  - `admin/profile.html`
- Policy maker:
  - `policymaker/dashboard.html`
  - `policymaker/analytics.html`
  - `policymaker/reports.html`
  - `policymaker/statistics.html`

### Shared UI Components
- `components/` contains reusable UI fragments (e.g., navbar/sidebar/footer).

## Frontend Behavior (What’s Implemented)
- **Responsive navigation**: mobile menu toggle (shared script).
- **FAQ accordion** on the landing page.
- **Contact form simulation**: shows a success message and resets the form.
- **Role-based UI**: login/register provide frontend navigation paths by role.

(See `assets/js/app.js` and other scripts under `assets/js/`.)

## How to Run
### Option A: Open directly (quickest)
1. Open `index.html` in a browser.
2. Navigate to pages from the UI.

### Option B: Serve with a local static server (recommended)
Because the project uses relative asset paths, you can also run it with any simple static server (e.g., VSCode Live Server, or `python -m http.server`).

## Assets
- Images: `assets/images/`
- Stylesheets: `assets/css/`
- Scripts: `assets/js/`

## Notes / Limitations
- There is **no backend** in this repository.
- Login/register flows are **simulated** for UI demonstration and role navigation.

## Next Steps (Backend Integration)
After implementing a backend, typical next steps would include:
- Real authentication + session handling (by role)
- Persisting theft reports and evidence metadata
- Police/admin workflow endpoints (status updates, review)
- Policy maker analytics backed by stored data

(Use `PROJECT_FRONTEND_SCOPE.md` as the starting point for planned features.)

# thieft-reprot-and-tracking-system
