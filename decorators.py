import time
from functools import wraps

def verificar_tempo_execucao(funcao):
    @wraps(funcao)
    def wrapper(*args, **kwargs):
        inicio = time.perf_counter()
        resultado = funcao(*args, **kwargs)
        fim = time.perf_counter()

        print(f"⏱ Tempo de execução: {funcao.__name__}: {fim - inicio:.2f}s")

        return resultado
    return wrapper
