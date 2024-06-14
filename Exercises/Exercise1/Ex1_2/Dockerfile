FROM python:3.12.3

WORKDIR /Ex1_2

COPY ./scripts/docker_extract_data.py ./scripts/docker_extract_data.py 
COPY ./scripts/docker_transform_load.py ./scripts/docker_transform_load.py
COPY ./scripts/release_pokemons.sh ./scripts/release_pokemons.sh
COPY ./scripts/run.sh ./scripts/run.sh

RUN mkdir -p ./pokedata/observations
RUN mkdir -p ./pokedata/pokebelt
RUN pip install pandas requests lxml
RUN chmod +x ./scripts/run.sh


CMD ["./scripts/run.sh"]