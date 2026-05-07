"""Laboratorio 8 - CLI del gestor de tareas."""

# TODO:Implementar CLI según README.md
import sys
from todo_manager import read_todo_file, write_todo_file
 
def main():
 
    if len(sys.argv) < 2:
        print("Insufficient arguments provided!")
        return