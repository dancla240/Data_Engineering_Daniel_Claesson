import pandas as pd
import requests
import json
import random
import time
import os

# define base directory
base_dir = os.path.dirname(os.path.abspath(__file__))

def create_pokelist():
    """Scrape web of first 151 Pokemons and save to file."""
    link = 'https://sv.wikipedia.org/wiki/Lista_%C3%B6ver_Pok%C3%A9mon'
    df = pd.DataFrame(pd.read_html(link)[1])
    df = df.iloc[0:151,[2,0]]
    df.rename(columns={'Nationellt Pokédex №' : 'Pokedex'}, inplace=True)
    df.set_index("Pokedex", inplace=True)
    df["Engelskt namn"].to_json("./Exercises/Exercise1/Ex1_2/pokedata/pokelist.json", orient="index")

def extract_pokemon_data():
    """Extracts data for 6 random Pokemons and saves the data as .json."""
    list_of_int = []

    while len(list_of_int) <= 5:
        rand_int = random.randint(1, 151)
        if rand_int not in list_of_int:
            list_of_int.append(rand_int)

    for item in list_of_int:
        pokelist_path = os.path.join(base_dir, '../pokedata/pokelist.json')
        with open(pokelist_path) as file:
            pokelist = json.load(file)
        pokemon = pokelist[str(item)].lower()
        pokemondata = requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{pokemon}")
        pokebelt_path = os.path.join(base_dir, f'../pokedata/pokebelt/{pokemon}.json')
        with open(pokebelt_path, 'w') as file2:
            #json.dump(pokebelt_path, file2)
            json.dump(pokemondata.json(), file2)
        time.sleep(2)

if __name__ == '__main__':
    create_pokelist()
    extract_pokemon_data()        