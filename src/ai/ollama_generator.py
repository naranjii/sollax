import subprocess
import json

def gerar_conteudo(system: str, user: str, model: str) -> str:
    prompt = f"{system}\n\n{user}"
    comando = ["ollama", "run", model, prompt]

    resultado = subprocess.run(comando, capture_output=True, text=True, encoding="utf-8", errors="replace")


    return resultado.stdout.strip()
