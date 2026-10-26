import sys

from rich.console import Console

from taskr.storage import add_task, load_tasks

console = Console()


def list_tasks():
    for i, task in enumerate(load_tasks(), 1):
        mark = "x" if task["done"] else " "
        console.print(f"[{mark}] {i}. {task['title']}")


def main():
    if len(sys.argv) > 2 and sys.argv[1] == "add":
        add_task(" ".join(sys.argv[2:]))
    else:
        list_tasks()


if __name__ == "__main__":
    main()
