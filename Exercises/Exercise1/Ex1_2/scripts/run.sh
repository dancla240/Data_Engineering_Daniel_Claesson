#!/bin/bash
python docker_extract_data.py
python docker_transform_load.py
bash release_pokemons.sh