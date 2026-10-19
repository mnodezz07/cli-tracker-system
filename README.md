# CLI Project Management Tool

## Description
A command-line application built with Python to manage users, projects, and tasks. It uses JSON to store data.

## Features
- Add and list users
- Add and list projects
- Add and list tasks
- Mark tasks as complete
- Edit projects and tasks
- Save data in a JSON file

## Technologies
- Python
- Object-Oriented Programming (OOP)
- Argparse
- JSON
- Tabulate

## Installation

Clone the repository and enter the project folder:

```bash
git clone https://github.com/mnodezz07/cli-tracker-system.git
cd cli-tracker-system
```

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

## Usage

Add a user:

```bash
python main.py add-user --name "Denis" --email "denis@example.com"
```

List users:

```bash
python main.py list-users
```

Add a project:

```bash
python main.py add-project --title "Website" --description "Build a website" --due-date "2026-12-31"
```

List projects:

```bash
python main.py list-projects
```

Add a task:

```bash
python main.py add-task --title "Build homepage" --assigned-to "Denis" --project-id 1
```

List tasks:

```bash
python main.py list-tasks
```

Complete a task:

```bash
python main.py complete-task --id 1
```

## Data Storage
Application data is stored in `data/database.json`.

