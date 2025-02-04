import json
import sqlite3
from datetime import datetime


def export_to_json(data, filename):
    # Primeiro, tenta carregar dados existentes
    try:
        with open(filename, 'r') as f:
            existing_data = json.load(f)
            if not isinstance(existing_data, dict):
                existing_data = {}
    except (FileNotFoundError, json.JSONDecodeError):
        existing_data = {}
    
    # Cria uma chave com a data/hora atual
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    
    # Adiciona os novos dados com a timestamp como chave
    existing_data[timestamp] = data
    
    # Salva todos os dados de volta no arquivo
    with open(filename, 'w') as f:
        json.dump(existing_data, f, indent=4)

def export_to_sqlite(data, db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS crypto_prices (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price TEXT NOT NULL
        )
    ''')
    
    for item in data:
        cursor.execute('''
            INSERT INTO crypto_prices (name, price) VALUES (?, ?)
        ''', (item['name'], item['price']))
    
    conn.commit()
    conn.close()