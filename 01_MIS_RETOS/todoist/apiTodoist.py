from todoist_api_python.api import TodoistAPI

class TodoistManager:
    def __init__(self, token):
        self.api = TodoistAPI(token)
    
    def add_task(self, content, due_date="today", priority=3):
        try:
            task = self.api.add_task(
                content=content,
                due_string=due_date,
                priority=priority
            )
            return task
        except Exception as error:
            return f"Error al añadir la tarea: {error}"

    def get_task(self, task_id):
        try:
            task = self.api.get_task(task_id)
            return task
        except Exception as error:
            return f"Error al obtener la tarea: {error}"

    def update_task(self, task_id, **kwargs):
        try:
            result = self.api.update_task(task_id=task_id, **kwargs)
            return result
        except Exception as error:
            return f"Error al actualizar la tarea: {error}"

    def delete_task(self, task_id):
        try:
            result = self.api.delete_task(task_id)
            return result
        except Exception as error:
            return f"Error al eliminar la tarea: {error}"
    
    def format_task(self, task):
        # Define el mensaje de fecha de vencimiento con un condicional para mostrar una fecha o indicar que no tiene.
        due_info = f"Due: {task.due.date} {task.due.string}" if task.due else "Due: No due date"
        
        # Formatea la salida con negrita y colores para cada parte de la tarea.
        return (
            f"\033[1;34mTask ID:\033[0m {task.id}\n"                   # Azul y negrita para el ID.
            f"\033[1;36mContent:\033[0m {task.content}\n"              # Cian y negrita para el contenido.
            f"\033[1;33mDue Info:\033[0m {due_info}\n"                 # Amarillo y negrita para la información de vencimiento.
            f"\033[1;35mPriority:\033[0m {task.priority}\n"            # Magenta y negrita para la prioridad.
            "\033[94m----------------------------------------\033[0m"  # Azul claro para la línea separadora.
        )


    def get_all_tasks(self):
        try:
            tasks = self.api.get_tasks()
            formatted_tasks = [self.format_task(task) for task in tasks]
            return "\n".join(formatted_tasks)
        except Exception as error:
            return f"Error al obtener todas las tareas: {error}"


# Crear una instancia del manejador de Todoist
todoist_manager = TodoistManager("0627aee48c870765d1a2d8f82a195aaa40aa268c")

# # Añadir una tarea
# new_task = todoist_manager.add_task("Test de Tarea", "today", 3)
# print("Tarea añadida:", new_task)

# # Obtener una tarea específica
# task_info = todoist_manager.get_task(task_id="123456789")
# print("Información de la tarea:", task_info)

# # Actualizar una tarea
# update_info = todoist_manager.update_task("123456789", content="Actualizar contenido de la tarea")
# print("Resultado de la actualización:", update_info)

# # Eliminar una tarea
# delete_result = todoist_manager.delete_task("123456789")
# print("Resultado de eliminación:", delete_result)


# Obtener todas las tareas
import os
os.system("clear")
all_tasks = todoist_manager.get_all_tasks()
print(f"Lista de todas las tareas:\n \n{all_tasks}")