#!/bin/bash
# run the scripts for n times with m seconds sleep btwn runs:
n=10
m=15

for ((i=1; i<=n; i++))
do
    echo "Iteration $i"
    echo "running docker_extract_data.py:"
    python ./scripts/docker_extract_data.py
    echo "Running docker_transform_load.py:"
    python ./scripts/docker_transform_load.py
    echo "Observations content:"
    echo echo | ls pokedata/observations
    echo "Pokebelt content:"
    echo | ls pokedata/pokebelt
    echo "Running release_pokemons.sh"
    #rm pokedata/pokebelt/*
    bash scripts/release_pokemons.sh
    echo "Pokebelt content:"
    echo | ls pokedata/pokebelt
    if [ $i -lt $n ]; then
        sleep $m
    fi
done

echo "Completed $n iterations"