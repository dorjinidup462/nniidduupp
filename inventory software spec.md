
SELICE COMPANY
Business Requirements Specification
Internal Inventory Management System (IMS)

Document Version	1.0 — Initial Release
Prepared By	Business Analysis Team
Date	April 22, 2026
Status	Draft — Pending Stakeholder Review
Confidentiality	Internal Use Only

This document is the authoritative specification for the Selice Company IMS. Developers must not begin implementation on any feature until the relevant section has been signed off by the Warehouse Manager and IT Lead.
 
1.  Business Context
1.1  Background
Selice Company currently manages internal stock allocation and issuance through  emails. There is no centralised system to track what items exist, how much is available, who requested what, or whether a request was approved or fulfilled. This creates regular stock discrepancies, or even delays.

1.2  Problem Statement
The absence of a formal inventory management process results in:
•	Stock issued without written approval or record — no audit trail exists
•	Admin staff overwhelmed with informal, untracked item requests via phone or message
•	Staff unable to raise formal item requests — no standard process
•	No visibility into current stock levels, consumption patterns, or reorder needs
•	Duplicate requests, lost requests, and over-issuance go undetected

1.3  Business Objectives
The IMS must deliver the following measurable outcomes:
•	100% of stock issuances are recorded digitally with an approval trail
•	Admin can notify staff a stock issuance notification directly from the system
•	Staff can submit item requests online 
•	Admin can approve or reject requests with a reason — all decisions recorded
•	Real time stock balance visible to Admin at all times
•	All user accounts are centrally managed — access revoked within minutes when staff leave

1.4  Scope
In Scope — Phase 1
•	Role-based login: Admin and Staff user types with separate experiences
•	Default password system with mandatory first-login password change
•	Admin dashboard: user management, item catalogue, stock recording, request approvals
•	Admin can switch to a Staff view to submit personal item requests on their own behalf
•	Staff dashboard: submit item requests, view request status, view own history
•	Email notifications: admin-triggered issuance emails sent to staff
•	Audit log of all key actions

Out of Scope — Phase 1
•	Integration with accounting or ERP software
•	Barcode scanning hardware
•	Supplier/vendor portal
•	Mobile application (web-responsive design is required; native app is not)
•	Automated purchase order generation
 
2.  Stakeholders & User Roles
2.1  Stakeholder Map
Stakeholder	Role in Project	Interest / Concern
Warehouse Manager / Admin	Primary system user; owns approvals and stock data	Accurate stock records; fast request processing; full audit trail
General Staff	End users submitting item requests	Simple request process; visibility into request status
IT Administrator	Sets up and maintains the system	Clean authentication model; minimal maintenance overhead
Company Management	Sponsors; receives reports	Cost control; accountability; no stock wastage

2.2  User Role Definitions
There are exactly two roles in Phase 1: Admin and Staff. The Admin cannot use their Admin account to submit personal item requests — they must switch to a Staff-mode session to do so. This is a deliberate design decision to maintain clean audit separation.

Role	Who Holds It	Core Permissions	Cannot Do
Admin	Warehouse Manager(s) only	Full user management, item catalogue management, stock recording, approve/reject requests, trigger issuance emails, view all reports and audit logs	Submit item requests from the Admin dashboard (must use Staff mode)
Staff	All other employees	Submit item requests, view own request history and status, update own profile and password	Approve requests, edit stock levels, view other users' requests, access admin functions
 
3.  Login Feature
3.1  Objective
Provide a secure, user-type-aware login flow that ensures every session is authenticated, role-appropriate, and protected by a mandatory password-change policy for new accounts. The login experience must clearly distinguish Admin from Staff before credentials are entered.

3.2  Login Flow — Step by Step
Step	Screen / Action	System Behaviour
1	User visits the IMS URL	System displays the Landing / Role Selection screen. No username or password fields are shown yet.
2	User selects their user type	Two clearly labelled buttons are shown: '🔑 Admin Login' and '👤 Staff Login'. User taps one.
3	Login form appears for selected role	Form shows: Email field, Password field, and a 'Show/Hide password' toggle. The header clearly displays the selected role (e.g. 'Admin Login' or 'Staff Login').
4	User enters credentials	Email = their company email. Default password format = first initial + last name (e.g. John Smith → jsmith). Case-insensitive.
5	System validates credentials	Checks email exists, role matches selected type, and password is correct. Failed attempt increments counter.
6a	Success — first login	If it is the user's first login (password has not been changed), system redirects to a mandatory Password Change screen before any dashboard access is granted.
6b	Success — returning user	System redirects to the role-appropriate dashboard (Admin Dashboard or Staff Dashboard).
6c	Failure	Error shown: 'Invalid email or password.' Counter incremented. After 5 consecutive failures → account locked. Admin must unlock it.

