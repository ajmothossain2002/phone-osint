# Phone OSINT Toolkit

A small Python-based toolkit for performing **public phone-number OSINT** on Windows 11.

The project currently provides:

- Phone-number validation
- Country code identification
- Numbering-region metadata
- Possible carrier information
- Time-zone information
- Public web search query generation
- Search queries for business/contact/social-media references

> **Important:** This toolkit does not track a phone's live location, access private accounts, bypass authentication, or hack devices. It is intended for legitimate OSINT and research using publicly available information.

---

## Requirements

- Windows 11
- Python 3.11+
- Internet connection
- Command Prompt or PowerShell

The project has been tested with:

```text
Python 3.14.4
```

---

# 1. Clone or Create the Project

If you already have the project:

```cmd
cd C:\Users\Ajmot\phone-osint
```

Your directory should eventually look similar to:

```text
phone-osint/
│
├── .venv/
├── phone_lookup.py
├── web_osint.py
└── README.md
```

---

# 2. Create a Virtual Environment

If `.venv` does not already exist:

```cmd
python -m venv .venv
```

---

# 3. Activate the Virtual Environment

Since the project can be run from Windows Command Prompt:

```cmd
.venv\Scripts\activate.bat
```

You should see:

```text
(.venv) C:\Users\Ajmot\phone-osint>
```

If you see `(.venv)` at the beginning of the command prompt, the environment is active.

---

# 4. Install Dependencies

Upgrade pip:

```cmd
python -m pip install --upgrade pip
```

Install the required packages:

```cmd
pip install phonenumbers requests
```

Verify the phone-number library:

```cmd
python -c "import phonenumbers; print(phonenumbers.__version__)"
```

Example:

```text
9.0.40
```

---

# 5. Phone Number Lookup

Run:

```cmd
python phone_lookup.py
```

The program will ask:

```text
Enter phone number with country code:
```

Enter a number using international format.

Example:

```text
+919876543210
```

The program displays information such as:

```text
=============================================
       PHONE NUMBER OSINT
=============================================
Formatted: +91 98765 43210
Country Code: 91
National Number: 9876543210
Valid: True
Possible: True
Region: India
Carrier: ...
Time Zone: Asia/Calcutta
=============================================
```

## What the results mean

### Valid

Whether the number conforms to the numbering rules and appears to be a valid number.

### Possible

Whether the number has a possible valid structure.

### Region

Numbering metadata associated with the number.

This is **not the phone's current physical location**.

### Carrier

Carrier information available from the underlying numbering metadata.

This may not represent the current carrier because of mobile-number portability.

### Time Zone

Possible time zones associated with the number.

This is not GPS information.

---

# 6. Public Web OSINT

Run:

```cmd
python web_osint.py
```

Enter the number:

```text
+919876543210
```

The program generates search queries for publicly accessible information.

Examples:

```text
"+919876543210"
"+919876543210" business
"+919876543210" company
"+919876543210" contact
"+919876543210" address
"+919876543210" WhatsApp
"+919876543210" Facebook
"+919876543210" Instagram
"+919876543210" LinkedIn
```

The program also generates Google search URLs.

Open the URLs in your browser and review the results manually.

---

# 7. Searching Different Number Formats

A phone number can appear online in different formats.

For example:

```text
+919876543210
```

could appear as:

```text
+91 98765 43210
```

or:

```text
9876543210
```

or:

```text
919876543210
```

Therefore, search multiple representations when conducting OSINT.

Example Google searches:

```text
"+919876543210"
```

```text
"9876543210"
```

```text
"+91 98765 43210"
```

---

# 8. Search Operators

Search engines can be used to narrow public results.

### LinkedIn

```text
"+919876543210" site:linkedin.com
```

### Facebook

```text
"+919876543210" site:facebook.com
```

### Instagram

```text
"+919876543210" site:instagram.com
```

### Business listings

```text
"+919876543210" business
```

```text
"+919876543210" company
```

### Contact information

```text
"+919876543210" contact
```

```text
"+919876543210" address
```

---

# 9. Interpreting Results

A search result should be treated as a **lead**, not automatically as proof that the phone number belongs to a particular person.

For example:

```text
Phone number
     │
     ↓
Public website
     │
     ↓
Name
     │
     ↓
Business
     │
     ↓
Address
```

Each relationship should be independently verified where possible.

Useful corroborating information can include:

- Same phone number
- Same business name
- Same publicly listed address
- Same website
- Same publicly listed email
- Consistent information across multiple independent sources

---

# 10. Limitations

This toolkit cannot determine:

- Live GPS location
- Current physical location
- Cell-tower location
- Private social-media accounts
- Private phone records
- Private messages
- Passwords
- Authentication tokens
- Private databases
- Device contents

A phone number alone does not provide access to these things.

---

# 11. Legal and Ethical Use

Use this toolkit only for legitimate purposes.

Appropriate examples include:

- Investigating your own phone number
- Checking your own public exposure
- Cybersecurity education
- Security research
- OSINT training
- Researching publicly listed businesses
- Verifying publicly published contact information

Do not use it to:

- Stalk or harass people
- Obtain someone's private location
- Bypass authentication
- Access private accounts
- Attempt unauthorized access to devices
- Purchase or use illegally obtained personal data

Publicly available information should still be handled responsibly.

---

# 12. Troubleshooting

## `python` is not recognized

Check:

```cmd
python --version
```

If that fails, try:

```cmd
py --version
```

Python may need to be added to your Windows PATH.

---

## Virtual environment does not activate

From Command Prompt:

```cmd
.venv\Scripts\activate.bat
```

Make sure you are inside the project directory:

```cmd
cd C:\Users\Ajmot\phone-osint
```

---

## `ModuleNotFoundError: No module named 'phonenumbers'`

Make sure the virtual environment is active:

```text
(.venv)
```

Then run:

```cmd
pip install phonenumbers
```

---

## Check installed packages

```cmd
pip list
```

You should see:

```text
phonenumbers
requests
```

---

# 13. Deactivating the Environment

When finished:

```cmd
deactivate
```

The `(.venv)` prefix should disappear.

To use the project again:

```cmd
cd C:\Users\Ajmot\phone-osint
.venv\Scripts\activate.bat
```

---

# 14. Current Project Structure

```text
phone-osint/
│
├── .venv/
│   └── Python virtual environment
│
├── phone_lookup.py
│   └── Phone-number metadata lookup
│
├── web_osint.py
│   └── Public web search query generator
│
└── README.md
    └── Project documentation
```

---

# 15. Quick Start

After the initial setup, the normal workflow is:

```cmd
cd C:\Users\Ajmot\phone-osint
```

```cmd
.venv\Scripts\activate.bat
```

Then:

```cmd
python phone_lookup.py
```

or:

```cmd
python web_osint.py
```

---

## Future Features

Possible future additions include:

- Automated public-search collection
- Structured OSINT reports
- Multiple phone-number format generation
- Public business-directory searches
- Domain/website correlation
- Email correlation
- Breach-exposure checking through authorized services
- JSON/CSV report export
- Evidence/source tracking
- A simple web interface
