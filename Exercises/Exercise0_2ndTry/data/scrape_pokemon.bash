#!/usr/bin/env bash
for p in $(cat pokemon_list.txt)
do
    curl https://pokeapi.co/api/v2/pokemon-species/${p} > pokemons/${p}.json
done