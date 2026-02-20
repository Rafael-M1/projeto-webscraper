from PIL import Image
import imagehash
import os
import shutil
from datetime import datetime


# ==========================
# CONFIGURAÇÕES
# ==========================

THRESHOLD_DIFERENCA = 5

PASTA_PRINTS = "screenshots"
ULTIMA_IMAGEM = os.path.join(PASTA_PRINTS, "ultimo.png")
TEMP_IMAGEM = os.path.join(PASTA_PRINTS, "temp.png")


# ==========================
# FUNÇÕES INTERNAS
# ==========================

def _garantir_pasta():
    os.makedirs(PASTA_PRINTS, exist_ok=True)


def _imagem_diferente(caminho_nova, caminho_antiga):
    if not os.path.exists(caminho_antiga):
        return True

    img1 = Image.open(caminho_nova)
    img2 = Image.open(caminho_antiga)

    hash1 = imagehash.phash(img1)
    hash2 = imagehash.phash(img2)

    diferenca = hash1 - hash2

    print(f"📊 Diferença visual detectada: {diferenca}")

    return diferenca > THRESHOLD_DIFERENCA


def _gerar_nome_unico():
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S_%f')
    return f"resultado_{timestamp}.png"


# ==========================
# FUNÇÃO PÚBLICA (USE ESSA)
# ==========================

def salvar_print(driver, numero_processo):

    pasta_processo = os.path.join(PASTA_PRINTS, str(numero_processo))
    os.makedirs(pasta_processo, exist_ok=True)

    ultima_imagem = os.path.join(pasta_processo, "ultimo.png")
    temp_imagem = os.path.join(pasta_processo, "temp.png")

    driver.save_screenshot(temp_imagem)

    if _imagem_diferente(temp_imagem, ultima_imagem):
        nome_arquivo = _gerar_nome_unico()
        destino = os.path.join(pasta_processo, nome_arquivo)

        shutil.copy(temp_imagem, destino)
        shutil.copy(temp_imagem, ultima_imagem)

        print(f"Mudança detectada — Screenshot salvo: {destino}")
        os.remove(temp_imagem)
        return destino
    else:
        print("Nenhuma mudança detectada — Screenshot ignorado")
        os.remove(temp_imagem)
        return None