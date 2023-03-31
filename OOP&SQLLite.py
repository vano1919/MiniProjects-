import datetime
import sqlite3


class Database:

    def __init__(self):
        self.connection = sqlite3.connect('todoVT.db')
        self.cursor = self.connection.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS To_Do
                         (id INTEGER PRIMARY KEY, text TEXT, deadline TEXT, date TEXT)''')
        self.connection.commit()

    def add_db(self, todo):
        self.cursor.execute("INSERT INTO To_Do (text, deadline, date) VALUES (?, ?, ?)",
                       (todo.text, todo.deadline, todo.date))
        self.connection.commit()
        print("\nToDo Added!")

    def edit_db(self, old_todo_id, new_todo):
        self.cursor.execute("UPDATE To_Do SET text = ?, deadline = ?, date = ? WHERE id = ?",
                       (new_todo.text, new_todo.deadline, new_todo.date, old_todo_id))
        self.connection.commit()
        print("\nToDo edited!")

    def delete_db(self, todo_id):
        self.cursor.execute("DELETE FROM To_Do WHERE id = ?", (todo_id,))
        self.connection.commit()
        print("\nToDo deleted!")

    def get_all(self):
        self.cursor.execute("SELECT * FROM To_Do")
        rows = self.cursor.fetchall()
        entries = []
        for row in rows:
            todo = Todo(row[1], row[2])
            todo.date = datetime.datetime.strptime(row[3], '%Y-%m-%d %H:%M:%S.%f')
            todo.id = row[0]
            entries.append(todo)
        return entries


class Manager:

    def __init__(self, database):
        self.database = database

    def add(self, todo):
        self.database.add_db(todo)

    def check_data(self):
        return len(self.database.get_all())

    def edit(self, old_todo_id, new_todo):
        self.database.edit_db(old_todo_id, new_todo)

    def delete(self, todo_id):
        self.database.delete_db(todo_id)

    def show_all(self):
        entries = self.database.get_all()

        for index, item in enumerate(entries, 1):
            print(f"{'-' * 25}{index}{'-' * 25}")
            print(item)
            print('-' * 51)


class Todo:

    def __init__(self, text, deadline):
        self.id = None
        self.text = text
        self.deadline = deadline
        self.date = datetime.datetime.now()

    def __str__(self):
        return f"Date: {self.date.strftime('%d/%m%Y %H:%M')}\nToDo: {self.text}\nDeadLine: {self.deadline}"


def menu():
    choice = None
    database = Database()
    manager = Manager(database)

    while choice != "q":
        print("\nToDo App Menu:")
        print("a. Add")
        print("e. Edit")
        print("d. Delete")
        print("s. Show All")
        print("q. Quit")

        choice = input("\nAction: ").lower()

        if choice == "a":
            print("Enter 'q' for Main Menu")
            text = input("To_Do: ")
            if text == "q":
                continue
            deadline = input("Enter Deadline (any format): ")
            if deadline == "q":
                continue
            todo = Todo(text, deadline)
            manager.add(todo)

        elif choice == "e":
            print("Enter 'q' for Main Menu")

            while True:
                if manager.check_data() == 0:
                    print("\nNothing Here")
                    break
                else:
                    try:
                        manager.show_all()
                        old_todo_index = input("Choose the index: ")
                        if old_todo_index == "q":
                            break
                        old_todo_index = int(old_todo_index) - 1
                        text = input("Text for new ToDo: ")
                        if text == "q":
                            break
                        deadline = input("Enter DeadLine (any format): ")
                        if deadline == "q":
                            break
                        entries = manager.database.get_all()
                        old_todo = entries[old_todo_index]
                        if not text:
                            text = old_todo.text
                        if not deadline:
                            deadline = old_todo.deadline
                        new_todo = Todo(text, deadline)
                        manager.edit(old_todo.id, new_todo)
                        break
                    except:
                        print("\nTry correct index\n")
        elif choice == "d":
            print("Enter 'q' for Main Menu")
            while True:
                entries = manager.database.get_all()
                if len(entries) == 0:
                    print("\nNothing Here")
                    break
                else:
                    try:
                        manager.show_all()
                        todo_index = input("Choose the index of the ToDo item to delete: ")
                        if todo_index == "q":
                            break
                        todo_index = int(todo_index) - 1
                        if todo_index < 0 or todo_index >= len(entries):
                            print("\nInvalid index. Please try again.\n")
                            continue
                        todo_id = entries[todo_index].id
                        manager.delete(todo_id)
                        break
                    except ValueError:
                        print("\nInvalid input. Please enter a valid index.\n")


        elif choice == "s":
            if manager.check_data() == 0:
                print("\nNothing Here")
            else:
                manager.show_all()

        elif choice == "q":
            print("Bye")

        else:
            print("Invalid choice, please try again.")
menu()