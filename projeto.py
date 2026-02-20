import time, json, random
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    TimeoutException,
    NoSuchElementException,
)
from screenshot_manager import salvar_print
from config import URL_PAGINA, URL_BUSCA_PAGINA, NUMERO
from driver_factory import criar_driver
from decorators import verificar_tempo_execucao

@verificar_tempo_execucao
def buscar_edicao():
    driver = criar_driver()
    try:
        print(f"🔎 Acessando página: {URL_PAGINA}")
        driver.get(URL_PAGINA)
        wait = WebDriverWait(driver, 20)
        elemento = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "p.edicao"))
        )
        edicao_texto = elemento.text
        print("✅ Edição encontrada:")
        print(edicao_texto)
        return edicao_texto
    except Exception as erro:
        print("❌ Erro ao buscar edição")
        print(erro)
    finally:
        driver.quit()

def get_status_code(driver, url_base):
    logs = driver.get_log("performance")

    for log in logs:
        message = json.loads(log["message"])["message"]

        if message["method"] == "Network.responseReceived":

            response_url = message["params"]["response"]["url"]

            if url_base in response_url:
                status = message["params"]["response"]["status"]
                return status

    return None

def busca_atualizacao_cia(numero_cia, driver):
    
    try:
        if URL_BUSCA_PAGINA not in driver.current_url:
            print(f"🔎 Acessando página: {URL_BUSCA_PAGINA}")
            driver.get(URL_BUSCA_PAGINA)
            status_http = get_status_code(driver, URL_BUSCA_PAGINA)
            print(f"🌐 Status HTTP da página: {status_http}")
        
        wait = WebDriverWait(driver, 20)
        fechar_modal_se_existir(driver)
        elemento = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input#nrProcessoConsultaPublica"))
        )
        wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input#nrProcessoConsultaPublica"))
        )
        elemento.click()
        elemento.clear()
        print(f"Limpa o Input encontrado")
        # Insere numeros
        for char in numero_cia:
            tempo = random.uniform(0.13, 0.41)
            elemento.send_keys(char)
            print(f"Pressiona a tecla {char} (delay: {tempo:.2f}s)")
            time.sleep(tempo)
        # pressiona Enter
        elemento.send_keys(Keys.ENTER)
        print(f"Pressiona a tecla ENTER")
        print("⏳ Aguardando carregamento do resultado...")
        wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".ui-dialog-titlebar"))
        )
        print("✅ Resultado carregado")
        salvar_print(driver, numero_cia)
        print(f"Print da tela realizado com sucesso!")
    except TimeoutException:
        print("⏰ Timeout: elemento não apareceu no tempo esperado")

    except Exception as erro:
        print("❌ Erro inesperado:")
        print(erro)
    
def fechar_modal_se_existir(driver):
    try:
        wait = WebDriverWait(driver, 5)
        # Verifica se existe dialog visível
        dialog = driver.find_element(By.CSS_SELECTOR, ".ui-dialog")
        if dialog.is_displayed():
            print("⚠️ Modal detectado. Tentando fechar...")
            botao_fechar = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "a.ui-dialog-titlebar-close"))
            )
            botao_fechar.click()
            # Aguarda o modal desaparecer
            wait.until(
                EC.invisibility_of_element_located((By.CSS_SELECTOR, ".ui-dialog"))
            )
            print("✅ Modal fechado com sucesso!")

    except NoSuchElementException:
        # Não existe modal
        pass

    except TimeoutException:
        print("⏰ Não conseguiu fechar o modal no tempo esperado.")

def executar_buscas(numeros):
    driver = criar_driver()

    try:
        for numero in numeros:
            print(f"\n🚀 Iniciando busca para o processo: {numero}")
            busca_atualizacao_cia(numero, driver)
    finally:
        driver.quit()
        
def main():
    # buscar_edicao()
    NUMEROS = [
        "1",
        "2",
        "3",
    ]
    executar_buscas(NUMEROS)
    
if __name__ == "__main__":
    main()
    

