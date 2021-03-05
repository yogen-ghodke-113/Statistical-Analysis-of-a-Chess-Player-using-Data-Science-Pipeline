def fight(df, username):
    import pandas as pd
    li = []
    for index, row in df[df['result_for_opponent'] == "win"][-100:].iterrows():
        li.append([index, row["moves"]])

    moves_df = pd.DataFrame(li, columns=['game_no', 'moves'])

    import plotly.express as px
    k = px.line(x="game_no", y="moves", data_frame=moves_df)
    k.update_layout(title_text="No. of Moves made in the last 100 games when the player lost", title_x=0.5)

    import plotly.io as pio
    pio.write_image(k, username + "/fight.png", scale=3)


def wh_countplot(df, username):
    import seaborn as sns
    import pandas as pd

    white_df = df[df["played_as"] == "white"]
    white_op_freq = pd.DataFrame(white_df['opening'].value_counts())

    black_df = df[df["played_as"] == "black"]
    black_op_freq = pd.DataFrame(black_df["opening"].value_counts())

    w_li = []

    for opening, row in white_op_freq.head(20).iterrows():
        w_li.append(opening)

    b_li = []

    for opening, row in black_op_freq.head(20).iterrows():
        b_li.append(opening)


    sns.set(rc={'figure.figsize': (20, 15)})
    sns.set_style("darkgrid", {'axes.grid': False})

    top_wh_op = white_df[white_df['opening'].isin(w_li)]

    fig1 = sns.countplot(y='opening', data=top_wh_op)

    fig1.set_ylabel("")
    fig1.set_xlabel("Frequency", size=20, labelpad=30)
    fig1.tick_params(labelsize=17)
    fig1.get_figure().savefig(username + "/top_op_wh.png", bbox_inches='tight', dpi=300)

    fig1.get_figure().clf()

    top_bl_op = black_df[black_df['opening'].isin(b_li)]
    fig1 = sns.countplot(y='opening', data=top_bl_op)
    fig1.set_ylabel("")
    fig1.set_xlabel("Frequency", size=20, labelpad=30)
    fig1.tick_params(labelsize=17)
    fig1.get_figure().savefig(username + "/top_op_bl.png", bbox_inches='tight', dpi=300)


def most_used_wh(df, username):
    import chess
    import chess.svg
    import chess.pgn

    white_df = df[df["played_as"] == "white"]
    top_move = white_df["first_move"].value_counts().to_frame()
    # top_move.sort_values(by=['player_username'], inplace=True, ascending=False)
    top_move.rename(columns={0: 'First Name'})
    top_move_list = []

    ret_di = {}

    for move, row in top_move.head(3).iterrows():
        top_move_list.append(move)
        ret_di.update({move: row["first_move"]})

    num = 0
    for x in top_move_list:
        num += 1
        boardk = chess.Board()
        boardk.push(chess.Move.from_uci(x))
        from cairosvg import svg2png

        s1 = "chess." + x[0].upper() + x[1]
        s2 = "chess." + x[2].upper() + x[3]

        svg_code = chess.svg.board(board=boardk)
        svg2png(bytestring=svg_code, write_to=username + '/top_opening_move_as_white_' + str(num) + '.png', scale=4.0)


def rating_ladder(df, username):
    import pandas as pd
    li = []
    for index, row in df[df['rated'] & df['time_class'].isin(["blitz"])][-150:].iterrows():
        li.append([index, row["player_rating"]])

    moves_df = pd.DataFrame(li, columns=['game_no', 'player_rating'])

    import plotly.express as px
    k = px.line(x="game_no", y="player_rating", data_frame=moves_df)
    k.update_layout(title_text="", title_x=0.5)
    k['data'][0]['line']['color'] = "#FF4D4D"

    import plotly.io as pio
    pio.write_image(k, username + "/rating_ladder_red.png", scale=3)