3.3  Functional Requirements — Login
LG-FR-01	User Story	Must Have
As any user, I want to select whether I am an Admin or Staff before entering my credentials so that the system loads the correct login context and dashboard.
Acceptance Criteria	A role-selection screen is shown FIRST at the login URL — before any credential fields appear. Two options displayed: 'Admin Login' and 'Staff Login'. Selecting one takes the user to the appropriate login form. A 'Back' link returns to role selection.

LG-FR-02	User Story	Must Have
As a new user (Admin or Staff), I want to log in with my email and default password (first initial + last name) so that I can access the system on my first day without IT intervention.
Acceptance Criteria	Default password is auto-generated as [first initial][last name] in lowercase (e.g. jsmith). Password is case-insensitive at this stage. On successful first login, system does NOT load the dashboard — it redirects to the mandatory Password Change screen.

LG-FR-03	User Story	Must Have
As a first-time user, I want to be forced to change my default password before accessing any feature so that my account is secure from day one.
Acceptance Criteria	Password Change screen shows: Current Password, New Password, Confirm New Password. New password must be min 8 characters, contain at least 1 uppercase letter, 1 lowercase letter, and 1 number. The default password cannot be reused as the new password. User cannot navigate away from this screen until the change is complete. On success, session is established and user is taken to their dashboard.

LG-FR-04	User Story	Must Have
As a returning user, I want to log in and be taken directly to my role dashboard so that I can start working without friction.
Acceptance Criteria	If password has been previously changed, system loads the correct dashboard: Admin → Admin Dashboard; Staff → Staff Dashboard. No intermediate screens.

LG-FR-05	User Story	Must Have
As a user who forgets their password, I want to reset it via a link sent to my registered email so that I can regain access without contacting IT.
Acceptance Criteria	'Forgot Password?' link on login form. User enters registered email → system sends reset link valid for 60 minutes. Link loads a reset form requiring New Password and Confirm Password (same rules as FR-03). After reset, user is taken to login screen. Reset link is single-use and expires after use.

LG-FR-06	User Story	Must Have
As a user who enters wrong credentials 5 times, I want my account to be locked so that brute-force attacks are prevented.
Acceptance Criteria	After 5 consecutive failed login attempts: account status set to LOCKED. User sees: 'Your account has been locked. Please contact your administrator.' Admin sees the account flagged in User Management and can unlock it with one click.

LG-FR-07	User Story	Must Have
As any logged-in user, I want to be automatically logged out after 30 minutes of inactivity so that my session is not left open on a shared device.
Acceptance Criteria	Inactivity timer starts on last user action. At 28 minutes: toast notification 'You will be logged out in 2 minutes.' At 30 minutes: session ends, user redirected to login with message: 'Your session expired. Please log in again.'

LG-FR-08	User Story	Should Have
As an Admin, I want to view a login audit log so that I can detect suspicious access patterns.
Acceptance Criteria	Audit log records: User ID, email, role, login timestamp, IP address, outcome (Success / Failed / Locked). Filterable by date range, user, and outcome. Exportable to CSV.

3.4  UX Requirements — Login
Ref	UX Requirement
LG-UX-01	Role selection buttons must be large, visually distinct, and clearly labelled — e.g. blue for Admin with a key icon, green for Staff with a person icon.
LG-UX-02	The selected role must be clearly displayed on the login form header so the user knows which context they are logging into.
LG-UX-03	Password field must include a show/hide toggle icon.
LG-UX-04	Error messages must not specify whether the email or password was incorrect (security requirement). Always display: 'Invalid email or password.'
LG-UX-05	The mandatory password change screen must explain the password rules before the user types. Rules shown as a checklist that turns green as each condition is met.
LG-UX-06	Login page must be fully responsive on desktop, tablet, and mobile browsers.
LG-UX-07	Pressing Enter/Return on the password field must submit the login form.
 
4.  Admin Dashboard
4.1  Objective
Provide the Admin (Warehouse Manager) with a centralised control centre to manage users, the item catalogue, real-time stock levels, incoming staff requests, and outgoing issuance communications. The Admin dashboard is the operational heart of the IMS.

