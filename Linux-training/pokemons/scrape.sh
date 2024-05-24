
#!/bin/bash
 
# File containing the list of Pokémon names
POKEMON_LIST="pokemon_list.txt"
 
# Base URL for the Pokémon API
BASE_URL="https://pokeapi.co/api/v2/pokemon-species"
 
# Loop through each line in the Pokémon list file
while IFS= read -r pokemon
do
    # Construct the URL
    URL="$BASE_URL/$pokemon"
 
    # Construct the output file name
    OUTPUT_FILE="$pokemon.json"
 
    # Download the JSON data and save it to the file
    curl -s -o "$OUTPUT_FILE" "$URL"
 
    # Check if the download was successful
    if [[ $? -eq 0 ]]; then
        echo "Downloaded data for $pokemon"
    else
        echo "Failed to download data for $pokemon"
    fi
sleep 2
done < "$POKEMON_LIST"
