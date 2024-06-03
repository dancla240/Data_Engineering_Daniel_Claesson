import pandas as pd

# Scrapea webben för att få tag i datan på rätt format:
link = 'https://sv.wikipedia.org/wiki/Lista_%C3%B6ver_Pok%C3%A9mon'
df = pd.DataFrame(pd.read_html(link)[1])
df = df.iloc[0:151,[2,0]]
df.rename(columns={'Nationellt Pokédex №' : 'Pokedex'}, inplace=True)
df.set_index("Pokedex", inplace=True)
#df["Engelskt namn"].to_json("../pokedata/pokelist1.json", orient="index")
df["Engelskt namn"].to_json("./Exercises/Exercise1/Ex1_2/pokedata/pokelist.json", orient="index")