4.2  Dashboard Overview Screen
On login, the Admin sees a summary dashboard with the following widgets:
Widget	Content	Action Available
Pending Requests	Count of staff item requests awaiting approval	Click → navigates to Request Approval module
Low Stock Items	Count of items at or below minimum stock level	Click → navigates to filtered Item Catalogue view
Total Inventory Value	Sum of (Unit Cost × Current Quantity) across all items	Click → navigates to full catalogue
Active Users	Count of active Staff and Admin accounts	Click → navigates to User Management
Recent Activity	Last 10 actions performed by any user (with timestamp and user)	View only
Switch to Staff Mode	Prominent button — allows Admin to act as a Staff user to submit personal item requests	Click → opens Staff mode session (see Section 4.7)

4.3  Module: User Management
Functional Requirements
AD-FR-01	User Story	Must Have
As an Admin, I want to create new user accounts so that new employees can access the system from their first day.
Acceptance Criteria	Create User form fields: Full Name (required), Email (required, must be unique, validated format), Role (dropdown: Admin / Staff), Department (optional free text), Default Password auto-displayed as [first initial][last name] in lowercase — Admin can copy it to share with the user. New account status = ACTIVE, First Login = TRUE. System sends a welcome email to the user's address with their default password and login instructions.

AD-FR-02	User Story	Must Have
As an Admin, I want to edit a user's account details so that name, email, department, or role changes are kept current.
Acceptance Criteria	Admin can edit: Full Name, Email, Department, Role. Changes are saved immediately and logged in the audit trail with old value and new value. If email is changed, user must re-verify the new email before next login. Role changes take effect on the user's next login.

AD-FR-03	User Story	Must Have
As an Admin, I want to deactivate a user account so that former employees or contractors lose access immediately.
Acceptance Criteria	Deactivate button on each user record. Confirmation dialog: 'Deactivate [Name]? They will be unable to log in immediately.' Deactivated users are shown in the user list with a greyed INACTIVE badge. Their historical records, requests, and audit entries are fully retained. Deactivated users cannot log in — system shows: 'Your account has been deactivated. Contact your administrator.' Admin can re-activate at any time.

AD-FR-04	User Story	Must Have
As an Admin, I want to unlock a locked user account so that a legitimate user who was locked out can regain access.
Acceptance Criteria	User Management list shows a red LOCKED badge for locked accounts. Admin clicks 'Unlock' → one-click action, no confirmation required. User can attempt login again immediately. Unlock action is logged in the audit trail.

AD-FR-05	User Story	Must Have
As an Admin, I want to reset a user's password so that I can assist staff who cannot use the self-service reset.
Acceptance Criteria	Admin clicks 'Reset Password' on a user record → system immediately resets the password to the default ([first initial][last name]) and sets First Login = TRUE. User receives email notification that their password has been reset. They will be forced to change it on next login.

AD-FR-06	User Story	Should Have
As an Admin, I want to search and filter the user list so that I can quickly find a specific account.
Acceptance Criteria	Search bar filters by name or email in real time. Filter dropdown: All / Active / Inactive / Locked / Admin / Staff. Results update as Admin types. Default sort: Active accounts first, then alphabetical by name.


UX Ref	UX Requirement — User Management
AD-UX-01	User list displays: Name, Email, Role (badge), Department, Status (badge: Active / Inactive / Locked), Last Login, Actions.
AD-UX-02	Deactivating an account requires a confirmation modal — destructive actions must never execute on a single click.
AD-UX-03	Default password shown in the Create User form must have a one-click copy button.

4.4  Module: Item Catalogue & Stock Management
Functional Requirements
AD-FR-10	User Story	Must Have
As an Admin, I want to add new inventory items to the catalogue so that all stockable goods are tracked.
Acceptance Criteria	Add Item form fields: Item Name (required), Item Code (auto-generated: ITM-XXXXX, editable), Category (dropdown + 'Add New' option), Unit of Measure (e.g. pcs, kg, box, litre), Current Quantity (required, integer ≥ 0), Minimum Stock Level (required — threshold for low-stock alert), Reorder Quantity (suggested order amount), Unit Cost (optional, decimal ≥ 0), Description / Notes (optional). Duplicate Item Code blocked on save.

AD-FR-11	User Story	Must Have
As an Admin, I want to edit an existing item's details so that the catalogue reflects accurate information.
Acceptance Criteria	Admin can edit all fields except Item Code. Changes logged: field changed, old value, new value, editor, timestamp. Quantity changes made through this form are classified as 'Admin Adjustment' in the audit trail, not as a Stock IN/OUT transaction.

