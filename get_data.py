import pandas as pd
import requests


def getGames(user):
    req = "https://api.chess.com/pub/player/" + user + "/games/archives"
    li = requests.get(req).json()["archives"]
    li_games = []
    for x in li:
        li_games.append(requests.get(x).json())
    all_games = []
    for x in li_games:
        all_games.extend(x["games"])
    return all_games


def createDataset(li, user):
    import pandas as pd
    import chess.pgn
    import io

    col = ['player_username', 'opponent_username', 'played_as', 'opponent_played_as', 'result_for_player',
           'result_for_opponent',
           'player_rating', 'opponent_rating', 'time_class', 'opening', 'moves', 'first_move', 'rated', 'PGN', 'FEN']

    df = pd.DataFrame(columns=col)

    for x in li:

        liz = [None] * 15

        if x["rules"] != "chess":
            continue

        liz[0] = user
        liz[8] = x["time_class"]
        liz[13] = x["pgn"]
        liz[14] = x["fen"]
        liz[12] = x["rated"]

        try:
            pgn = chess.pgn.read_game(io.StringIO(x["pgn"]))
            opening = pgn.headers["ECOUrl"][31:].replace("-", " ")
            liz[9] = opening
        except:
            pass

        count = 0
        for moves in pgn.mainline_moves():
            if count == 0:
                liz[11] = str(moves)
            count += 1

        liz[10] = str(int(count / 2))

        if x["white"]["username"] == user:
            liz[2] = "white"
            liz[3] = "black"
            liz[4] = x["white"]["result"]
            liz[5] = x["black"]["result"]
            liz[6] = x["white"]["rating"]
            liz[7] = x["black"]["rating"]
            liz[1] = x["black"]["username"]


        else:
            liz[2] = "black"
            liz[3] = "white"
            liz[4] = x["black"]["result"]
            liz[5] = x["white"]["result"]
            liz[6] = x["black"]["rating"]
            liz[7] = x["white"]["rating"]
            liz[1] = x["white"]["username"]

        if None in liz:
            continue
        else:
            df.loc[len(df)] = liz

    df.to_csv(user + '/chess_dataset.csv', index=False)


def driver_fn(username):
    all_games_List = getGames(username)

    import os
    path = os.path.join("", username)
    try:
        os.mkdir(path)
    except:
        pass
    createDataset(all_games_List, username)