import subprocess
import json

def gerar_conteudo(system: str, user: str, modelo="llama3") -> str:
    prompt = f"{system}\n\n{user}"
    comando = ["ollama", "run", modelo, prompt]

    resultado = subprocess.run(comando, capture_output=True, text=True)

    if resultado.returncode != 0:
        raise RuntimeError(f"Erro ao executar o modelo Ollama:\n{resultado.stderr}")
    return resultado.stdout.strip()