AD-FR-12	User Story	Must Have
As an Admin, I want to record a stock quantity change (Stock IN or Stock OUT) so that inventory movements are formally tracked.
Acceptance Criteria	Stock Movement form: Transaction Type (Stock IN / Stock OUT), Item (searchable dropdown), Quantity (positive integer), Reference (e.g. delivery note number or PO number — optional), Notes (optional), Date (defaults to today, editable). System validates: Stock OUT cannot reduce quantity below zero — error: 'Insufficient stock. Available: [X] units.' Successful transaction updates current quantity immediately and logs the movement.

AD-FR-13	User Story	Must Have
As an Admin, I want to deactivate an item so that discontinued goods are removed from request forms without deleting historical data.
Acceptance Criteria	Deactivate Item sets status = INACTIVE. Inactive items do not appear in Staff request dropdowns or Stock Movement forms. Historical records referencing the item are retained. Admin can reactivate. A filter toggle on the catalogue allows Admin to view inactive items.

AD-FR-14	User Story	Should Have
As an Admin, I want to import items in bulk via a CSV file so that the initial catalogue setup is fast.
Acceptance Criteria	A downloadable CSV template is available. Admin uploads completed CSV. System validates all rows before any are imported (all-or-nothing for each batch). Validation errors shown per row with specific field. On success: confirmation showing how many items were imported.


UX Ref	UX Requirement — Item Catalogue
AD-UX-10	Items with quantity at or below Minimum Stock Level are highlighted with a red LOW STOCK badge in the catalogue list.
AD-UX-11	Item list supports: search by name or code, filter by category and status, column sort (name, quantity, last updated). Pagination at 25 rows.
AD-UX-12	Clicking an item opens a detail view showing full info, stock movement history for that item, and all requests that referenced it.

4.5  Module: Request Approval
Functional Requirements
AD-FR-20	User Story	Must Have
As an Admin, I want to view all pending staff item requests so that I can action them in a timely manner.
Acceptance Criteria	Request Approval screen shows a list of all requests with status = PENDING. Columns: Request ID, Staff Name, Item Requested, Quantity, Date Submitted, Priority (if set by staff), Notes. Default sort: oldest first. Admin can filter by: All / Pending / Approved / Rejected. Count badge on the navigation menu shows number of pending requests.

AD-FR-21	User Story	Must Have
As an Admin, I want to approve a staff item request so that the stock is formally allocated and the staff member is notified.
Acceptance Criteria	Admin clicks 'Approve' on a request. A modal appears with: Item, Quantity Requested, Current Stock (live figure), Quantity to Issue (pre-filled with requested qty, editable). Admin clicks 'Confirm Approval'. System: (1) Deducts the issued quantity from stock as a Stock OUT transaction linked to this request. (2) Changes request status to APPROVED. (3) Sends an automatic email to the requesting staff member (see Section 4.6). Approval blocked if current stock is less than the quantity to issue — Admin shown: 'Insufficient stock. Available: [X] units.' Admin can edit the issued quantity before confirming.

AD-FR-22	User Story	Must Have
As an Admin, I want to reject a staff item request with a reason so that the staff member understands why it was declined.
Acceptance Criteria	Admin clicks 'Reject' on a request. A modal requires: Rejection Reason (mandatory text field, min 10 characters). Admin clicks 'Confirm Rejection'. System: (1) Changes request status to REJECTED. (2) Sends an automatic email to the requesting staff member with the rejection reason. No stock is deducted. Rejection reason is visible to the staff member in their request history.

AD-FR-23	User Story	Must Have
As an Admin, I want to view the full detail of any request so that I have full context before approving or rejecting.
Acceptance Criteria	Clicking a request opens a detail panel/modal showing: all request fields, requester profile summary, current stock level of the requested item, the item's recent transaction history, and all previous requests for the same item in the past 90 days.


4.6  Email Notifications from Admin
This is a key requirement from Selice Company. The Admin must be able to trigger a formal issuance email to a staff member directly from within the system. This email serves as the official record that an item has been issued.

AD-FR-24	User Story	Must Have
As an Admin, I want the system to automatically send an issuance email to the staff member when I approve their request so that they receive a formal written record of what was issued to them.
Acceptance Criteria	On request approval (AD-FR-21), the system sends an HTML email to the staff member's registered email address. The email must contain: Selice Company logo/header, Staff member's full name, Request ID (for reference), Item name and Item Code, Quantity issued, Date of issuance, Admin's name (approver), Any notes added during approval, A footer reminding the staff member to collect the item from the warehouse within [configurable] working days. The email is logged in the Audit Log with timestamp and recipient.

