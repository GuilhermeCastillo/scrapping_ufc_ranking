import requests
import page_ufc
import pandas as pd

url_rankings = "https://www.ufc.com.br/rankings"
response = requests.get(url_rankings)

titles = page_ufc.get_titles_rank(response)
titles = list(map(lambda x: x.replace(" ", ""), titles))

print(response)

dict_output = {}

for index_rank in range(1, 14):
    list_athlete = []
    list_rank = []
    
    for index_athlete in range(1, 16):
        rank, athlete = page_ufc.get_atleta_rank(response, index_rank, index_athlete)
        rank = "".join(rank).rstrip()
        athlete = "".join(athlete)
    
        list_athlete.append(athlete)
        list_rank.append(rank)

    dict_output[titles[index_rank - 1]] = list_athlete
    # dict_output["Top"] = list_rank

df = pd.DataFrame(dict_output)

df.to_csv("ufc_ranking.csv", index=False)

print(df)
