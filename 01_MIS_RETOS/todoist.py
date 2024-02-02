import datetime

# Clase para gestionar las tareas
class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, due_date=None):
        task = {'description': description, 'due_date': due_date, 'completed': False}
        self.tasks.append(task)
        print(f"Task added: {description}")

    def list_tasks(self):
        for i, task in enumerate(self.tasks, start=1):
            status = "Done" if task['completed'] else "Pending"
            print(f"{i}. {task['description']} - {status} - Due: {task['due_date']}")

# Instancia del gestor de tareas
manager = TaskManager()

# Añadir algunas tareas
manager.add_task("Revisar la asignación de IA", datetime.datetime(2024, 1, 31))
manager.add_task("Jugar una ronda de Halo")

# Listar tareas
manager.list_tasks()
