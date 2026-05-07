"""Laboratorio 8 - CLI del gestor de tareas."""

TODO:Implementar CLI según README.md
import sys
from todo_manager import read_todo_file, write_todo_file

def main():
 
    if len(sys.argv) < 2:
        print("Insufficient arguments provided!")
        return
     
 
    if sys.argv[1] == "--help":
        print("""Usage: python main.py <file_path> <command> [arguments]...
Commands:
  add "task"    - Add a task to the list.
  remove "task" - Remove a task from the list.
  view          - Display all tasks.
Examples:
  python main.py tasks.txt add "Buy groceries"
  python main.py tasks.txt remove "Do laundry"
  python main.py tasks.txt view
  python main.py tasks.txt add "Call mom" remove "Take out trash" view""")
        return
        file_path = sys.argv[1]
   
try:
       
        tasks = read_todo_file(file_path)
       
       
        i = 2
        while i < len(sys.argv):
            command = sys.argv[i]
           
            if command == "view":
                print("Tasks:")
                for task in tasks:
                    print(task)
                i += 1
               
            elif command == "add":
                if i + 1 >= len(sys.argv):
                    raise IndexError('Task description required for "add".')
                new_task = sys.argv[i+1]
                tasks.append(new_task)
                print(f'Task "{new_task}" added.')
                i += 2