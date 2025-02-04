from scraper import scrape_crypto_prices
from exporter import export_to_json, export_to_sqlite

if __name__ == "__main__":
    crypto_data = scrape_crypto_prices()
    
    if crypto_data:
        # Exportar para JSON
        export_to_json(crypto_data, 'crypto_prices.json')
        
        # Exportar para SQLite
        export_to_sqlite(crypto_data, 'crypto_prices.db')
    else:
        print("Nenhum dado de criptomoeda foi encontrado.")