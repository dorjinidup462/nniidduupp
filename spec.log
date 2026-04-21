1. Functional Overview
The system provides two distinct entry points. While the UI style remains consistent, the backend authentication logic and post-login redirection differ based on the selected role.
Key Logic:
•	Role Selection: Users must choose their portal (Admin vs. Staff) before entering credentials.
•	Initial Credentialing: All new users are assigned a "Master" temporary password (e.g., Welcome@2026).
•	Force Change Workflow: A boolean flag in the database (is_first_login) triggers a mandatory password update.
________________________________________
2. User Interface (UI) Component
A. The Gateway Screen
Before the email/password fields are visible, the user is presented with two large, distinct cards or a toggle switch:
•	Option 1: "Login as Administrator" (High-level system access).
•	Option 2: "Login as Staff" (Operational access).
B. The Login Form
Once a role is selected, the form displays:
•	Header: Dynamic text (e.g., "Staff Portal Login").
•	Email Field: Standard text input with regex validation.
•	Password Field: Masked input with a "Show Password" toggle.
•	CTA Button: "Sign In".
________________________________________
3. The "First Login" Workflow
To ensure security, the system intercepts the login process if the account is new.
Step	Action	Description
1	Authentication	User enters Email + Default Password.
2	Flag Check	System checks if must_change_password == true.
3	Interception	Instead of the Dashboard, the user is redirected to /update-password.
4	Validation	User enters a "New Password" and "Confirm Password". The system ensures it is not the same as the default password.
5	Update	Database flag is set to false, and the user is redirected to their respective Dashboard.
________________________________________
4. Technical Specification
Database Schema Requirements
To support this template, your User table needs the following specific fields:
•	role: Enum (Admin, Staff)
•	email: String (Unique)
•	password_hash: String
•	is_first_login: Boolean (Default: True)
Security Constraints
•	Password Complexity: New passwords must meet a minimum standard (e.g., 8+ characters, 1 uppercase, 1 number).
•	Session Management: Sessions should expire after 30 minutes of inactivity.
•	Account Lockout: After 5 failed attempts, the account should lock for 15 minutes to prevent brute-force attacks on the default password.
________________________________________
5. Prototype Layout (Example)
Login as Administrator | Login as Staff
________________________________________
Staff Login
Email: [ email@company.com ]
Password: [ •••••••••••••• ]
[ Sign In ]
If it's your first time:
Security Notice: Update Required
Your account was created with a temporary password. Please set a permanent password to continue.
New Password: [ •••••••••• ]
Confirm Password: [ •••••••••• ]
[ Save & Continue ]

