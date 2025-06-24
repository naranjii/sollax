import json
from ollama_generator import gerar_conteudo
from tweet_sender import postar_tweet

# Lê configurações
with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)
print("🟢 Configurações carregadas com sucesso.")
# Gera o tweet
tweet = gerar_conteudo(
    system=config["system_prompt"],
    user=config["user_prompt"]
)
print("🐦 Tweet gerado:\n", tweet)

# Posta o tweet
postar_tweet(tweet, config["chrome_profile_path"])
print("🟢 Tweet postado com sucesso.")
