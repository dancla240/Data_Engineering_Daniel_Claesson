# Transform Load functions:
# en for loop som, för varje fil i pokebelt
# öppnar json filen,
# läser ut base happiness
# sparar / appendar base happiness datan till en csv fil som sparas i pokedata/observations/observation_YY-MM-dd-HH-mm.csv
# ett bash kommando ska sedan deleta alla json-filerna, så att mappen är tom till nästa körning
import csv
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
path_to_pokemons = os.path.join(base_dir, '../pokedata/pokebelt')
pokemon_list = os.listdir(path_to_pokemons)
print(pokemon_list)