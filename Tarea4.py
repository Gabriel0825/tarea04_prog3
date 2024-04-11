from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Edge()

driver.get("https://www.demoblaze.com/index.html")

#Funcion para maximizar la pantalla
driver.maximize_window()
time.sleep(2)

"""# Historia de Usuario 1- Registrar Usuario Nuevo

signUser= driver.find_element(By.XPATH, "//a[contains(@id,'signin2')]").click()
time.sleep(1)
userName= driver.find_element(By.XPATH, "//input[contains(@id,'sign-username')]").send_keys("20210055")
Password= driver.find_element(By.XPATH, "//input[contains(@id,'sign-password')]").send_keys("A*12345678")
SingUp= driver.find_element(By.XPATH, "//button[@type='button'][contains(.,'Sign up')]").click()"""


# Historia de Usuario 2- Loguearse con usuario ya registrado

"""logUser= driver.find_element(By.XPATH, "//a[contains(@id,'login2')]").click()
time.sleep(1)
logUserName= driver.find_element(By.XPATH, "//input[contains(@id,'loginusername')]").send_keys("20210055")
logPassword= driver.find_element(By.XPATH, "//input[contains(@id,'loginpassword')]").send_keys("A*12345678")
LogIn= driver.find_element(By.XPATH, "//button[@type='button'][contains(.,'Log in')]").click()"""


# Historia de Usuario 3- Añadir Producto a carrito

addToCart= driver.find_element(By.XPATH, "//a[@href='prod.html?idp_=4'][contains(.,'Samsung galaxy s7')]").click()
time.sleep(1)


#Tiempo de suspension de la pantalla (Segundos)
time.sleep(20)

#Cerrar ventana y finalizar prueba
driver.quit()