def result_pi(df, username):
    result_li = df.result_for_player.unique()
    freq_li = []
    for index, row in df.groupby(['result_for_player']).count().iterrows():
        freq_li.append(row["player_username"])
    result_li.sort()
    df.groupby(['result_for_player']).count()

    from plotly.offline import iplot, init_notebook_mode
    #   init_notebook_mode(connected=True)
    import plotly.graph_objs as go

    trace = go.Pie(labels=result_li, values=freq_li)
    data = [trace]
    fig = go.Figure(data=data)

    fig.update_traces(textposition='inside', textinfo='value+label')
    import plotly.io as pio
    pio.write_image(fig, username + "/result_pi.png", scale=3)


def wh_result(df, username):
    import matplotlib.pyplot as plt
    c1 = df[df["played_as"] == "white"]
    wh_sizes = []
    wh_sizes.append(c1[c1["result_for_player"].isin(["win"])].shape[0])
    wh_sizes.append(c1[c1["result_for_player"].isin(
        ["agreed", "timevsinsufficient", "insufficient", "stalemate", "repetition"])].shape[0])
    wh_sizes.append(c1[c1["result_for_player"].isin(["resigned", "checkmated", "timeout", "abandoned"])].shape[0])

    plt.figure(figsize=(5, 5))
    labels = ["Wins", "Draws", "Losses"]

    colors = ["#ffe93f", "#723fff", "#3fffa2"]
    plt.pie(wh_sizes, labels=labels, colors=colors, autopct="%1.1f%%")

    # draw a circle at the center of pie to make it look like a donut
    centre_circle = plt.Circle((0, 0), 0.7, color="gray", fc="white")
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)
    plt.axis("equal")
    plt.savefig(username + '/result_as_wh.png', dpi=150)


def bl_result(df, username):
    import matplotlib.pyplot as plt

    c1 = df[df["played_as"] == "black"]
    bl_sizes = []
    bl_sizes.append(c1[c1["result_for_player"].isin(["win"])].shape[0])
    bl_sizes.append(c1[c1["result_for_player"].isin(
        ["agreed", "timevsinsufficient", "insufficient", "stalemate", "repetition"])].shape[0])
    bl_sizes.append(c1[c1["result_for_player"].isin(["resigned", "checkmated", "timeout", "abandoned"])].shape[0])

    plt.figure(figsize=(5, 5))
    labels = ["Wins", "Draws", "Losses"]
    colors = ["#ffe93f", "#723fff", "#3fffa2"]
    plt.pie(bl_sizes, labels=labels, colors=colors, autopct="%1.1f%%")
    centre_circle = plt.Circle((0, 0), 0.7, color="gray", fc="white")
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)
    plt.axis("equal")
    plt.savefig(username + '/result_as_bl.png', dpi=150)


def overall(df, username):
    import matplotlib.pyplot as plt
    import seaborn as sns
    most_frequently_opening = df["result_for_player"].value_counts().nlargest(30)
    plt.figure(figsize=(18, 8))
    palette = sns.color_palette("Blues_d", n_colors=15)
    # palette.reverse()
    opening = sns.barplot(x=most_frequently_opening.index, y=most_frequently_opening.values, palette=palette)
    # opening = sns.barplot(x=most_frequently_opening.index, y=most_frequently_opening.values, palette="Blues_d")
    plt.ylabel("Frequency", fontsize=18, labelpad=30)
    plt.xlabel("Game Result", fontsize=18, labelpad=30)
    for p in opening.patches:
        height = p.get_height()
        text = str(int(height))
        opening.text(p.get_x() + p.get_width() / 2, height + 2, text, ha="center")
    plt.savefig(username + '/overall_results.png', bbox_inches='tight', dpi=200)


def time_class(df, username):
    result_li = df.time_class.unique()
    freq_li = []
    for index, row in df.groupby(['time_class']).count().iterrows():
        freq_li.append(row["player_username"])
    result_li.sort()
    df.groupby(['time_class']).count()

    from plotly.offline import iplot, init_notebook_mode
    #   init_notebook_mode(connected=True)
    import plotly.graph_objs as go

    trace = go.Pie(labels=result_li, values=freq_li)
    data = [trace]
    fig = go.Figure(data=data)

    fig.update_traces(textposition='inside', textinfo='value+label')

    import plotly.io as pio
    pio.write_image(fig, username + "/time_class.png", scale=3)


