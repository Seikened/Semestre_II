# Importar pymongo e inicializar el cliente
from pymongo import MongoClient

# Reemplaza con tu cadena de conexión
MONGO_URI = 'mongodb+srv://seiken:fer213142@cluster0.va3sdo5.mongodb.net/miapp?retryWrites=true&w=majority'

# Conectar a MongoDB usando el URI
cliente = MongoClient(MONGO_URI)

# Seleccionar la base de datos
base_datos = cliente['miapp']

# Seleccionar la colección (equivalente a una tabla)
coleccion = base_datos['users']  # Asegúrate de que coincide con tu colección real

# Insertar varios documentos (crear múltiples usuarios)
usuarios = [
   {'name': 'Fernando', 'lastname': 'León', 'email': 'fernando@example.com'},
   {'name': 'María', 'lastname': 'Pérez', 'email': 'maria.perez@example.com'},
   {'name': 'Luis', 'lastname': 'García', 'email': 'luis.garcia@example.com'}
]
resultados = coleccion.insert_many(usuarios)
print(f'IDs de los nuevos usuarios insertados: {resultados.inserted_ids}')

# Obtener un documento por ID
user_id = resultados.inserted_ids[0]
user = coleccion.find_one({'_id': user_id})
print(f'Usuario encontrado: {user}')

# Filtrar usuarios por apellido
usuarios_filtrados = coleccion.find({'lastname': 'León'})
print('Usuarios con el apellido León:')
for usuario in usuarios_filtrados:
   print(usuario)

# Actualizar un documento
coleccion.update_one(
   {'_id': user_id},
   {'$set': {'email': 'nuevo_email@example.com'}}
)
user_actualizado = coleccion.find_one({'_id': user_id})
print(f'Usuario actualizado: {user_actualizado}')

# Eliminar un documento por ID
coleccion.delete_one({'_id': user_id})
print(f'Usuario eliminado con ID: {user_id}')