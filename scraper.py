from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def scrape_crypto_prices():
    # Configurar as opções do Chrome
    chrome_options = Options()
    # chrome_options.add_argument("--headless")  # Comentado para ver o navegador em ação
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option("useAutomationExtension", False)

    # Inicializar o driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    crypto_data = []

    try:
        # Acessar a página
        url = "https://www.mercadobitcoin.com.br/"
        driver.get(url)
        
        # Esperar até que os preços sejam carregados
        wait = WebDriverWait(driver, 15)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "td[data-type='ticker-price']:not(:empty)")))
        
        # Encontrar todas as linhas de criptomoedas
        crypto_rows = driver.find_elements(By.CSS_SELECTOR, "tr.item")
        
        print("Criptomoedas e seus preços:")
        
        for row in crypto_rows:
            try:
                name_element = row.find_element(By.CSS_SELECTOR, "td.asset div.name")
                price_element = row.find_element(By.CSS_SELECTOR, "td[data-type='ticker-price']")
                
                if name_element and price_element:
                    name = name_element.text
                    price = price_element.text
                    crypto_data.append({"name": name, "price": price})
                    print(f"{name}: {price}")
            except Exception as e:
                pass
        
    except Exception as e:
        print(f"Erro ao acessar a página: {e}")
    
    finally:
        driver.quit()
        
    return crypto_data