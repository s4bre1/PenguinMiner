import json
import random
import threading
import time
import pyautogui as pg
import ctypes
import os
import keyboard

# ------------------ CONFIG ------------------
CONFIG_PATH = "config.json"

# Configuração padrão
default_config = {
    "enabled": True,
    "key": "j",
    "coordinates": None
}

# Carrega ou cria o config.json
if not os.path.exists(CONFIG_PATH):
    with open(CONFIG_PATH, "w") as f:
        json.dump(default_config, f, indent=4)

with open(CONFIG_PATH, "r") as f:
    config = json.load(f)

# Coordenadas
if not config.get("coordinates"):
    print("Mova o mouse até o CANTO SUPERIOR ESQUERDO da área onde deseja minerar...")
    time.sleep(5)
    pos1 = pg.position()

    print("Agora mova até o CANTO INFERIOR DIREITO...")
    time.sleep(5)
    pos2 = pg.position()

    config["coordinates"] = {
        "top_left": [pos1.x, pos1.y],
        "bottom_right": [pos2.x, pos2.y]
    }
    with open(CONFIG_PATH, "w") as f:
        json.dump(config, f, indent=4)
else:
    resposta = input("Deseja capturar novas coordenadas? (s/n): ").strip().lower()
    if resposta == "s":
        print("Mova o mouse até o CANTO SUPERIOR ESQUERDO da área onde deseja minerar...")
        time.sleep(5)
        pos1 = pg.position()

        print("Agora mova até o CANTO INFERIOR DIREITO...")
        time.sleep(5)
        pos2 = pg.position()

        config["coordinates"] = {
            "top_left": [pos1.x, pos1.y],
            "bottom_right": [pos2.x, pos2.y]
        }
        with open(CONFIG_PATH, "w") as f:
            json.dump(config, f, indent=4)

ENABLE_BOT = config.get("enabled", True)
PRESS_MIN = 0.09
PRESS_MAX = 0.12
STEP_EVERY_MIN = 20
STEP_EVERY_MAX = 40
STEP_DURATION = 0.25
CUSTOM_KEY = config.get("key", "j")
# --------------------------------------------

running = ENABLE_BOT
press_count = 0
start_time = time.time() if ENABLE_BOT else None
next_step_time = time.time() + random.uniform(STEP_EVERY_MIN, STEP_EVERY_MAX)
DIRECTIONS = ["left", "right", "up", "down"]
last_click = (0, 0)

print("\n[INFO] Bot está {}\n".format("LIGADO" if ENABLE_BOT else "DESLIGADO"))
print("Pressione Ctrl+C para encerrar o script.")
print(f"Pressione a tecla '{CUSTOM_KEY.upper()}' para ligar/desligar o bot.")


def format_time(seconds):
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = int(seconds % 60)
    return f"{h}H{m}M{s}S"


def update_title():
    if start_time is None:
        return
    elapsed = time.time() - start_time
    titulo = f"PenguinMiner - Miner: {press_count} - Tempo: {format_time(elapsed)}"
    ctypes.windll.kernel32.SetConsoleTitleW(titulo)


def random_walk():
    key = random.choice(DIRECTIONS)
    pg.keyDown(key)
    time.sleep(STEP_DURATION)
    pg.keyUp(key)


def random_click_within_area():
    global last_click
    x1, y1 = config["coordinates"]["top_left"]
    x2, y2 = config["coordinates"]["bottom_right"]

    # Evita clique muito próximo do anterior
    while True:
        x = random.randint(x1, x2)
        y = random.randint(y1, y2)
        if abs(x - last_click[0]) > 20 or abs(y - last_click[1]) > 20:
            break

    last_click = (x, y)
    pg.click(x, y)


def miner_loop():
    global next_step_time, press_count, start_time
    while True:
        if running:
            now = time.time()
            if now >= next_step_time:
                random_walk()
                random_click_within_area()
                time.sleep(1)  # Espera 1 segundo antes de pressionar D
                for _ in range(3):
                    pg.keyDown("d")
                    time.sleep(0.6)
                    pg.keyUp("d")
                    press_count += 1
                update_title()
                print(f"[LOG] Movimento, clique e 'D' pressionado 3x. Total: {press_count}")
                next_step_time = now + random.uniform(STEP_EVERY_MIN, STEP_EVERY_MAX)
            time.sleep(random.uniform(PRESS_MIN, PRESS_MAX))
        else:
            time.sleep(0.1)


def monitor_key():
    global running, start_time, press_count
    while True:
        keyboard.wait(CUSTOM_KEY)
        running = not running
        if running:
            start_time = time.time()
            press_count = 0
            print("[INFO] Bot LIGADO pelo teclado.")
        else:
            print("[INFO] Bot DESLIGADO pelo teclado.")

threading.Thread(target=miner_loop, daemon=True).start()
threading.Thread(target=monitor_key, daemon=True).start()

# Mantém o script vivo
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\n[ENCERRADO] Bot finalizado pelo usuário.")
