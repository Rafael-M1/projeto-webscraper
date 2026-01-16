from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import URL_PAGINA
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
            
def main():
    buscar_edicao()

if __name__ == "__main__":
    main()
