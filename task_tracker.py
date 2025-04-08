import argparse
import os
os.system("cls" if os.name == "nt" else "clear")
# TASK TRACKER APPLICATION as simple command line interface (CLI)

import json
import random

import datetime

import uuid



TASKS_FILE = "new_tasks.json"
def load_tasks_file():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []


def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)



def add_new_task(topic, description):
    tasks = load_tasks_file()
    task_id = str(uuid.uuid4())
    created_at = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    updated_at = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    task = {
        "id": task_id,
        "topic": topic,
        "description": description,
        "status": "todo",
        "createdAt": created_at,
        "updated_at": updated_at,
    }

    tasks.append(task)
    save_tasks(tasks)
    print(f"Task: : {task['topic']} successfully added.".title())


def update_task_status(task_id, new_status):
    tasks = load_tasks_file()
    
    task_found = False
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = new_status
            task["updated_at"] = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            save_tasks(tasks)
            task_found = True
            print(f"Task updated: {task['topic']}".title())
    if not task_found:
        print("task is not found".upper()) 
    

def update_task_descrption(task_id, new_description):
    tasks = load_tasks_file()
    
    task_found = False
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = new_description
            task["updated_at"] = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            save_tasks(tasks)
            task_found = True
            print(f"Task updated: {task['topic']}".title())
    if not task_found:
        print("task is not found".upper())
    

def delete_task_object(task_id):
    tasks = load_tasks_file()
    tasks = [task for task in tasks if task["id"] != task_id]
    save_tasks(tasks)
    return f"Task {task_id} deleted.".upper()


def list_tasks(filter_status = None):
    tasks = load_tasks_file()
    if filter_status:
        tasks = [task for task in tasks if task["status"] == filter_status]
    for task in tasks:
        print(task)



def main():
    parser = argparse.ArgumentParser(description="Task Tracker Command-Line-Interface")
    subparsers = parser.add_subparsers(dest = "command")

    add_parser = subparsers.add_parser("add", help="Add a task")
    add_parser.add_argument("topic", type = str, help = "Define a topic for your task")
    add_parser.add_argument("description", type = str, help = "Description of the task")

    update_parser = subparsers.add_parser("update_status", help="Update a task's status")
    update_parser.add_argument("task_id", type = str, help="ID of the task")
    update_parser.add_argument("new_status", type = str, help="New status of the task (todo, in-progress, done)")

    update_parser = subparsers.add_parser("update_descrption", help="Update a task's description")
    update_parser.add_argument("task_id", type = str, help="ID of the task")
    update_parser.add_argument("new_description", type = str, help="New description for the task")


    delete_parser = subparsers.add_parser("delete_task", help = "Delete a task")
    delete_parser.add_argument("task_id", type = str, help = "ID of the task")

    list_parser = subparsers.add_parser("list", help="List the tasks")
    list_parser.add_argument("filter_status", type = str, help = "Filter by status (todo, in-progress, done)")

    args = parser.parse_args()

    if args.command == "add":
        add_new_task(args.topic, args.description)
    elif args.command == "update_status":
        update_task_status(args.task_id, args.new_status)
    elif args.command == "update_descrption":
        update_task_descrption(args.task_id, args.new_description)
    elif args.command == "delete_task":
        delete_task_object(args.task_id)
    elif args.command == "list":
        list_tasks(args.filter_status)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
