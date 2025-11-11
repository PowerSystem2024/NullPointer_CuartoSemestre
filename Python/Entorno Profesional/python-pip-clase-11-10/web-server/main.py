import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

# Crear una instancia de FastAPI
app = FastAPI()
@app.get('/')
def get_list():
    return[1, 2, 3]
@app.get('/contact', response_class=HTMLResponse)
def get_list():
    return """
    <h1>Hola soy una pagina de contacto</h1>
    <p>Soy un parrafo para que leas</p>
"""
def run():
    store.get_razas()

if __name__ == "__main__":
    run()   