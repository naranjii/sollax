from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

def postar_tweet(texto, chrome_profile_path):
    options = Options()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    options.add_argument(f"--user-data-dir={chrome_profile_path}")  # caminho completo para o diretório
    # options.add_argument("--headless=new")  # executa em segundo plano
    options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(options=options)
    driver.get("https://x.com/compose/tweet")
    time.sleep(5)
    box = driver.find_element(By.XPATH, '//div[@aria-label="Post text"]')
    box.send_keys(texto)
    time.sleep(2)
    post = driver.find_element(By.XPATH, "//button[@data-testid='tweetButton']")
    driver.execute_script("arguments[0].click();", post)
    time.sleep(5)