AD-FR-25	User Story	Must Have
As an Admin, I want to send a manual ad-hoc issuance email to any staff member so that I can notify them of stock allocated outside of the formal request workflow.
Acceptance Criteria	In the Admin dashboard, a 'Send Issuance Notification' button allows Admin to manually compose an issuance email: Select Staff Member (dropdown of all active staff), Select Item, Enter Quantity Issued, Date (default today), Notes/Message (optional). Preview shown before send. System sends the email and logs the action with all fields recorded. This also records a corresponding Stock OUT transaction for the issued quantity.

AD-FR-26	User Story	Should Have
As an Admin, I want to view a log of all issuance emails sent so that I have a communication audit trail.
Acceptance Criteria	Email Log screen shows: Date/Time, Recipient (name + email), Item, Quantity, Trigger (Auto-Approval / Manual), Admin who sent, Status (Sent / Failed). Failed emails are highlighted in red. Admin can resend a failed email with one click.


4.7  Admin Staff Mode — Personal Item Requests
The Admin cannot submit item requests from their Admin account dashboard. To request items for personal use, the Admin must explicitly switch to a Staff-mode session. This prevents requests from being approved by the same person who submitted them, maintaining process integrity.

AD-FR-30	User Story	Must Have
As an Admin, I want to switch to Staff mode so that I can submit item requests for my own use through the same process as regular staff.
Acceptance Criteria	A prominent 'Switch to Staff Mode' button is shown on the Admin dashboard. Clicking it loads the Staff Dashboard view within the same session. A persistent banner at the top of every screen reads: '🔄 Staff Mode — You are viewing as Staff. [Return to Admin Dashboard]' The Admin's requests submitted in Staff Mode are visible in the Admin's Request Approval queue but cannot be approved by the same Admin account — they require another Admin to approve, OR the system can be configured to allow self-approval with an explicit acknowledgement modal (configurable setting).


4.8  Module: Reports
Report ID	Report Name	Description	Access
RPT-01	Current Stock Level Report	All active items with current qty, min level, LOW STOCK flag, last movement date. Filter by category.	Admin
RPT-02	Stock Movement History	All Stock IN/OUT transactions in a date range. Filter by item, type, date. Export to Excel.	Admin
RPT-03	Request History Report	All requests in a date range with outcome, requester, item, qty, approver. Export to Excel.	Admin
RPT-04	Issuance by Staff Report	Total items issued per staff member over a period. Useful for usage audits.	Admin
RPT-05	Audit Log	Full system action log: user, action, entity, old/new value, timestamp, IP. Export to CSV.	Admin only
 
5.  Staff (User) Dashboard
5.1  Objective
Provide all Selice Company staff with a simple, focused interface to submit item requests, track the status of their requests, and manage their own account. The Staff experience is intentionally streamlined — staff should have no access to catalogue management, other users' data, or any administrative function.

5.2  Dashboard Overview Screen
On login, the Staff user sees a clean dashboard with:
Widget	Content
My Pending Requests	Count and list of their own requests with status PENDING
My Approved Requests	Requests approved and ready for collection
Quick Action Button	Large prominent 'Submit New Request' button
Recent Notifications	Last 5 email notifications received (approval / rejection) with dates
My Request History Summary	Short table of their last 10 requests with outcome

5.3  Module: Item Request Submission
Functional Requirements
USR-FR-01	User Story	Must Have
As a Staff member, I want to submit an item request so that I can formally ask the Admin to issue stock to me.
Acceptance Criteria	Item Request form fields: Item (searchable dropdown — only ACTIVE items shown), Quantity Required (positive integer, mandatory), Urgency / Priority (dropdown: Normal / Urgent — optional), Reason / Purpose (free text, optional but encouraged). On submit: Request created with status = PENDING. Request ID assigned (format: REQ-YYYYMMDD-XXXX). Staff member sees confirmation: 'Your request REQ-[ID] has been submitted. You will be notified by email once it is reviewed.' Admin receives a notification (badge count on their dashboard updates in real time).

USR-FR-02	User Story	Must Have
As a Staff member, I want to view the status of all my requests so that I know which have been approved, rejected, or are still pending.
Acceptance Criteria	My Requests page shows all requests submitted by the logged-in user. Columns: Request ID, Item, Quantity Requested, Quantity Issued (shown once approved), Date Submitted, Status (PENDING / APPROVED / REJECTED), Rejection Reason (shown if rejected). Default sort: most recent first. Filter by status.

