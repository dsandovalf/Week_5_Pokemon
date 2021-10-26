from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html.j2')

@app.route('/pokemon', methods=['GET', 'POST'])
def pokemon():
    if request.method == 'POST':
        pokemon = request.form.get('pokemon')
        url = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
        response = requests.get(url)
        if response.ok:
            if not response.json():
                return "We had an error loading your data. The pokemon you entered is not in the Pokedex"
            data = response.json()
            all_pokemon=[]
            pokemon_dict={
                "name":data["forms"][0]["name"],
                "ability": data["abilities"][0]["ability"]["name"],
                "base_experience":data["base_experience"],
                "base_hp":data["stats"][0]["base_stat"],
                "base_defense":data["stats"][2]["base_stat"],
                "base_attack":data["stats"][1]["base_stat"],
                "front_shiny":data["sprites"]["front_shiny"],
            }
            all_pokemon.append(pokemon_dict)
            print(all_pokemon)
            return render_template('pokemon.html.j2', pokemons=all_pokemon)
        else:
            return "The pokemon you entered is not in the Pokedex"
    return render_template('pokemon.html.j2')