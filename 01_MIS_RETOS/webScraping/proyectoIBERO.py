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

#=====================================================================================================


# Abre la página que contiene el calendario de eventos
driver.get('https://cursos.iberoleon.mx/online/calendar/view.php')

# Espera hasta que el contenedor de eventos próximos sea visible
# Esta vez buscamos por clase, que parece ser más constante.
WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CLASS_NAME, "eventlist"))
)

# Encuentra los eventos próximos
# Utilizamos un selector de clase que identifique todos los elementos de eventos
eventos_proximos = driver.find_elements(By.CSS_SELECTOR, ".eventlist .card.rounded")

# Itera a través de los eventos para extraer la información
for evento in eventos_proximos:
    # Puedes extraer más información aquí si lo necesitas
    titulo_evento = evento.find_element(By.CSS_SELECTOR, '.card-header').text
    descripcion_evento = evento.find_element(By.CSS_SELECTOR, '.card-body').text
    pie_evento = evento.find_element(By.CSS_SELECTOR, '.card-footer').text
    print(f"Titulo: {titulo_evento}")
    print(f"Descripcion: {descripcion_evento}")
    print(f"Pie: {pie_evento}")
    print("----------")

input("Presiona Enter para cerrar el navegador...")

# Cierra el navegador después de presionar Enter
driver.quit()