USR-FR-03	User Story	Must Have
As a Staff member, I want to cancel a pending request so that I can withdraw it if I no longer need the item.
Acceptance Criteria	A 'Cancel' button is shown next to each request with status = PENDING. Clicking prompts: 'Cancel request REQ-[ID]? This cannot be undone.' On confirm: status changes to CANCELLED. Cancelled requests are visible in history but cannot be reactivated. Requests with status APPROVED or REJECTED cannot be cancelled.

USR-FR-04	User Story	Must Have
As a Staff member, I want to see the rejection reason when my request is declined so that I understand why and can act accordingly.
Acceptance Criteria	Rejected requests in the Staff's request list show a 'See Reason' link. Clicking opens a small modal or inline expanded row showing: the rejection reason written by the Admin, the date rejected, and the Admin's name. Staff can use this to resubmit a modified request if appropriate.

USR-FR-05	User Story	Should Have
As a Staff member, I want to resubmit a rejected request with modifications so that I can correct my original request without starting from scratch.
Acceptance Criteria	A 'Resubmit' button appears on rejected requests. Clicking pre-fills the request form with the original values. Staff can modify any field. The new submission is a fresh request with a new Request ID. The original rejected request is referenced in the notes as 'Resubmission of REQ-[original ID]'.

USR-FR-06	User Story	Must Have
As a Staff member, I want to update my password so that I can maintain the security of my account.
Acceptance Criteria	Profile page has a 'Change Password' section. Fields: Current Password, New Password, Confirm New Password. Same password rules as first-login change. Success message shown. Current session remains active after password change.


5.4  UX Requirements — Staff Dashboard
UX Ref	UX Requirement
USR-UX-01	The 'Submit New Request' button must be the most prominent element on the Staff dashboard — large, coloured, and above the fold on any screen size.
USR-UX-02	Status badges use colour coding: PENDING = amber, APPROVED = green, REJECTED = red, CANCELLED = grey.
USR-UX-03	The item dropdown in the request form must be searchable by item name. It must NOT show item codes, quantities, or prices to staff — only the name and unit of measure.
USR-UX-04	After submitting a request, the Staff member must not be able to submit the same item again while a PENDING request for that item already exists. System warns: 'You already have a pending request for [Item Name].'
USR-UX-05	Email notifications received (approval/rejection) must be mirrored as in-app notifications in the Staff dashboard, shown with an unread badge.
USR-UX-06	Staff interface must be clean and minimal — staff must not see stock quantities, other users' requests, or any admin functions.
 
6.  Non-Functional Requirements
ID	Category	Requirement	Target / Measure
NFR-01	Performance	Page load time for all screens	< 3 seconds on standard broadband connection
NFR-02	Performance	Real-time stock balance update after transaction	< 2 seconds
NFR-03	Availability	System uptime during business hours (Mon–Sat, 7am–7pm)	99.5% minimum
NFR-04	Security	Password storage	Hashed with bcrypt (min cost factor 12) — never stored in plain text
NFR-05	Security	All data transmission	HTTPS / TLS 1.2 or higher — mandatory
NFR-06	Security	Role-based access enforcement	Enforced server-side on every API call — not just front-end
NFR-07	Security	Email notifications	Sent via authenticated SMTP or transactional email service (e.g. SendGrid, Mailgun)
NFR-08	Scalability	Concurrent users supported	Up to 100 concurrent users in Phase 1
NFR-09	Scalability	Item catalogue size	Up to 5,000 active SKUs
NFR-10	Usability	New Staff onboarding	Staff must be able to submit their first request within 5 minutes of first login, with no training
NFR-11	Usability	Browser compatibility	Chrome (latest), Firefox (latest), Edge (latest), Safari (latest) on desktop and tablet
NFR-12	Audit	Data changes logged	All create/edit/delete/approve/reject actions logged with: UserID, action, entity, old value, new value, timestamp
NFR-13	Data Retention	Minimum data retention	All records (transactions, requests, emails, audit logs) retained for 5 years
NFR-14	Compliance	Password policy enforcement	System blocks reuse of last 3 passwords
 
