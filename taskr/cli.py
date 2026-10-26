import sys
import pendulum

from rich.console import Console

from taskr.storage import add_task, load_tasks, sort_by_priority

console = Console()


def list_tasks():
    tasks = sort_by_priority(load_tasks())
    for i, task in enumerate(tasks, 1):
        mark = "x" if task["done"] else " "
        due = format_due_date(task)
        console.print(f"[{mark}] {i}. {task['title']} {due}")


def main():
    if len(sys.argv) > 2 and sys.argv[1] == "add":
        add_task(" ".join(sys.argv[2:]))
    else:
        list_tasks()


if __name__ == "__main__":
    main()
