# Email-AutomationKu
🤖 Python-based Gmail automation agent using Selenium. Automates login, compose, and send operations via command line. Built for AuditRAM Assignment 2.
📧 Gmail Automation Agent – AuditRAM Assignment 2

A fully automated browser-based Gmail email sender built using Python and Selenium WebDriver.
This automation script logs into Gmail, opens the compose window, fills in the recipient, subject, and body, and sends the email—either automatically or with manual fallback when required.

🚀 Features

🔐 Automated Gmail Login (with fallback for manual login if Google blocks automation)

📨 Automatic Compose & Send Email

🌍 Uses Selenium Manager (no need to install ChromeDriver manually)

🛡 Graceful Error Handling with prompts for manual steps

💻 Cross-platform: Works on Windows, macOS, Linux

🎯 Designed for AuditRAM Assessment 2 Requirements

📁 Project Structure
📦 AuditRAM Email Automation
│
├── email_automation.py        # Main automation script
├── README.md                  # Documentation (this file)
└── requirements.txt           # Python dependencies (selenium)

🛠️ Requirements
Component	Version
Python	3.7+
Google Chrome	Latest
Selenium	4.6+
Gmail App Password	Required

📌 Regular Gmail passwords will NOT work if 2FA is enabled. Use an App Password.

📦 Installation
1️⃣ Install Python dependencies
pip install selenium

2️⃣ Enable Gmail App Password (Important)

Go to:

Google Account → Security → 2-Step Verification → App Passwords → Generate

Use this 16-character password in the script.

▶️ Usage

Run the script from the terminal:

python email_automation.py \
   --email "your_email@gmail.com" \
   --password "your_app_password" \
   --to "scittest@auditram.com" \
   --subject "AuditRAM Assignment Email" \
   --body "This is an automated email sent using Selenium."

Example
python email_automation.py --email "test@gmail.com" --password "abcd efgh ijkl mnop" --to "scittest@auditram.com" --subject "Hello" --body "This email was automated!"

🔄 How It Works
✔ Step 1 — Launch Browser

Chrome opens using Selenium Manager.

✔ Step 2 — Login to Gmail

Automated login (email + password)

If Google blocks automation → script waits for manual login

✔ Step 3 — Open Compose Window

Automatically clicks "Compose".

✔ Step 4 — Fill To / Subject / Body

Multiple selectors ensure maximum compatibility.

✔ Step 5 — Send Email

Click "Send" → fallback to Ctrl + Enter shortcut if needed.

✔ Step 6 — Confirmation

Script waits for “Message sent” notification.

📸 Manual Intervention (Fallback Mode)

Gmail sometimes blocks automated login.
Your script already handles this:

Prompts user to manually login

Prompts user to manually click Compose

Prompts to manually fill fields if automation fails

This ensures 100% completion even with Gmail restrictions.

🧪 Assignment Checklist (AuditRAM Ready)
Requirement	Status
Login using browser automation	✅ Done
Compose an email	✅ Done
Send to scittest@auditram.com	✅ Supported
CLI-based input	✅ Included
Fully sequential flow	✅ Implemented
Error handling	✅ Advanced
🐞 Troubleshooting
❌ Gmail not logging in automatically

✔ Use App Password
✔ Ensure Chrome is up to date
✔ If blocked → Login manually in the opened window

❌ Compose button not detected

✔ Gmail UI may load slowly → wait 2–3 seconds
✔ Script falls back to manual click

❌ Email not sending

Try:

Click Send manually

Use shortcut Ctrl + Enter
