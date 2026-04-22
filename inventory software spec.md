SECTION 1 — LOGIN FEATURE
Objective: Provide secure, role-based access to the IMS so that only authorised personnel can access the system.

User Roles:
  • System Admin: Full access — can manage users, roles, and all modules
  • Warehouse Manager: Access to inventory, POs, approvals, and reports
  • Warehouse Staff: Record stock IN/OUT transactions at assigned location
  • Viewer / Auditor: Read-only access to reports and audit logs

Functional Requirements:
  [LG-FR-01] [Must Have]
  User Story: As any user, I want to log in with my email and password so that I can securely access the system.
  Acceptance Criteria: System validates credentials. On success, redirect to role-specific dashboard. On failure, show 'Invalid email or password' after 3 attempts → lock account for 15 minutes.

  [LG-FR-02] [Must Have]
  User Story: As any user, I want to reset my password via email so that I can regain access if I forget my credentials.
  Acceptance Criteria: User enters registered email → receives reset link valid for 60 minutes → sets new password with min 8 chars, 1 uppercase, 1 number.

  [LG-FR-03] [Must Have]
  User Story: As a System Admin, I want the system to enforce role-based access so that each user only sees what they are permitted to.
  Acceptance Criteria: After login, system loads permissions for user's role. Attempting to access a restricted URL returns HTTP 403 with message 'Access Denied'.

  [LG-FR-04] [Must Have]
  User Story: As any user, I want to be automatically logged out after inactivity so that unauthorised access is prevented.
  Acceptance Criteria: Session expires after 30 minutes of inactivity. User shown a 2-minute warning popup before logout. Unsaved form data preserved as draft for 24 hours.

  [LG-FR-05] [Should Have]
  User Story: As a System Admin, I want to view a login audit log so that I can monitor access patterns and detect suspicious activity.
  Acceptance Criteria: Log records: UserID, timestamp, IP address, success/failure. Exportable to CSV. Retained for 12 months.

UX Notes:
  • Login page must load within 2 seconds
  • Error messages must not reveal whether the email or password is incorrect (security best practice)
  • Password field must have show/hide toggle
  • Login page must be accessible on mobile and tablet browsers

─────────────────────────────────────────────────────────

SECTION 2 — ADMIN PAGE
Objective: Provide the System Admin with full control over users, item catalogue, locations, and system configuration.

Module: User Management
  [AD-FR-01] [Must Have]
  User Story: As an Admin, I want to create new user accounts so that staff can log in and use the system.
  Acceptance Criteria: Admin fills: Name, Email, Role (dropdown), Department, Location(s). System sends activation email to new user. Account inactive until user sets password.

  [AD-FR-02] [Must Have]
  User Story: As an Admin, I want to edit or deactivate user accounts so that access is kept up to date.
  Acceptance Criteria: Admin can change role, department, or location. Deactivated users cannot log in. Their historical records and transactions are retained unchanged.

  [AD-FR-03] [Must Have]
  User Story: As an Admin, I want to assign roles to users so that permissions are correctly enforced.
  Acceptance Criteria: Roles selectable from: Admin, Warehouse Manager, Warehouse Staff, Procurement Officer, Dept. Manager, Viewer. One role per user in Phase 1.

Module: Item Catalogue
  [AD-FR-10] [Must Have]
  User Story: As an Admin, I want to add new inventory items so that they can be tracked in the system.
  Acceptance Criteria: Required fields: Item Name, Category, Unit of Measure, Min Stock Level, Reorder Qty, Unit Cost. Item Code auto-generated (format: ITM-XXXXX). Duplicate Item Code blocked.

  [AD-FR-11] [Must Have]
  User Story: As an Admin, I want to edit existing items so that catalogue data remains accurate.
  Acceptance Criteria: Admin can edit all fields except Item Code. Changes logged with old value, new value, editor ID, and timestamp.

  [AD-FR-12] [Should Have]
  User Story: As an Admin, I want to bulk-import items via CSV so that initial setup is efficient.
  Acceptance Criteria: Downloadable CSV template provided. System validates all rows before import. Invalid rows shown with error detail; valid rows imported. Partial import supported.

