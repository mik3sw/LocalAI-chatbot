import platform
import psutil
import GPUtil
import shutil
import sqlite3

def get_system_info():
    # Identifica il sistema operativo
    os_info = platform.system()
    is_apple_silicon = False

    # Verifica se il sistema è Apple Silicon
    if os_info == "Darwin":
        chip_info = platform.processor()
        if "arm" in chip_info:
            is_apple_silicon = True
    
    # Informazioni CPU
    cpu_info = psutil.cpu_percent(interval=1)
    cpu_count = psutil.cpu_count(logical=True)

    # Informazioni RAM
    ram_info = psutil.virtual_memory()
    ram_total = ram_info.total // (1024 * 1024)  # Converti in MB
    ram_used = ram_info.used // (1024 * 1024)    # Converti in MB
    ram_percent = ram_info.percent

    # Informazioni GPU
    if is_apple_silicon:
        gpu_name = "Apple Silicon Integrated GPU"
        gpu_mem_total = "Integrata"
        gpu_mem_used = "N/A"
        gpu_load = "N/A"
    else:
        gpus = GPUtil.getGPUs()
        gpu_info = gpus[0] if gpus else None
        gpu_name = gpu_info.name if gpu_info else "N/A"
        gpu_mem_total = gpu_info.memoryTotal if gpu_info else "N/A"
        gpu_mem_used = gpu_info.memoryUsed if gpu_info else "N/A"
        gpu_load = gpu_info.load * 100 if gpu_info else "N/A"

    # Informazioni Storage
    total, used, free = shutil.disk_usage("/")
    storage_total = total // (1024 * 1024 * 1024)  # Converti in GB
    storage_used = used // (1024 * 1024 * 1024)    # Converti in GB

    # Costruisci la stringa formattata con emoticon e dati
    if not is_apple_silicon:
        info_string = f"""
🖥️  <b>System Information ({os_info})</b>


🧠  <b>CPU</b>: {cpu_count} cores
    - Utilizzo: {cpu_info}%

💾  <b>RAM</b>: {ram_used}MB / {ram_total}MB ({ram_percent}% utilizzata)

📊  <b>Storage</b>: {storage_used}GB / {storage_total}GB

🎮  <b>GPU</b>: {gpu_name}
    - Memoria: {gpu_mem_used}MB / {gpu_mem_total}MB
    - Utilizzo GPU: {gpu_load}%
"""
    else:
        info_string = f"""
🖥️  <b>System Information ({os_info})</b>


🧠  <b>CPU</b>: {cpu_count} cores
    - Utilizzo: {cpu_info}%

💾  <b>RAM</b>: {ram_used}MB / {ram_total}MB ({ram_percent}% utilizzata)

📊  <b>Storage</b>: {storage_used}GB / {storage_total}GB

🎮  <b>GPU</b>: {gpu_name}
"""


    return info_string


def get_connection():
    return sqlite3.connect("db/chat.db")
    
def create_database():
    conn = get_connection()
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS interactions
              (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER, role TEXT, message TEXT, counter INTEGER)''')
    conn.commit()
    conn.close()

def save_interaction(user_id, role, message, counter):
    conn = get_connection()
    c = conn.cursor()
    c.execute("INSERT INTO interactions (user_id, role, message, counter) VALUES (?, ?, ?, ?)", (user_id, role, message, counter,))
    conn.commit()
    conn.close()

def get_user_interactions(user_id):
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM interactions WHERE user_id = ? ORDER BY COUNTER ASC", (user_id,))
    interactions = c.fetchall()
    conn.close()
    return interactions

def get_all_interactions():
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM interactions ")
    conn.commit()
    conn.close()


def delete_user_interactions(user_id):
    conn = get_connection()
    c = conn.cursor()
    c.execute("DELETE FROM interactions WHERE user_id = ?", (user_id,))
    conn.commit()
    conn.close()