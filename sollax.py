import json
from src.ai.ollama_generator import gerar_conteudo
from src.selenium.tweet_sender import postar_tweet


with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)
print("🟢 config.json loaded")
# Gera o tweet
tweet = gerar_conteudo(
    system=config["system_prompt"],
    user=config["user_prompt"]
)
print("🐦 Sollax says:\n", tweet)

# Posta o tweet
postar_tweet(tweet, config["chrome_profile_path"])
print("🔥 Tweet posted ")
