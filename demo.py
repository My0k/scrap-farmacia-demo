import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_products(url):
    # Enviar solicitud HTTP al URL proporcionado
    response = requests.get(url)
    
    # Verificar que la solicitud fue exitosa
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Buscar los productos en la página
        # Suponiendo que todos los productos están contenidos en un elemento con una clase específica, ajusta según sea necesario
        productos = soup.find_all('div', class_="product-tile")  # Ajusta esta línea si es necesario
        
        data = []
        for producto in productos:
            # Extraer los datos del producto
            img_url = producto.find('img', class_="tile-image")['src']
            marca = producto.find('span', class_="link").text.strip()
            titulo = producto.find('a', class_="link").text.strip()
            precio = producto.find('span', class_="value").text.strip()
            
            # Generar el prompt para ChatGPT-4
            chatgpt_prompt = f"Crea una descripción de producto para ecommerce para una publicacion cuyo titulo sea {titulo} y de la marca {marca}, de entre 100 y 150 palabras detallado y utilizando un lenguaje variado y keywords relevantes para SEO"
            
            data.append([img_url, marca, titulo, precio, chatgpt_prompt])
        
        # Convertir los datos a DataFrame y guardar en un archivo Excel
        df = pd.DataFrame(data, columns=['URL Imagen', 'Marca', 'Título', 'Precio', 'Prompt ChatGPT-4'])
        df.to_excel('productos.xlsx', index=False)
        print("Archivo 'productos.xlsx' creado con éxito.")
    else:
        print("No fue posible obtener una respuesta exitosa del servidor.")

# Pedir al usuario que ingrese el URL
url_usuario = input("Por favor, ingrese el URL de la página para hacer scraping: ")
scrape_products(url_usuario)
