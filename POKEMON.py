import requests
import shutil 
import json
class Llamadasinternet():
    def primer_request(self):
        url = 'https://github.com/'
        r = requests.get('https://github.com/')
        print(r )
        print(r.content)
        print(r.status_code)
    def imagen(self, url, file_name):

        res = requests.get(url,stream = True)
        if 200==res.status_code:
            with open(file_name, 'wb')as f:
                shutil.copyfileobj(res.raw, f)
            print('imagen descargada corectamente')
        else:
            print('No se encontro la imagen')

    def clima(self, city, api_key):
        base_url= 'https://api.openweathermap.org/data/2.5/weather?'
        params = {'q':city, 'appid':api_key,'units':'metric'}
        try:
            r = requests.get(base_url, params=params)
            r.raise_for_status()

            weather_data = r.json()
            if 200==weather_data['cod']:
                print(f'El clima en{weather_data['name']}:')
                print(f'Descripcion{weather_data['weather'][0]['description']}')
                print(f'Temperatura{weather_data['main']['temp']}°c')
                print(f'Humedad{weather_data['main']['humidity']}%')
                print(f'Viento{weather_data['wind']['speed']}m/s')
        except:
            print('error') 
       
    def nombre_pokemon(self,pokemon):
        
        url = ' https://pokeapi.co/api/v2/pokemon/'
        r = requests.get(url+pokemon)
        print(r)
        obj = json.loads(r.content)
        return obj['sprites']['back_default']
url = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/shiny/132.png"
req = Llamadasinternet()
pokemon = input("escribe el nombre del pokemon:")
img = req.nombre_pokemon(pokemon)
req.imagen(img, pokemon+".png")
#api_key = '69ec8ca2037d63a120d31c59efd0f604'
#city = 'Zapopan'
#req.clima(city, api_key)