7.  Business Rules
Rule ID	Module	Rule Description
BR-01	Stock Management	Stock quantity can never go below zero. Any transaction (Stock OUT or Request Approval) that would result in a negative balance is blocked. Error message: 'Insufficient stock. Available: [X] units.'
BR-02	Login	Default password for all new users is [first initial][last name] in lowercase (e.g. John Smith → jsmith). This is case-insensitive on first login only.
BR-03	Login	Users must change their default password before accessing any feature of the system. The mandatory password change screen cannot be bypassed or skipped.
BR-04	Login	After 5 consecutive failed login attempts, the account is locked. Only an Admin can unlock it. The lock persists indefinitely until manually cleared.
BR-05	User Management	Deactivated users cannot log in. Their data is never deleted. Deactivation is reversible — Admin can reactivate at any time.
BR-06	Request Approval	An Admin cannot approve their own item requests submitted in Staff Mode without an explicit system-level configuration enabling self-approval (disabled by default). This must be a configurable setting.
BR-07	Request Approval	A staff member cannot have two PENDING requests for the same item simultaneously. A new request for the same item is blocked until the existing pending request is resolved.
BR-08	Stock Transactions	All stock movements (IN/OUT) are immutable once recorded. They cannot be edited or deleted. Corrections must be made via a counter-entry (reversal transaction) with a mandatory reason.
BR-09	Issuance Email	Every approved request must trigger an issuance email to the requesting staff member. This email cannot be suppressed unless the email service is down (in which case the failure is logged and a retry attempted after 5 minutes).
BR-10	Item Catalogue	Minimum Stock Level must be less than or equal to the item's Reorder Quantity. System validates this on save and blocks save if violated.
BR-11	Passwords	New password cannot be the same as the current password or any of the last 3 passwords used by that account.
 
8.  Data Requirements
8.1  Key Data Entities
Entity	Key Attributes	Notes
User	UserID, FullName, Email (unique), Role (Admin/Staff), Department, Status (Active/Inactive/Locked), FirstLogin (boolean), PasswordHash, CreatedAt, LastLoginAt	Soft-delete only — never hard delete
InventoryItem	ItemCode (unique), Name, Category, UoM, CurrentQuantity, MinStockLevel, ReorderQuantity, UnitCost, Description, Status, CreatedAt, LastUpdatedAt	Status: Active / Inactive
StockTransaction	TxnID, Type (IN/OUT/Adjustment/Reversal), ItemCode, Quantity, BalanceAfter, Reference, Notes, PerformedBy (UserID), LinkedRequestID (nullable), Timestamp	Immutable after creation
ItemRequest	RequestID, RequestedBy (UserID), ItemCode, QuantityRequested, QuantityIssued, Priority, Reason, Status, SubmittedAt, ReviewedBy (UserID), ReviewedAt, RejectionReason, ResubmissionOf (nullable)	Status: Pending/Approved/Rejected/Cancelled
EmailLog	EmailID, Recipient (UserID + Email), Subject, Trigger (Auto/Manual), ItemCode, Quantity, SentBy (Admin UserID), SentAt, Status (Sent/Failed), RetryCount	Retained for audit trail
AuditLog	LogID, UserID, Action, EntityType, EntityID, OldValue (JSON), NewValue (JSON), IPAddress, Timestamp	Read-only — no updates or deletes
PasswordHistory	UserID, PasswordHash, ChangedAt	Last 3 hashes retained per user for reuse prevention

8.2  Data Validation Rules
Field	Rule
Email	Must match standard email format (RFC 5322). Must be unique across all users.
Quantity fields	Positive integers only (whole units). Exception: items with UoM = 'kg' or 'L' allow up to 2 decimal places.
Item Code	Auto-generated format: ITM-XXXXX (5 digits, zero-padded). Editable by Admin but must remain unique.
Request ID	Auto-generated format: REQ-YYYYMMDD-XXXX (4-digit sequential per day).
Unit Cost	Decimal ≥ 0.00. Maximum 4 decimal places. Optional field — defaults to 0 if not provided.
Password	Min 8 characters. Must contain: 1 uppercase, 1 lowercase, 1 number. No spaces allowed.
Min Stock Level	Integer ≥ 0. Must be strictly less than or equal to Reorder Quantity.
 
9.  Key Process Flows
9.1  New User First Login Flow
Step	Actor	Action	System Response
1	Admin	Creates user account in User Management	System auto-generates default password [first initial][last name]. Welcome email sent to user.
2	New User	Visits login page, selects their role (Admin or Staff)	Role-specific login form displayed
3	New User	Enters email and default password	Credentials validated. First Login = TRUE detected.
4	System	Detects first login	Redirects to mandatory Password Change screen. Dashboard NOT accessible yet.
5	New User	Sets new password meeting all rules	System hashes and saves new password. First Login set to FALSE. Password history record created.
6	System	Redirects to dashboard	User lands on their role-appropriate dashboard and can begin using the system.

