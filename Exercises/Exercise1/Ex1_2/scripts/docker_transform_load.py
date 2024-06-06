# Transform Load functions:
# en for loop som, för varje fil i pokebelt
# öppnar json filen,
# läser ut base happiness
# sparar / appendar base happiness datan till en csv fil som sparas i pokedata/observations/observation_YY-MM-dd-HH-mm.csv
# ett bash kommando ska sedan deleta alla json-filerna, så att mappen är tom till nästa körning
import csv
import os
import datetime
import csv
import json

base_dir = os.path.dirname(os.path.abspath(__file__))
path_to_pokemons = os.path.join(base_dir, '../pokedata/pokebelt')
path_to_observations = os.path.join(base_dir, '../pokedata/observations')

def create_pokemon_list():
    """Creates a list containing all file names in the pokebelt directory (.json files)."""
    pokemon_list = os.listdir(path_to_pokemons)
    print(pokemon_list)
    return pokemon_list


def transform_load(list_of_pokemon_jsons):
    pokemons_list_of_dicts = []
    field_names = ['name', 'base_happiness']
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    for pokemon in list_of_pokemon_jsons:
        with open(f'{path_to_pokemons}/{pokemon}', 'r') as file:
            pokef = json.load(file)
            dict = {'name': pokef['name'] , 'base_happiness': pokef['base_happiness']}
            pokemons_list_of_dicts.append(dict)
    
    with open(f'{path_to_observations}/observation_{timestamp}.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(pokemons_list_of_dicts)

if __name__ == '__main__':
    pokemons_2 = create_pokemon_list()
    transform_load(pokemons_2)  