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

def salvar_print_se_diferente(driver):
    """
    Salva screenshot somente se houver mudança visual
    """

    _garantir_pasta()

    temp_path = TEMP_IMAGEM

    # Screenshot temporário
    driver.save_screenshot(temp_path)

    if _imagem_diferente(temp_path, ULTIMA_IMAGEM):
        nome_arquivo = _gerar_nome_unico()
        destino = os.path.join(PASTA_PRINTS, nome_arquivo)
        shutil.copy(temp_path, destino)
        shutil.copy(temp_path, ULTIMA_IMAGEM)
        print(f"Mudança detectada — Screenshot salvo: {destino}")
        os.remove(temp_path)
        return destino
    else:
        print("Nenhuma mudança detectada — Screenshot ignorado")
        os.remove(temp_path)
        return None
