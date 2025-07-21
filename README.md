# Job Autofill Tool

Quickly fill out job applications with hotkeys and track them in Google Sheets.

## Features

✅ Autofill names, contact info, and experience bullets  
✅ Use keyboard hotkeys (e.g., `f`, `l`, `1`, etc.)  
✅ Google Sheets logging for applications

---

## Setup

1. Clone the repo and create a virtual environment:

```bash
git clone https://github.com/yourusername/job-autofill-tool.git
cd job-autofill-tool
python -m venv venv
source venv/bin/activate  # or .\venv\Scripts\activate on Windows
jobhunttools
```

2.Install dependencies:

```bash
pip install -r requirements.txt
```

3.Place your OAuth creds.json in data/, and optionally fill out autofill.json.

## 🔧 Sample `autofill.json` Format

Create a file at `data/autofill.json` and populate it with your personalized values. These will be triggered by keyboard shortcuts (e.g. `f` for first name, `1` for experience bullet 1).

```json
{
  "f": "First Name",
  "l": "Last Name",
  "e": "email@example.com",
  "n": "123-456-7890",
  "a": "1234 Address St, City, State",
  "s": "Your School Name",
  "k": "https://linkedin.com/in/yourprofile",
  "1": "● Experience bullet 1...",
  "2": "● Experience bullet 2...",
  "i": "This is my general interest statement for applications."
}