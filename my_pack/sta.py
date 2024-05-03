import sys

def add_task(tasks): #user defined function to perform add task
    try:
        n_tasks = int(input("How many tasks do you want to add: "))
        for _ in range(n_tasks):
            task = input("Enter the task: ")
            description = input("Enter task description: ")
            assigned_to = input("Assign task to: ")
            roll_number = int(input("Enter the roll number: "))
            due_date = input("Enter the due date (YYYY-MM-DD): ")
            tasks.append({
                "roll_number": roll_number,
                "task": task,
                "assigned_to": assigned_to,
                "description": description,
                "due_date": due_date,
                "done": False
            })
            print("Task added!")
    except Exception as e:
        print(sys.exc_info()[0],sys.exc_info()[1])

def view_tasks(tasks): #user defined function to view task
    print("\nTasks:")
    try:
        for index, task in enumerate(tasks, start=1):
            status = "Done" if task["done"] else "Not Done"
            print(f"{index}. Task: {task['task']}")
            print(f"   Description: {task['description']}")
            print(f"   Assigned to: {task['assigned_to']}")
            print(f"   Roll Number: {task['roll_number']}")
            print(f"   Due date: {task['due_date']}")
            print(f"   Status: {status}\n")
    except Exception as e:
        print(sys.exc_info()[0],sys.exc_info()[1])

def remove_task(tasks): #user defined function to remove task
    try:
        for task in tasks:
            task_name = input("Enter the task name to remove: ")
            if task["task"].lower() == task_name.lower():
                tasks.remove(task)
                print(f"Task '{task_name}' removed!")
                return True
        print(f"No task with the name '{task_name}' found.")
        return False
    except Exception as e:
        print(sys.exc_info()[0],sys.exc_info()[1])

def edit_task(tasks): #user defined function to edit task
    try:
        for task in tasks:
            task_name = input("Enter the task name to edit: ")
            if task["task"].lower() == task_name.lower():
                task["task"] = input("Enter the new task name: ")
                task["description"] = input("Enter the new task description: ")
                task["assigned_to"] = input("Assign task to: ")
                task["roll_number"] = int(input("Enter the new roll number: "))
                task["due_date"] = input("Enter the new due date (YYYY-MM-DD): ")
                print(f"Task '{task_name}' updated!")
                return True
        print(f"No task with the name '{task_name}' found.")
        return False
    except Exception as e:
        print(sys.exc_info()[0],sys.exc_info()[1])

from datetime import datetime

def set_reminder(tasks): #user defined function to set remainder to a task
     for task in tasks:
         task_name = input("Enter the task name to set_reminder: ")
         if task["task"].lower() == task_name.lower():
             date_str = input("Enter the reminder date (YYYY-MM-DD): ")
             time_str = input("Enter the reminder time (HH:MM AM/PM): ")
             
             try:
                 reminder_datetime = datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %I:%M %p")
                 print(f"Reminder set for task '{task_name}' on {reminder_datetime}.")
                 return True
             except ValueError:
                 print("Invalid date or time format. Please use YYYY-MM-DD and HH:MM AM/PM.")
                 return False

     print(f"No task with the name '{task_name}' found.")
     return False

def clear_all_tasks(tasks): #user defined function to clear all task
    try:
        tasks.clear()
        print("All tasks cleared!")
    except Exception as e:
        print(sys.exc_info()[0],sys.exc_info()[1])
        
def mark_task_done(tasks): #user defined function to perform mark task as done
    try:
        keyword = input("Enter a roll_number or assigned to: ").lower()
    
        found_task = None
        for index, task in enumerate(tasks, start=1):
            if (keyword in str(task["roll_number"]) or 
                keyword in task["assigned_to"].lower()):
                found_task = task
                break

        if found_task:
            found_task["done"] = True
            found_task["complete_date"] = input("Enter the completion date (YYYY-MM-DD): ")
            print("Task marked as done!")
        else:
            print("Task not found. Please check the roll number and assigned team member.")
    except Exception as e:
        print(sys.exc_info()[0],sys.exc_info()[1])

def search_tasks(tasks): #user defined function to perform search & filter task
    try:
        keyword = input("Enter a task or due_date or assigned to or roll_number: ").lower()
        filtered_tasks = []
    
        for index, task in enumerate(tasks, start=1):
            if (keyword in str(task["roll_number"]) or 
                keyword in task["task"].lower() or
                keyword in task["due_date"].lower() or
                keyword in task["assigned_to"].lower()):
                filtered_tasks.append(task)
    
        if filtered_tasks:
            print("Matching tasks:")
            for index, task in enumerate(filtered_tasks, start=1):
                print(f"{index}. {task['task']} (Assigned to: {task['assigned_to']}, "
                      f"roll_number: {task['roll_number']}, Due: {task['due_date']}, done: {task['done']})")
        else:
            print("No matching tasks found.")
    except Exception as e:
        print(sys.exc_info()[0],sys.exc_info()[1])

import csv

def export_csv(tasks): #user defined function to export task
    try:
        with open("tasks_exported.csv", "w", newline="") as csvfile:
            fieldnames = ["roll_number", "assigned_to", "task", "description", "due_date", "done", "complete_date"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(tasks)
        print("Tasks exported to tasks_exported.csv")
    except Exception as e:
        print(sys.exc_info()[0],sys.exc_info()[1])