#   iplot(fig)


def opening_results(df, username):
    import pandas as pd
    wh_opening_result_df = pd.DataFrame(columns=["opening", "wins", "draws", "losses"])
    white_df = df[df["played_as"] == "white"]
    white_op_freq = pd.DataFrame(white_df['opening'].value_counts())

    black_df = df[df["played_as"] == "black"]
    black_op_freq = pd.DataFrame(black_df["opening"].value_counts())

    w_li = []

    for opening, row in white_op_freq.head(20).iterrows():
        w_li.append(opening)

    b_li = []

    for opening, row in black_op_freq.head(20).iterrows():
        b_li.append(opening)

    df_bli = pd.DataFrame({"opening": b_li[:6]})

    wh_top_5 = []
    bl_top_5 = []
    df.groupby(['opening']).count()

    wh_op_name = []
    wh_win = []
    wh_draw = []
    wh_loss = []

    for x in range(5):
        wh_op_name.append(w_li[x])
        k = white_df[white_df["opening"] == w_li[x]]
        wh_win.append(k[k["result_for_player"].isin(["win"])].shape[0])
        wh_draw.append(k[k["result_for_player"].isin(
            ["agreed", "timevsinsufficient", "insufficient", "stalemate", "repetition"])].shape[0])
        wh_loss.append(k[k["result_for_player"].isin(["resigned", "checkmated", "timeout", "abandoned"])].shape[0])

    di2 = {  # 'opening':wh_op_name,
        'wins': wh_win,
        'draws': wh_draw,
        'losses': wh_loss
    }

    most_used_openings = pd.DataFrame(di2, index=wh_op_name)

    import matplotlib.pyplot as plt

    ax = most_used_openings[["wins", "draws", "losses"]].plot.barh(rot=0, color=["green", "blue", "red"], stacked=False)
    ax.set_facecolor('xkcd:white')
    ax.legend(prop={'size': 22})
    plt.title("Results for Top 5 Openings as White", size=30, y=1.05)
    plt.xlabel("Number of Games", size=20, labelpad=30)
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=20)
    plt.savefig(username + '/result_top_5_wh.png', dpi=150, bbox_inches='tight')

    bl_op_name = []
    bl_win = []
    bl_draw = []
    bl_loss = []

    for x in range(5):
        bl_op_name.append(b_li[x])
        k = black_df[black_df["opening"] == b_li[x]]
        bl_win.append(k[k["result_for_player"].isin(["win"])].shape[0])
        bl_draw.append(k[k["result_for_player"].isin(
            ["agreed", "timevsinsufficient", "insufficient", "stalemate", "repetition"])].shape[0])
        bl_loss.append(k[k["result_for_player"].isin(["resigned", "checkmated", "timeout", "abandoned"])].shape[0])

    di2 = {  # 'opening':wh_op_name,
        'wins': bl_win,
        'draws': bl_draw,
        'losses': bl_loss
    }

    most_used_openings = pd.DataFrame(di2, index=bl_op_name)

    import matplotlib.pyplot as plt

    ax = most_used_openings[["wins", "draws", "losses"]].plot.barh(rot=0, color=["green", "blue", "red"], stacked=False)
    ax.set_facecolor('xkcd:white')
    ax.legend(prop={'size': 22})
    plt.title("Results for Top 5 Openings as Black", size=30, y=1.05)
    plt.xlabel("Number of Games", size=20, labelpad=30)
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=20)
    plt.savefig(username + '/result_top_5_bl.png', dpi=150, bbox_inches='tight')


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

    fight(df, username)

    wh_countplot(df, username)
    most_used_wh(df, username)
    rating_ladder(df, username)
    result_pi(df, username)
    wh_result(df, username)
    bl_result(df, username)
    overall(df, username)
    time_class(df, username)
    opening_results(df, username)

    df.to_csv(username + '/chess_dataset_adv.csv', index=False)

    # opening_results(df,username)


import sys

driver_fn(sys.argv[1])