Module: Location Management
  [AD-FR-20] [Must Have]
  User Story: As an Admin, I want to configure warehouse and office locations so that stock can be tracked per site.
  Acceptance Criteria: Admin adds: Location Name, Type (Warehouse/Office/Other), Address, Status (Active/Inactive). Minimum 1 location required for system operation.

Module: System Configuration
  [AD-FR-30] [Should Have]
  User Story: As an Admin, I want to configure global settings so that the system behaves according to company policy.
  Acceptance Criteria: Settings include: PO approval threshold (default $5,000), session timeout (default 30 min), email notification recipients, fiscal year start month.

  [AD-FR-31] [Must Have]
  User Story: As an Admin, I want to view the full audit log so that I can review all system activities.
  Acceptance Criteria: Log shows: User, Action, Entity, Old Value, New Value, Timestamp, IP. Filterable by user, date range, action type. Exportable to CSV.

Admin UX Notes:
  • Admin dashboard shows: total users, active items, active locations, pending approvals at a glance
  • All data tables support column sorting, search filtering, and pagination (25 rows default)
  • Confirmation dialog required for all destructive actions (deactivate, delete)
  • CSV export available on all list views

─────────────────────────────────────────────────────────

SECTION 3 — USER PAGE
Objective: Enable authorised staff to perform day-to-day inventory operations: recording transactions, managing purchase orders, and viewing reports relevant to their role.

Module: Dashboard
  [USR-FR-01] [Must Have]
  User Story: As any logged-in user, I want to see a role-relevant dashboard so that I immediately see what needs my attention.
  Acceptance Criteria: Dashboard shows widgets based on role. Warehouse Staff: pending transactions, low stock at their location. Manager: PO approvals pending, low stock summary, stock value. Procurement: open POs, overdue deliveries.

Module: Stock Transaction Recording
  [USR-FR-10] [Must Have]
  User Story: As Warehouse Staff, I want to record a Stock IN transaction so that received goods are added to inventory.
  Acceptance Criteria: Fields: Item (searchable), Location, Quantity, Date, Supplier (optional), Reference PO (optional), Notes. System updates stock balance in real time. Confirmation screen shows new balance.

  [USR-FR-11] [Must Have]
  User Story: As Warehouse Staff, I want to record a Stock OUT transaction so that issued goods are deducted from inventory.
  Acceptance Criteria: Fields: Item, Source Location, Quantity, Department/Requestor, Purpose. System blocks if quantity exceeds available stock (shows error with available balance). LOW STOCK alert triggered if new balance ≤ Min Stock Level.

  [USR-FR-12] [Must Have]
  User Story: As Warehouse Staff, I want to transfer stock between locations so that inter-site movements are tracked.
  Acceptance Criteria: Select: Item, From Location, To Location (different from source), Quantity. Single transaction creates a Stock OUT at source and Stock IN at destination simultaneously.

  [USR-FR-13] [Must Have]
  User Story: As Warehouse Manager, I want to record a stock adjustment so that variances, damages, or corrections are documented.
  Acceptance Criteria: Fields: Item, Location, Adjustment Qty (positive or negative), Reason (mandatory dropdown + notes), Date. Adjustments > 10% of current balance require a file attachment. Adjustments cannot be deleted — only reversed.

Module: Purchase Order Management
  [USR-FR-20] [Must Have]
  User Story: As a Procurement Officer, I want to create a Purchase Order so that restocking is formally planned and approved.
  Acceptance Criteria: Fields: Supplier, Line items (Item + Qty + Unit Price), Expected Delivery Date, Notes. System calculates PO total. Submitted PO enters 'Pending Approval' status.

  [USR-FR-21] [Must Have]
  User Story: As Warehouse Manager, I want to approve or reject Purchase Orders so that procurement is authorised.
  Acceptance Criteria: Manager sees pending POs list. Can approve (status → Approved) or reject with mandatory reason (status → Rejected). Procurement Officer notified by email. PO value > configured threshold requires secondary approval.

  [USR-FR-22] [Must Have]
  User Story: As Warehouse Staff, I want to record a Goods Receipt against a PO so that incoming stock is added to inventory.
  Acceptance Criteria: Select PO (filter: Approved/Ordered status). View ordered items. Enter received qty per line. System highlights discrepancies vs ordered qty. On submit: Stock IN transaction auto-created per line. PO status updates to Partially Received or Closed.

