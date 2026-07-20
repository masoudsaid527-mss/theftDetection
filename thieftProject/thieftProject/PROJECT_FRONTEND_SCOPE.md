# Project Development Scope (Frontend Only)

The current development phase of the Nationwide Software-Based Theft Reporting and Tracking System (NSTRTS) focuses only on the frontend implementation of the system.

This means the system is currently designed to demonstrate the user interface (UI), page navigation, user interactions, and system workflow without a connected backend server or database.

The frontend is developed using:

- **HTML** for creating the structure of web pages.
- **CSS** for designing the user interface and improving the visual appearance.
- **JavaScript** for adding interactivity, validation, and frontend functionality.

## Frontend Features Implemented

1. **User Interface Design**

   The system provides complete interfaces for different users:

   - Citizen interface
   - Police officer interface
   - Administrator interface
   - Policy maker interface

   Each user role has its own dashboard and pages based on its responsibilities.

2. **Registration Interface**

   The registration page allows users to create accounts by providing:

   - Full name
   - Email address
   - Phone number
   - National ID
   - Password
   - User role

   The frontend validates user inputs and prepares the data structure for future backend integration.

3. **Login Interface**

   The login page provides:

   - Email input
   - Password input
   - Role selection

   The frontend login system demonstrates role-based navigation:

   - Citizen → Citizen Dashboard
   - Police → Police Dashboard
   - Admin → Admin Dashboard
   - Policy Maker → Policy Maker Dashboard

   **Note:** The current login system is only a frontend simulation. It does not verify users from a real database.

4. **Dashboard Interfaces**

   Different dashboards have been designed for each user category.

   **Citizen Dashboard**

   Allows citizens to:

   - View their reports
   - Submit theft reports
   - Track case progress
   - Manage profile information

   **Police Dashboard**

   Allows police officers to:

   - View reported cases
   - Review theft information
   - Update investigation status
   - Manage case progress

   **Admin Dashboard**

   Allows administrators to:

   - View users
   - Monitor reports
   - Access system statistics

   **Policy Maker Dashboard**

   Provides crime analytics:

   - View crime trends
   - Analyze theft patterns
   - Access statistical reports

