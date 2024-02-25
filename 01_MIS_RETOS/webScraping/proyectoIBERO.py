from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options



#========================= FUNCIONES =========================#

# Parte 1: Configuración inicial y acceso a la página
def configurar_navegador(chrome_driver_path, link_visit):
    chrome_options = Options()
    # chrome_options.add_argument("--headless")  # Descomenta para ejecutar en modo sin cabeza
    chrome_service = Service(executable_path=chrome_driver_path)
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
    driver.get(link_visit)
    return driver


def iniciar_sesion(username, password):
    driver.find_element(By.NAME, 'username').send_keys(username)
    driver.find_element(By.NAME, 'password').send_keys(password)
    login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "loginbtn")))
    login_button.click()

def entregar_tarea(evento, pie_evento):
    if "Añadir envío" in pie_evento:
        enlace_envio = evento.find_element(By.CSS_SELECTOR, 'a.card-link')
        enlace_envio.click()

def evento_proximo(eventos_proximos):
    for evento in eventos_proximos:
        titulo_evento = evento.find_element(By.CSS_SELECTOR, '.card-header').text
        descripcion_evento = evento.find_element(By.CSS_SELECTOR, '.card-body').text
        pie_evento = evento.find_element(By.CSS_SELECTOR, '.card-footer').text
    return titulo_evento, descripcion_evento, pie_evento



#========================= FIN DE FUNCIONES =========================#


#==================================== PARTE 1 ====================================#
path_chrome_drive = r"C:\\Users\\ferna\\OneDrive\\Documentos\\Semestre_II\\01_MIS_RETOS\\webScraping\\chromedriver.exe"
url = 'https://cursos.iberoleon.mx/online/login/index.php'

# Parte 1: Prepar el navegador y nuestra ruta
driver = configurar_navegador(path_chrome_drive, url)
#==================================== FIN DE PARTE 1 ====================================#



#==================================== PARTE 2 ====================================#
# Parte 2: Inicio de sesión
username = '192488-7'
password =  'Ftry2131*'#input("Introduce tu contraseña: ")
iniciar_sesion(username, password)
ruta_archivo = r"C:\Users\ferna\OneDrive\Documentos\Semestre_II\01_MIS_RETOS\webScraping\materias\analisisDatos\Investigación sobre Logaritmos y Antilogaritmos.pdf"
#==================================== FIN DE PARTE 2 ====================================#



#==================================== PARTE 3 ====================================#
# Parte 3: Navegación a la página del calendario y selección del evento
driver.get('https://cursos.iberoleon.mx/online/calendar/view.php') # esto  navega a la página que le pongas como argumento
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "eventlist")))
eventos_proximos = driver.find_elements(By.CSS_SELECTOR, ".eventlist .card.rounded")

titulo_evento, descripcion_evento, pie_evento = evento_proximo(eventos_proximos)
print(f"Evento: {titulo_evento}\nDescripción: {descripcion_evento}\nPie: {pie_evento}")
#==================================== FIN DE PARTE 3 ====================================#



#==================================== PARTE 4 NO FUNCIONA ====================================#
# # Parte 4: Subida de archivos
entregar_tarea(eventos_proximos[0], pie_evento)

# 1. Hacer clic en el botón que abre la ventana modal
boton_agregar = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[@title='Agregar...'][contains(@class, 'btn-secondary')]"))
)
boton_agregar.click()

# # 2. Esperar a que la ventana modal sea visible
# ventana_modal = WebDriverWait(driver, 20).until(
#     EC.visibility_of_element_located((By.CLASS_NAME, "moodle-dialogue-wrap"))
# )

# # 3. Enviar la ruta del archivo al input del tipo file
input_file = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='file'][name='repo_upload_file']"))
)
input_file.send_keys(ruta_archivo)

# # 4. Hacer clic en el botón para subir el archivo
boton_subir = driver.find_element(By.CSS_SELECTOR, '.fp-upload-btn.btn-primary.btn')
boton_subir.click()

boton_guardar_cambios = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "id_submitbutton"))
)
boton_guardar_cambios.click()



#==================================== FIN DE PARTE 4 ====================================#


#==================================== PARTE 5 ====================================#
# Parte 5: Finalización y cierre
input("Presiona Enter para cerrar el navegador...")
driver.quit()
#==================================== FIN DE PARTE 5 ====================================#