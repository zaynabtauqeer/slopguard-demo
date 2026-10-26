import json
from pathlib import Path

DB = Path.home() / ".taskr.json"


def load_tasks():
    if not DB.exists():
        return []
    return json.loads(DB.read_text())


def save_tasks(tasks):
    DB.write_text(json.dumps(tasks, indent=2))


def add_task(title, due=None):
    tasks = load_tasks()
    tasks.append({"title": title, "due": due, "done": False})
    save_tasks(tasks)
