import requests

# Función para obtener las razas de perros desde una API externa
def get_razas():
    r = requests.get("https://dog.ceo/api/breeds/list/all")
    print(r.status_code)
    print(type(r.text)) 
    razas = r.json()
    for raza in razas.values():
        print(f"Raza de los perritos: {raza}")