Module: Reports & Alerts
  [USR-FR-30] [Must Have]
  User Story: As a Manager, I want to view a stock level report so that I can see current inventory status across all locations.
  Acceptance Criteria: Filterable by: Location, Category, Status (All/Low Stock/Normal). Shows: Item, Current Qty, Min Level, Status flag, Last Movement date. Exportable to Excel and PDF.

  [USR-FR-31] [Must Have]
  User Story: As a Manager, I want to view transaction history so that I can audit all stock movements.
  Acceptance Criteria: Date range selector. Filter by: Transaction Type, Item, Location, User. Table shows all fields including reference numbers. Exportable to Excel.

  [USR-FR-32] [Must Have]
  User Story: As a Manager, I want to receive low stock email alerts automatically so that restocking is never missed.
  Acceptance Criteria: Alert sent when item stock ≤ Min Stock Level. Email includes: Item name, current qty, min level, location, link to create PO. Max 1 alert per item per 24-hour period.

User UX Notes:
  • Item search in transaction forms must support searching by Item Name or Item Code
  • All quantity fields must show unit of measure (e.g., '25 pcs', '3.5 kg')
  • Transactions submitted successfully show a green confirmation banner with transaction reference number
  • Low-stock items highlighted in red on all list views
  • Users can view their own transaction history for the past 30 days from their profile page

─────────────────────────────────────────────────────────

SECTION 4 — NON-FUNCTIONAL REQUIREMENTS
  [Performance] [Specify requirement] → Target: e.g. < 3 seconds page load
  [Availability] [Specify requirement] → Target: e.g. 99.5% uptime Mon–Sat 7am–7pm
  [Security] Password hashing → Target: bcrypt or Argon2
  [Security] Data transmission → Target: HTTPS / TLS 1.2+
  [Security] Role-based access enforced server-side → Target: Mandatory
  [Scalability] [Specify requirement] → Target: e.g. 200 concurrent users
  [Usability] [Specify requirement] → Target: e.g. Mobile-friendly on tablet browsers
  [Compliance] Data retention → Target: e.g. Minimum 5 years
  [Audit] All data changes logged → Target: UserID + timestamp + old/new values

─────────────────────────────────────────────────────────

SECTION 5 — BUSINESS RULES
  [BR-01] [Stock Transactions] Stock balance can never go below zero. Any transaction that would result in a negative balance must be blocked with error: 'Insufficient stock. Available: [X] units.'
  [BR-02] [Purchase Orders] Purchase Orders above the configured approval threshold (default: [INSERT VALUE]) require approval from both Warehouse Manager AND [INSERT ROLE].
  [BR-03] [Stock Adjustments] Stock adjustments greater than [X]% of current balance require a mandatory file attachment (e.g. damage report).
  [BR-04] [Item Catalogue] Min Stock Level must be less than Reorder Quantity. System validates this on item save.
  [BR-05] [All Transactions] Transactions cannot be deleted. Only a counter-entry (reversal) can be made, and both entries are retained in history.
  [BR-06] [User Management] A deactivated user cannot log in. All their historical records and transactions remain intact.
  [BR-07] [Purchase Orders] A closed PO cannot be reopened. A new PO must be created for any additional items.

─────────────────────────────────────────────────────────

SECTION 6 — GLOSSARY
  IMS: Inventory Management System — the software described in this spec
  SKU: Stock Keeping Unit — unique identifier for each distinct inventory item
  UoM: Unit of Measure — how an item is counted (pcs, kg, litre, box, etc.)
  PO: Purchase Order — formal document issued to a supplier to request goods
  Stock IN: Any transaction that increases stock quantity (goods received, returns)
  Stock OUT: Any transaction that decreases stock quantity (issuance, damage write-off)
  Min Stock Level: Minimum quantity threshold below which a LOW STOCK alert is triggered
  Reorder Qty: Recommended quantity to order when restocking a low-stock item
  Goods Receipt: Formal recording of goods arrived against a Purchase Order
  UAT: User Acceptance Testing — validation by end users that the system meets requirements
  RBAC: Role-Based Access Control — permissions granted based on a user's assigned role
  Audit Log: Tamper-proof record of all system actions for traceability and compliance
