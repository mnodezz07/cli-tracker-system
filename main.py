
import argparse
from tabulate import tabulate

from utils.storage import load_data, save_data


def add_user(args):
    data = load_data()

    user = {
        "id": len(data["users"]) + 1,
        "name": args.name,
        "email": args.email
    }

    data["users"].append(user)
    save_data(data)

    print("User added successfully!")


def list_users(args):
    data = load_data()

    if not data["users"]:
        print("No users found.")
        return

    print(tabulate(
        data["users"],
        headers="keys",
        tablefmt="grid"
    ))


def add_project(args):
    data = load_data()

    project = {
        "id": len(data["projects"]) + 1,
        "title": args.title,
        "description": args.description,
        "due_date": args.due_date
    }

    data["projects"].append(project)
    save_data(data)

    print("Project added successfully!")


def list_projects(args):
    data = load_data()

    if not data["projects"]:
        print("No projects found.")
        return

    print(tabulate(
        data["projects"],
        headers="keys",
        tablefmt="grid"
    ))


def add_task(args):
    data = load_data()

    task = {
        "id": len(data["tasks"]) + 1,
        "title": args.title,
        "status": "Pending",
        "assigned_to": args.assigned_to,
        "project_id": args.project_id
    }

    data["tasks"].append(task)
    save_data(data)

    print("Task added successfully!")


def list_tasks(args):
    data = load_data()

    if not data["tasks"]:
        print("No tasks found.")
        return

    print(tabulate(
        data["tasks"],
        headers="keys",
        tablefmt="grid"
    ))


def complete_task(args):
    data = load_data()

    for task in data["tasks"]:
        if task["id"] == args.id:
            task["status"] = "Complete"
            save_data(data)
            print("Task marked as complete!")
            return

    print("Task not found.")


def edit_project(args):
    data = load_data()

    for project in data["projects"]:
        if project["id"] == args.id:
            project["title"] = args.title
            project["description"] = args.description
            project["due_date"] = args.due_date

            save_data(data)
            print("Project updated successfully!")
            return

    print("Project not found.")


def edit_task(args):
    data = load_data()

    for task in data["tasks"]:
        if task["id"] == args.id:
            task["title"] = args.title
            task["assigned_to"] = args.assigned_to

            save_data(data)
            print("Task updated successfully!")
            return

    print("Task not found.")


def main():
    parser = argparse.ArgumentParser(
        description="CLI Project Management Tool"
    )

    commands = parser.add_subparsers(
        dest="command",
        required=True
    )

    # Add user
    add_user_parser = commands.add_parser("add-user")
    add_user_parser.add_argument("--name", required=True)
    add_user_parser.add_argument("--email", required=True)
    add_user_parser.set_defaults(func=add_user)

    # List users
    list_users_parser = commands.add_parser("list-users")
    list_users_parser.set_defaults(func=list_users)

    # Add project
    add_project_parser = commands.add_parser("add-project")
    add_project_parser.add_argument("--title", required=True)
    add_project_parser.add_argument("--description", required=True)
    add_project_parser.add_argument("--due-date", required=True)
    add_project_parser.set_defaults(func=add_project)

    # List projects
    list_projects_parser = commands.add_parser("list-projects")
    list_projects_parser.set_defaults(func=list_projects)

    # Add task
    add_task_parser = commands.add_parser("add-task")
    add_task_parser.add_argument("--title", required=True)
    add_task_parser.add_argument("--assigned-to", required=True)
    add_task_parser.add_argument("--project-id", type=int, required=True)
    add_task_parser.set_defaults(func=add_task)

    # List tasks
    list_tasks_parser = commands.add_parser("list-tasks")
    list_tasks_parser.set_defaults(func=list_tasks)

    # Complete task
    complete_parser = commands.add_parser("complete-task")
    complete_parser.add_argument("--id", type=int, required=True)
    complete_parser.set_defaults(func=complete_task)

    # Edit project
    edit_project_parser = commands.add_parser("edit-project")
    edit_project_parser.add_argument("--id", type=int, required=True)
    edit_project_parser.add_argument("--title", required=True)
    edit_project_parser.add_argument("--description", required=True)
    edit_project_parser.add_argument("--due-date", required=True)
    edit_project_parser.set_defaults(func=edit_project)

    # Edit task
    edit_task_parser = commands.add_parser("edit-task")
    edit_task_parser.add_argument("--id", type=int, required=True)
    edit_task_parser.add_argument("--title", required=True)
    edit_task_parser.add_argument("--assigned-to", required=True)
    edit_task_parser.set_defaults(func=edit_task)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
