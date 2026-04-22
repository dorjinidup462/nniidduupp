---

# **Software Requirements Specification (SRS)**

## **Office Supply Management System (OSMS)**

---

## **1. Project Overview**

* **Objective**

  * Develop a web-based internal system to manage office supply requests and inventory.
  * Replace manual/email-based request processes with a centralized digital workflow.

* **Key Goals**

  * Improve efficiency in supply request handling.
  * Provide real-time inventory visibility.
  * Ensure transparency between Admin and Staff.
  * Reduce repetitive admin communication tasks.

* **System Type**

  * Single Page Application (SPA)
  * Frontend-only prototype (no backend integration)

---

## **2. Scope of the System**

* **In Scope**

  * User authentication (frontend simulation)
  * Inventory management
  * Request submission and approval workflow
  * Local data persistence using browser storage
  * Responsive UI across devices

* **Out of Scope (Future Enhancements)**

  * Backend database integration
  * Role-based access via API
  * Email/SMS notifications
  * Multi-admin support

---

## **3. User Roles**

* **Admin**

  * Full control over inventory and requests
* **Staff**

  * Submit supply requests and view request status

---

## **4. Authentication & Authorization**

* **Login Credentials (Hardcoded)**

  * Admin Username: `Admin@2026`
  * Staff Username: `Staff@2026`
  * Default Password (both): `abc@123`

* **Authentication Requirements**

  * Login form with:

    * Username field
    * Password field
    * Login button
  * Validate credentials against predefined values
  * Redirect based on role:

    * Admin → Admin Dashboard
    * Staff → Staff Dashboard

* **Password Management**

  * Force password change on first login
  * Password rules:

    * Minimum 6 characters
    * Must include letters and numbers
  * Store updated password in `localStorage`
  * Persist login session using `localStorage` or `sessionStorage`

* **Session Handling**

  * Maintain login state until logout or browser clear
  * Logout button must:

    * Clear session
    * Redirect to login page

---

## **5. Admin Functional Requirements**

### **5.1 Dashboard Overview**

* Display summary cards:

  * Total items in inventory
  * Total requests
  * Pending requests count
  * Low stock items count

---

### **5.2 Inventory Management (CRUD)**

* **Create Item**

  * Fields:

    * Item ID (auto-generated)
    * Item Name (required)
    * Category (dropdown: Stationery, Snacks, Apparel, Others)
    * Quantity (numeric, required)
    * Low Stock Threshold (optional)
  * Validation:

    * No empty fields
    * Quantity ≥ 0

* **Read/View Items**

  * Display inventory in table:

    * Item Name
    * Category
    * Quantity
    * Status (In Stock / Low Stock / Out of Stock)
  * Highlight:

    * Low stock (e.g., yellow)
    * Out of stock (e.g., red)

* **Update Item**

  * Edit:

    * Name
    * Category
    * Quantity
  * Adjust stock manually

* **Delete Item**

  * Confirmation popup before deletion

---

### **5.3 Request Management**

* View all staff requests in table:

  * Request ID
  * Staff Name
  * Item Name
  * Requested Quantity
  * Status (Pending / Approved / Rejected)
  * Timestamp

* **Actions**

  * Approve button
  * Reject button

* **Approval Logic**

  * On approval:

    * Deduct requested quantity from inventory
    * Update status → Approved
  * If insufficient stock:

    * Disable approval OR show error message

* **Rejection Logic**

  * Update status → Rejected
  * No inventory change

---

## **6. Staff Functional Requirements**

### **6.1 Dashboard**

* Display:

  * Available items (only items with quantity > 0)
  * Simple card or list view

---

### **6.2 Request Submission**

* Request Form Fields:

  * Item selection (dropdown)
  * Quantity input

* **Validation Rules**

  * Quantity must be > 0
  * Quantity must not exceed available stock

* **Submission Flow**

  * On submit:

    * Create request with status = Pending
    * Save in `localStorage`
    * Show success notification

---

### **6.3 Request History**

* Display user-specific requests:

  * Item Name
  * Quantity
  * Status
  * Date

* **Status Indicators**

  * Pending → Yellow
  * Approved → Green
  * Rejected → Red

---

## **7. Data Management**

* **Storage Mechanism**

  * Use `localStorage` for:

    * Users (credentials & password updates)
    * Inventory items
    * Requests

* **Data Structures**

  * Inventory Object:

    * id, name, category, quantity, threshold
  * Request Object:

    * id, user, itemId, quantity, status, timestamp

---

## **8. UI/UX Requirements**

* **Design Principles**

  * Clean, modern dashboard UI
  * Mobile-first responsive design

* **Layout**

  * Sidebar navigation:

    * Dashboard
    * Inventory (Admin only)
    * Requests
    * Logout
  * Main content area for:

    * Tables
    * Forms
    * Cards

* **User Feedback**

  * Toast notifications:

    * Success (green)
    * Error (red)
  * Loading indicators (optional)

* **Visual Indicators**

  * Low stock alerts
  * Status color coding
  * Disabled buttons when invalid

---

## **9. Technical Requirements**

* **Frontend Stack (Suggested)**

  * HTML5
  * CSS3 (or Tailwind CSS)
  * JavaScript (Vanilla or React)

* **Architecture**

  * SPA (Single Page Application)
  * Component-based structure (if using framework)

* **State Management**

  * Local state + `localStorage`

---

## **10. Non-Functional Requirements**

* **Performance**

  * Fast load time (<2 seconds)
  * Smooth UI transitions

* **Usability**

  * Minimal learning curve
  * Clear navigation

* **Security (Prototype Level)**

  * Basic credential validation
  * Password masking

* **Scalability (Future Ready)**

  * Structure code for easy backend integration

---

## **11. Future Enhancements**

* Backend integration (Node.js / Firebase / Django)
* Real authentication system (JWT, OAuth)
* Email notifications for approvals
* Role expansion (Storekeeper, Manager)
* Reporting & analytics dashboard

---



