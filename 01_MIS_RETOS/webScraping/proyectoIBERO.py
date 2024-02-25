from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Parte 1: Configuración inicial y acceso a la página
chrome_options = Options()
# chrome_options.add_argument("--headless")  # Descomenta para ejecutar en modo sin cabeza
chrome_service = Service(executable_path='C:\\Users\\ferna\\OneDrive\\Documentos\\Semestre_II\\01_MIS_RETOS\\webScraping\\chromedriver.exe')
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
driver.get('https://cursos.iberoleon.mx/online/login/index.php')

# Parte 2: Inicio de sesión
username = '192488-7'
password = 'Ftry2131*'
driver.find_element(By.NAME, 'username').send_keys(username)
driver.find_element(By.NAME, 'password').send_keys(password)
login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "loginbtn")))
login_button.click()

# Parte 3: Navegación a la página del calendario y selección del evento
driver.get('https://cursos.iberoleon.mx/online/calendar/view.php')
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "eventlist")))
eventos_proximos = driver.find_elements(By.CSS_SELECTOR, ".eventlist .card.rounded")
for evento in eventos_proximos:
    titulo_evento = evento.find_element(By.CSS_SELECTOR, '.card-header').text
    pie_evento = evento.find_element(By.CSS_SELECTOR, '.card-footer').text
    if "Añadir envío" in pie_evento:
        enlace_envio = evento.find_element(By.CSS_SELECTOR, 'a.card-link')
        enlace_envio.click()
        break  # Salir del bucle después de hacer clic en el enlace

# Parte 4: Subida de archivos
# Espera hasta que la nueva página cargue completamente o hasta que un elemento específico sea visible
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='files_filemanager']")))

# Utiliza JavaScript para encontrar el input de tipo file y hacerlo visible
input_file_script = """
var fileInput = document.querySelector('input[name="files_filemanager"]');
if (fileInput) {
    fileInput.style.display = 'block';
    return true;
}
return false;
"""
# Ejecuta el script
file_input_visible = driver.execute_script(input_file_script)

if file_input_visible:
    # Si el script ha hecho el input visible, procede a enviar el archivo
    file_path = r'C:\Users\ferna\OneDrive\Documentos\Semestre_II\01_MIS_RETOS\webScraping\materias\analisisDatos\Investigación sobre Logaritmos y Antilogaritmos.pdf'
    driver.find_element(By.NAME, 'files_filemanager').send_keys(file_path)
else:
    print("No se pudo hacer visible el input de archivo.")

# Parte 5: Finalización y cierre
# Agrega aquí cualquier paso adicional que necesites realizar, como guardar el envío
input("Presiona Enter para cerrar el navegador...")
driver.quit()
