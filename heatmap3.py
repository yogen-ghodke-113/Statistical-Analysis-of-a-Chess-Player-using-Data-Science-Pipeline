def heatmap(df,username):
    import matplotlib.pyplot as plt
    import seaborn as sns
    sns.set(rc={'figure.figsize': (20, 15)})
    sns.set(font_scale=1.5)
    k = sns.heatmap(df.corr(), annot=True, square=False)
    k.get_figure().savefig(username + "/corr_heatmap.png", bbox_inches='tight', dpi=300)



def driver_fn(username):
    import pandas as pd

    df = pd.read_csv(username + '\chess_dataset.csv')
    kt = pd.DataFrame(df["player_rating"] - df["opponent_rating"])
    df.insert(8, "rating_difference", kt, False)
    df_res = []

    for row in df.result_for_player:
        if row == "win":
            df_res.append(1)
        elif row in ["agreed", "timevsinsufficient", "insufficient", "stalemate", "repetition"]:
            df_res.append(0.5)
        elif row in ["resigned", "checkmated", "timeout", "abandoned"]:
            df_res.append(0)

    df_res = pd.DataFrame(df_res, columns=['result_val_for_player'])
    df.insert(9, 'result_val_for_player', df_res, False)
    
    heatmap(df,username)
    
    
import sys
driver_fn(sys.argv[1])