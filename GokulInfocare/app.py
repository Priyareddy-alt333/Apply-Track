from datetime import date, datetime, timedelta
import sqlite3
from pathlib import Path
from flask import Flask, render_template, request, redirect, url_for, flash

APP_DIR = Path(__file__).resolve().parent
DB_PATH = APP_DIR / "applications.db"

app = Flask(__name__)
app.secret_key = "change-this-demo-secret-key"

STATUSES = ["Saved", "Applied", "Assessment", "Interview", "Offer", "Rejected"]


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    with get_db() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS applications (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                company TEXT NOT NULL,
                role TEXT NOT NULL,
                applied_on TEXT NOT NULL,
                status TEXT NOT NULL,
                notes TEXT DEFAULT ''
            )
        """)
        count = conn.execute("SELECT COUNT(*) FROM applications").fetchone()[0]
        if count == 0:
            # Demo records make the first launch easy to explore.
            conn.executemany("""
                INSERT INTO applications (company, role, applied_on, status, notes)
                VALUES (?, ?, ?, ?, ?)
            """, [
                ("ABC Technologies", "Junior Java Developer",
                 (date.today() - timedelta(days=10)).isoformat(), "Applied",
                 "Demo record: follow up if no response."),
                ("XYZ Solutions", "Python Trainee",
                 (date.today() - timedelta(days=3)).isoformat(), "Applied",
                 "Demo record: recently applied."),
                ("Tech Company", "AI Automation Associate",
                 (date.today() - timedelta(days=12)).isoformat(), "Interview",
                 "Demo record: interview scheduled.")
            ])


@app.route("/")
def index():
    init_db()
    search = request.args.get("q", "").strip()
    status_filter = request.args.get("status", "").strip()
    query = "SELECT * FROM applications WHERE 1=1"
    params = []
    if search:
        query += " AND (company LIKE ? OR role LIKE ?)"
        params.extend([f"%{search}%", f"%{search}%"])
    if status_filter in STATUSES:
        query += " AND status = ?"
        params.append(status_filter)
    query += " ORDER BY applied_on DESC, id DESC"

    with get_db() as conn:
        applications = conn.execute(query, params).fetchall()

    today = date.today()
    rows = []
    for item in applications:
        record = dict(item)
        try:
            applied_date = date.fromisoformat(record["applied_on"])
            days_waiting = (today - applied_date).days
        except ValueError:
            days_waiting = 0
        record["days_waiting"] = days_waiting
        record["needs_followup"] = (
            record["status"] == "Applied" and days_waiting > 7
        )
        rows.append(record)

    with get_db() as conn:
        total = conn.execute("SELECT COUNT(*) FROM applications").fetchone()[0]
        applied = conn.execute(
            "SELECT COUNT(*) FROM applications WHERE status='Applied'"
        ).fetchone()[0]
        followups = sum(1 for row in rows if row["needs_followup"])

    return render_template(
        "index.html", applications=rows, statuses=STATUSES,
        search=search, status_filter=status_filter, total=total,
        applied=applied, followups=followups
    )


@app.route("/add", methods=["POST"])
def add_application():
    company = request.form.get("company", "").strip()
    role = request.form.get("role", "").strip()
    applied_on = request.form.get("applied_on", "").strip()
    status = request.form.get("status", "Saved").strip()
    notes = request.form.get("notes", "").strip()

    if not company or not role or not applied_on:
        flash("Company, role, and date are required.", "error")
        return redirect(url_for("index"))
    try:
        date.fromisoformat(applied_on)
    except ValueError:
        flash("Please enter a valid date.", "error")
        return redirect(url_for("index"))
    if status not in STATUSES:
        status = "Saved"

    with get_db() as conn:
        conn.execute("""
            INSERT INTO applications (company, role, applied_on, status, notes)
            VALUES (?, ?, ?, ?, ?)
        """, (company, role, applied_on, status, notes))
    flash("Application added successfully.", "success")
    return redirect(url_for("index"))


@app.route("/update/<int:application_id>", methods=["POST"])
def update_status(application_id):
    status = request.form.get("status", "Saved")
    if status not in STATUSES:
        flash("Invalid status selected.", "error")
        return redirect(url_for("index"))
    with get_db() as conn:
        conn.execute(
            "UPDATE applications SET status=? WHERE id=?",
            (status, application_id)
        )
    flash("Status updated.", "success")
    return redirect(url_for("index"))


@app.route("/delete/<int:application_id>", methods=["POST"])
def delete_application(application_id):
    with get_db() as conn:
        conn.execute("DELETE FROM applications WHERE id=?", (application_id,))
    flash("Application deleted.", "success")
    return redirect(url_for("index"))


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
