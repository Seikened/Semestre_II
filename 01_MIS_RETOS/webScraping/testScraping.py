# import aiohttp
# import asyncio
# from bs4 import BeautifulSoup  # Asegúrate de tener instalado BeautifulSoup

# async def login(url, username, password):
#     async with aiohttp.ClientSession() as session:
#         login_url = url
#         login_data = {
#             'username': username,
#             'password': password
#             # Asegúrate de incluir otros campos necesarios que el formulario de inicio de sesión requiera.
#         }
#         # Dentro de tu función 'login', después de enviar la solicitud POST:
#         response_text = await response.text()
#         print(response_text)  # Esto imprimirá el HTML de la respuesta

#         async with session.post(login_url, data=login_data) as response:
#             # Convertimos la respuesta en texto
#             response_text = await response.text()

#             # Usamos BeautifulSoup para analizar el HTML
#             soup = BeautifulSoup(response_text, 'html.parser')

#             # Aquí debes buscar elementos específicos que indiquen un inicio de sesión exitoso.
#             # Por ejemplo, buscar un elemento que contenga un mensaje de bienvenida:
#             # welcome_message = soup.find(...)  # Ajusta esto según el sitio web
            

#             # O verificar si te redirigieron a una página específica:
#             if response.url == 'https://cursos.iberoleon.mx/online/':
#                 print("Inicio de sesión exitoso")
#             else:
#                 print("Inicio de sesión fallido o se requieren más pasos")


# url = 'https://cursos.iberoleon.mx/online/login/index.php'

# asyncio.run(login(url, username, password))

# username = '192488-7@iberoleon.edu.mx'
# password = 'Ftry2131'


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Opciones de Chrome
chrome_options = Options()
# chrome_options.add_argument("--headless")  # Ejecutar Chrome en modo sin cabeza (sin interfaz gráfica)

# Servicio de Chrome
chrome_service = Service(executable_path='C:\\Users\\ferna\\OneDrive\\Documentos\\Semestre_II\\01_MIS_RETOS\\webScraping\\chromedriver.exe')

# Inicializar el WebDriver con las opciones y el servicio de Chrome
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

# Abre la página de inicio de sesión
driver.get('https://cursos.iberoleon.mx/online/login/index.php')

# Tus credenciales
username = '192488-7'
password =                                                                                                                                      'Ftry2131*'

# Encuentra los campos del formulario y los rellena con tus credenciales
driver.find_element(By.NAME, 'username').send_keys(username)
driver.find_element(By.NAME, 'password').send_keys(password)

# Espera explícita hasta que el botón de inicio de sesión sea clickeable y luego hacer clic en él
login_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "loginbtn"))
)
login_button.click()
input("Presiona Enter para cerrar el navegador...")

# Cierra el navegador después de presionar Enter
driver.quit()