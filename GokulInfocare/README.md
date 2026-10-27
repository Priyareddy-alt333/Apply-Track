# ApplyTrack — AI-assisted Job Application Tracker

## What it does
- Adds job applications with company, role, date, status, and notes.
- Saves data locally in a SQLite database (`applications.db`).
- Searches by company or role and filters by status.
- Highlights applications whose status is **Applied** and whose application date is more than 7 days ago.
- Lets the user update a status or delete a record.
- Includes sample records on first launch so the follow-up feature can be demonstrated immediately.

## Requirements
- Python 3.10 or newer
- Internet access only to install Flask the first time

## Run locally (Windows)
1. Install Python from https://www.python.org/downloads/ and enable **Add Python to PATH**.
2. Extract this ZIP to a folder.
3. Open Command Prompt in the `AI_Job_Application_Tracker` folder.
4. Run:
   ```bash
   py -m venv .venv
   .venv\Scripts\activate
   pip install -r requirements.txt
   py app.py
   ```
5. Open http://127.0.0.1:5000 in your browser.
6. To stop the app, return to Command Prompt and press `Ctrl+C`.

If `py` does not work, try `python` instead.

## Demo checklist
1. Show the three example applications.
2. Point out the application that has been waiting more than seven days and is still marked Applied.
3. Add a test application with an older date and status Applied; confirm it is flagged.
4. Change its status to Interview; confirm it is no longer flagged for follow-up.
5. Search by company and filter by status.
6. Explain that the data is saved in SQLite on your own computer.

## Important
- The sample company names are fictional demo data.
- The app is a learning prototype, not a production service.
- Do not enter sensitive personal data.
- Review and test the code before presenting it. Be ready to explain the code in your own words.
- The app is not yet deployed online. You can submit the project folder via a Google Drive folder, or publish it to GitHub if you know how.
