import time
from functools import wraps
from config import DEBUG

def verificar_tempo_execucao(funcao):
    if not DEBUG:
        return funcao
    @wraps(funcao)
    def wrapper(*args, **kwargs):
        inicio = time.perf_counter()
        resultado = funcao(*args, **kwargs)
        fim = time.perf_counter()

        print(f"[DEBUG] {funcao.__name__} executada em {fim - inicio:.2f}s")
        return resultado
    return wrapper
