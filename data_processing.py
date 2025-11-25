import pandas as pd
import numpy as np

df = pd.read_csv("cse158-assignment2-master.csv.gz")


# winner.trophies
# winner.isinclan
# loser.trophies
# loser.isinclan
# winner.cards
# winner.troops
# winner.structures
# winner.spells
# winner.commons
# winner.rares
# winner.epics
# winner.legendaries
# winner.elixir.average
# loser.cards
# loser.troops
# loser.structures
# loser.spells
# loser.commons
# loser.rares
# loser.epics
# loser.legendaries
# loser.elixir.average

stat_columns = [
        "trophies", "isinclan", "cards", "troops", "structures", "spells",
        "commons", "rares", "epics", "legendaries", "elixir.average"
]

# A is winner, B is loser
rows_A_winner = {}
for stat in stat_columns:
    rows_A_winner[f"A.{stat}"] = df[f"winner.{stat}"]
    rows_A_winner[f"B.{stat}"] = df[f"loser.{stat}"]
y_A_winner = pd.Series(np.ones(len(df)), name="label")   # A won = 1

df_A = pd.DataFrame(rows_A_winner)
df_A["label"] = y_A_winner

# B is winner, A is loser
rows_B_winner = {}
for stat in stat_columns:
    rows_B_winner[f"A.{stat}"] = df[f"winner.{stat}"]
    rows_B_winner[f"B.{stat}"] = df[f"loser.{stat}"]
y_B_winner = pd.Series(np.zeros(len(df)), name="label")   # A lost = 0

df_B = pd.DataFrame(rows_B_winner)
df_B["label"] = y_B_winner

df_pairs = pd.concat([df_A, df_B], ignore_index=True)