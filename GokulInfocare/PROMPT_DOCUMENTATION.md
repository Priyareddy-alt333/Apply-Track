# Prompt Documentation — ApplyTrack

**Project:** ApplyTrack — Job Application Tracker  
**Domain:** Technology / productivity automation  
**AI tool:** ChatGPT  
**Purpose:** Document the prompts used to plan, develop, and test the project. This file is a template: keep only the prompts you actually used and add your own revisions after testing.

## Prompt 1 — Choose a beginner-sized project
> I am a beginner learning Python and applying for an AI Growth and Automation Associate role. Suggest a practical technology project I can build and explain honestly. It should solve a real problem, be small enough to complete, and demonstrate automation and problem-solving.

**Goal:** Select a useful project rather than submitting only an idea.

## Prompt 2 — Define requirements
> Help me design a beginner-friendly job application tracker. Requirements: add company, job role, application date, status and notes; search applications; filter by status; update status; delete records; and flag applications marked Applied when more than seven days have passed. Explain the simplest suitable architecture and the limitations.

**Goal:** Convert the idea into clear functional requirements.

## Prompt 3 — Generate a Python prototype
> Create a small Python Flask web app for the requirements above. Use SQLite for storage, validate required fields and dates, use parameterized SQL queries, and provide readable code and simple HTML/CSS. Include sample fictional records so I can demonstrate the follow-up rule. Explain each file and avoid unnecessary frameworks.

**Goal:** Build a working prototype with a small technology stack.

## Prompt 4 — Review correctness and safety
> Review the code for likely errors. Check that user input is validated, SQL statements use parameters, only allowed status values are accepted, and follow-up reminders are shown only when status is Applied and the date is more than seven days old. Explain any limitations and how I can test each behavior manually.

**Goal:** Ask for review, then verify the result by running the app and testing it.

## Prompt 5 — Improve usability
> Suggest simple usability improvements without making this beginner project unnecessarily complex. Include clear labels, readable layout, search/filter controls, success/error messages, and a mobile-friendly layout.

**Goal:** Improve clarity and ease of demonstration.

## Iteration log — complete after you test
Record what actually happened. Do not claim a test passed until you run it.

| Test | Expected result | Actual result |
|---|---|---|
| Add application with all required fields | Record appears in list | Fill in after testing |
| Submit without company or role | Validation message appears | Fill in after testing |
| Applied date is 10 days ago and status is Applied | Follow-up flag appears | Fill in after testing |
| Change status to Interview | Follow-up flag disappears | Fill in after testing |
| Search by company | Matching records only | Fill in after testing |
| Filter by status | Matching status only | Fill in after testing |

## How I used AI
Draft this in your own words after completing the work. A truthful example, if accurate, is:

"I used ChatGPT to help break the project into requirements, generate an initial Flask/SQLite implementation, explain unfamiliar code, and suggest test cases. I reviewed the output and ran manual tests, then documented the results. AI-generated code can contain errors, so I treated the output as a draft and checked the behavior."

**Important:** Do not submit this as a record of work until you have actually used the prompts, run the app, and completed the iteration log. Keep the prompt history aligned with what you really did.
