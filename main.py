from fastapi import FastAPI
import requests
import re

app = FastAPI()

@app.get("/get-nexus-link")
def get_link():
    # URL de la web donde está el canal (la que usas para sacar el token)
    target_url = "https://futbollibre.example/sky-sports" 
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }

    try:
        response = requests.get(target_url, headers=headers, timeout=10)
        # Buscamos el patrón del playbackURL en el código fuente
        match = re.search(r'var playbackURL = "(https://.*?index\.m3u8\?token=.*?)";', response.text)
        
        if match:
            return {"status": "success", "url": match.group(1)}
        else:
            return {"status": "error", "message": "No se encontró el token"}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.get("/")
def home():
    return {"message": "Nexus API Online"}