9.2  Staff Item Request → Approval → Issuance Email Flow
Step	Actor	Action	System Response
1	Staff	Logs in and clicks 'Submit New Request'	Request form opens. Only active items shown in dropdown.
2	Staff	Selects item, enters quantity, adds reason	System checks: no existing PENDING request for the same item. If found: blocks submission with warning.
3	Staff	Submits request	Request saved with status = PENDING. Confirmation shown. Admin dashboard pending count badge increments.
4	Admin	Sees new request in Request Approval queue	Admin opens request detail. Sees current stock level, item history, and requester info.
5	Admin	Clicks 'Approve'	Approval modal shows: item, requested qty, current stock, editable issued qty.
6	Admin	Confirms issued quantity and approves	Stock OUT transaction recorded. Request status → APPROVED. Automatic issuance email sent to staff.
7	System	Sends issuance email	Email delivered to staff member's registered email. Email logged in Email Log.
8	Staff	Receives email notification	Staff collects the item from the warehouse, referencing the Request ID in the email.

9.3  Admin Staff Mode — Personal Request Flow
Step	Actor	Action
1	Admin	From Admin Dashboard, clicks 'Switch to Staff Mode'
2	System	Loads Staff Dashboard view. Persistent banner shown: '🔄 Staff Mode — [Return to Admin Dashboard]'
3	Admin (as Staff)	Submits an item request using the standard Staff request form
4	System	Creates the request. Request appears in the Admin Approval queue with requester shown as the Admin's name.
5	Admin	Clicks 'Return to Admin Dashboard'
6	Admin / Another Admin	Reviews and approves the request in the Admin Approval queue (self-approval governed by BR-06)
 
10.  Assumptions & Constraints
10.1  Assumptions
•	All Selice Company staff have a company-issued or personal email address that will be used as their system login identifier.
•	An outbound email service (SMTP relay or transactional email API) will be available and configured before go-live.
•	The initial user list and item catalogue data will be provided by Selice Company in a structured format (spreadsheet or CSV) at least 2 weeks before User Acceptance Testing (UAT).
•	Selice Company will identify at least one IT contact who is responsible for hosting setup, SSL certificate management, and database backups.
•	Staff training will be delivered by the project team before go-live. A user guide will be provided for both Admin and Staff roles.
•	All users will have access to a device with a modern web browser (Chrome, Firefox, Edge, or Safari) and internet access.

10.2  Constraints
•	Technology: The system must be web-based. No native desktop or mobile application will be developed in Phase 1. The web application must be responsive on tablet and desktop screen sizes.
•	Authentication: No third-party SSO (e.g. Google, Microsoft) is required in Phase 1. The system manages its own user authentication.
•	Language: The system UI must be in English only for Phase 1.
•	Single company: The system is built for Selice Company only — no multi-tenancy required in Phase 1.
•	Phase 1 budget and timeline to be confirmed with the Selice Company sponsor before development begins.
 
11.  Glossary
Term	Definition
IMS	Inventory Management System — the software described in this specification
Admin	A user with the Admin role — typically the Warehouse Manager at Selice Company
Staff	A user with the Staff role — any Selice Company employee who needs to request stock
Staff Mode	A session mode available to Admin users that presents the Staff dashboard, allowing the Admin to submit personal item requests
Default Password	The auto-generated first-use password assigned to every new account: [first initial][last name] in lowercase (e.g. jsmith for John Smith)
First Login	The flag indicating that a user has not yet changed their default password. First Login = TRUE blocks dashboard access until the password is changed
Request	A formal item request submitted by a Staff user (or Admin in Staff Mode) asking for stock to be issued
Issuance Email	A system-generated or manually triggered email sent from Admin to Staff confirming that a stock item has been allocated and is ready for collection
Stock IN	A transaction that increases the quantity of an inventory item (e.g. delivery received)
Stock OUT	A transaction that decreases the quantity of an inventory item (e.g. item issued to staff)
Min Stock Level	The quantity threshold below which an item is flagged as LOW STOCK and highlighted for Admin attention
Reorder Quantity	The suggested quantity to procure when restocking a low-stock item
SKU	Stock Keeping Unit — a unique identifier for each distinct inventory item
UoM	Unit of Measure — the unit in which an item is counted (pcs, kg, litre, box, etc.)
Audit Log	A tamper-proof record of all system actions, retained for compliance and traceability
UAT	User Acceptance Testing — validation by Selice Company staff that the system meets these requirements before go-live
PENDING	Request status: submitted by Staff, not yet reviewed by Admin
APPROVED	Request status: reviewed and approved by Admin; stock deducted; issuance email sent
REJECTED	Request status: reviewed and declined by Admin; rejection reason recorded and communicated to Staff
 

