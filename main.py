from tkinter import *
from tkinter import ttk

import PIL
from PIL import ImageTk
from PIL.Image import Image

root = Tk()
root.iconbitmap("img_files/bishop.ico")
root.geometry("%dx%d" % (root.winfo_screenwidth(), root.winfo_screenheight()))
title = "Statistical Analysis of a Chess Player using Data Science Pipeline"
root.title(title)
root.state('zoomed')
tabControl = ttk.Notebook(root)

ttk.Style().theme_create("yg", parent="alt", settings={
    "TNotebook": {"configure": {"tabmargins": [2, 5, 2, 0]}},
    "TNotebook.Tab": {
        "configure": {"padding": [50, 10], "background": "#454444", "foreground": "#FFF",
                      "font": ('Helvetica', '12', 'bold')},
        "map": {"background": [("selected", "#000")], "foreground": [("selected", "#FFF")],
                "expand": [("selected", [1, 1, 1, 0])]}}})

ttk.Style().theme_use("yg")


def resize_img(x, src):
    img = PIL.Image.open(src)
    wpercent = (x / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((x, hsize), PIL.Image.ANTIALIAS)
    return ImageTk.PhotoImage(img, PIL.Image.ANTIALIAS)


def stretch_img(x, y, src):
    return ImageTk.PhotoImage(PIL.Image.open(src).resize((x, y), PIL.Image.ANTIALIAS))


def assign_grid(fr, n):
    for x in range(n):
        fr.grid_columnconfigure(x, weight=1)
    for x in range(15 * n):
        fr.grid_rowconfigure(x, weight=1)


tab1 = Frame(tabControl)
tab2 = Frame(tabControl)
tab3 = Frame(tabControl)
tab4 = Frame(tabControl)
tab5 = Frame(tabControl)

tabControl.add(tab1, text='Home')
tabControl.add(tab2, text='User Input')
tabControl.add(tab3, text='Player  Analysis')
tabControl.add(tab4, text='Game Prediction')
tabControl.add(tab5, text='About')
tabControl.pack(expand=1, fill="both")

#############################################################

# Home Tab

frame = Frame(tab1)
frame.pack(fill="both", expand=True)

# Scroll Bar Implementation

my_canvas = Canvas(frame)
my_canvas.pack(side=LEFT, fill=BOTH, expand=True)
my_scrollbar = ttk.Scrollbar(frame, orient=VERTICAL, command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)
my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
second_frame = Frame(my_canvas)
my_canvas.create_window((0, 0), window=second_frame, anchor="nw", width=1517)

f1 = Frame(second_frame)
f1.pack(fill="both", pady=10, expand=True)

tit_frame = Frame(f1)
tit_frame.pack(fill="x")

assign_grid(tit_frame, 9)

p = resize_img(50, "img_files/chess.png")

Label(tit_frame, image=p).grid(row=0, column=1, sticky="e", padx=0)

Title = Label(tit_frame, text=title, font=("Arial", 25), padx=20, pady=20, borderwidth=5, relief="sunken")
Title.grid(padx=20, pady=20, row=0, column=2, columnspan=5)

Label(tit_frame, image=p).grid(row=0, column=7, sticky="w")

Title = Label(tit_frame, text="Introduction :", font=("Arial", 18, "underline", "bold"), padx=20, pady=20)
Title.grid(padx=20, pady=(20, 0), row=1, column=1, columnspan=2, sticky="w")

intro_text = "There is no tool available in the market which provides an in-depth analysis of \na player’s overall " \
             "games. This software provides Chess players a tool to \nimprove their chess game with assistance from several " \
             "Machine Learning and \nData Science techniques. It works by studying the player's previous games \nand " \
             "deriving useful data to help them learn from their previous mistakes. "

Title = Label(tit_frame, text=intro_text, font=("Arial", 18), padx=20, pady=20, anchor="e", justify=LEFT)
Title.grid(padx=(60, 0), pady=0, row=2, column=1, columnspan=6, sticky="w")

k = resize_img(400, "img_files/magnus.png")
Label(tit_frame, image=k).grid(row=2, column=6, columnspan=3, sticky="nsew")

Title = Label(tit_frame, text="Tutorial :", font=("Arial", 18, "underline", "bold"), padx=20, pady=20)
Title.grid(padx=20, pady=(20, 0), row=3, column=1, columnspan=2, sticky="w")

intro_text = "Click on the black tabs on the top to switch different modes of operation.\n\n" \
             "1. User Input : \n\n          Provides a complete statistical data analysis, based on your previous\n" \
             "          chess games. Just enter your chess.com username and wait for a\n" \
             "          few seconds. The program will download all your data via API.\n\n" \
             "2. Player Analysis : \n\n " \
             "          Provides a thorough analysis of your data with interactive charts and\n" \
             "           data visualization. \n\n " \
             "          Also gives you detailed instructions on how to interpret the charts. \n\n" \
             "3. Game Prediction : \n\n" \
             "          Enter you and your opponent's username and see the prediction on \n" \
             "          the result of the game between you two.\n\n" \
             "          This module, uses Logistic Regression on your previous game data to \n" \
             "          predict who, among the two will be the winner in the next game or whether \n" \
             "          the game would be a draw. "

Title = Label(tit_frame, text=intro_text, font=("Arial", 18), padx=20, pady=20, anchor="e", justify=LEFT)
Title.grid(padx=(60, 0), pady=0, row=4, column=1, columnspan=6, sticky="nw")

t = resize_img(400, "img_files/kasparov.png")
Label(tit_frame, image=t).grid(row=4, column=6, columnspan=3, sticky="ns")

Label(tit_frame, text="\n\n\n").grid(padx=(60, 0), pady=0, row=5, column=1, columnspan=6, sticky="nw")

#############################################################
# User Input Tab

frame2 = Frame(tab2)
frame2.pack(fill="both", expand=True)

# Scroll Bar Implementation

my_canvas2 = Canvas(frame2)
my_canvas2.pack(side=LEFT, fill=BOTH, expand=True)
my_scrollbar2 = ttk.Scrollbar(frame2, orient=VERTICAL, command=my_canvas.yview)
my_scrollbar2.pack(side=RIGHT, fill=Y)
my_canvas2.configure(yscrollcommand=my_scrollbar2.set)
my_canvas2.bind('<Configure>', lambda e: my_canvas2.configure(scrollregion=my_canvas2.bbox("all")))
second_frame2 = Frame(my_canvas2)
my_canvas2.create_window((0, 0), window=second_frame2, anchor="nw", width=1517)

f2 = Frame(second_frame2)
f2.pack(fill="both", pady=10, expand=True)

tit_frame2 = Frame(f2)
tit_frame2.pack(fill="x")

assign_grid(tit_frame2, 9)

pz2 = resize_img(50, "img_files/chess.png")

Label(tit_frame2, image=pz2).grid(row=0, column=3, sticky="e", padx=0)

Title = Label(tit_frame2, text="User Input", font=("Arial", 25), padx=40, pady=20, borderwidth=5, relief="sunken")
Title.grid(padx=20, pady=20, row=0, column=2, columnspan=5)

Label(tit_frame2, image=pz2).grid(row=0, column=5, sticky="w")

Title = Label(tit_frame2, text="Enter your username :", font=("Arial", 22, "bold"), padx=20, pady=20)
Title.grid(padx=0, pady=(20, 0), row=1, column=1, columnspan=6, sticky="w")

username_input = Entry(tit_frame2, width=30, borderwidth=3, font=("Arial", 15))
username_input.insert(0, 'username')
username_input.grid(row=2, column=4, padx=(5, 0), pady=(25, 0), ipady=8)


def tut_click():
    from tkinter import messagebox
    username = username_input.get()
    print(username)
    messagebox.showinfo("Loading", "Fetching Data, Please Wait.")
    from os import path
    if not path.exists(username + "/corr_heatmap.png"):
        import get_data as gd
        gd.driver_fn(username)
        import visualize as viz
        viz.visualize_data(username)
    ki(username)
    messagebox.showinfo("Completed", "Analysis Complete. Proceed to the Player Analysis Tab.")
    Title1 = Label(tit_frame2, text="Data Analysis Complete. \n\n ", font=("Arial", 18), padx=20, pady=20)
    Title1.grid(row=5, column=4, sticky="ns", pady=(30, 0))


Tutorial_bttn = Button(tit_frame2, text="Request Analysis", font=("Arial", 15), padx=20, pady=8, command=tut_click)
Tutorial_bttn.grid(row=3, column=4, sticky="ns", pady=(30, 0))

#############################################################
# Player Analysis Tab

frame3 = Frame(tab3)
frame3.pack(fill="both", expand=True)

# Scroll Bar Implementation

my_canvas3 = Canvas(frame3)
my_canvas3.pack(side=LEFT, fill=BOTH, expand=True)
my_scrollbar3 = ttk.Scrollbar(frame3, orient=VERTICAL, command=my_canvas3.yview)
my_scrollbar3.pack(side=RIGHT, fill=Y)
my_canvas3.configure(yscrollcommand=my_scrollbar3.set)
my_canvas3.bind('<Configure>', lambda e: my_canvas3.configure(scrollregion=my_canvas3.bbox("all")))
second_frame3 = Frame(my_canvas3)
my_canvas3.create_window((0, 0), window=second_frame3, anchor="nw", width=1517)

f3 = Frame(second_frame3)
f3.pack(fill="both", pady=10, expand=True)

tit_frame3 = Frame(f3)
tit_frame3.pack(fill="x")

assign_grid(tit_frame3, 9)

pz3 = resize_img(50, "img_files/chess.png")

Label(tit_frame3, image=pz3).grid(row=0, column=2, sticky="e", padx=(100, 0))

Title = Label(tit_frame3, text="Player Analysis", font=("Arial", 25), padx=40, pady=20, borderwidth=5, relief="sunken")
Title.grid(padx=(100, 0), pady=20, row=0, column=2, columnspan=5)

Label(tit_frame3, image=pz3).grid(row=0, column=6, sticky="w", padx=(100, 0))


def ki(u):
    Title = Label(tit_frame3, text="Top 20 Most Played Openings as White :", font=("Arial", 18, "underline", "bold"),
                  padx=20, pady=20)
    Title.grid(padx=0, pady=(20, 0), row=1, column=1, columnspan=6, sticky="w")

    intro_text = "This is a frequency countplot chart of the user's top 20 most played openings as white.  \n"

    Title = Label(tit_frame3, text=intro_text, font=("Arial", 18), padx=20, pady=20, anchor="e", justify=LEFT)
    Title.grid(padx=(60, 0), pady=0, row=2, column=1, columnspan=10, sticky="w")

    k = resize_img(1200, u + "/top_op_wh.png")
    mg = Label(tit_frame3, image=k)
    mg.image = k
    mg.grid(row=3, column=0, columnspan=10, sticky="nsew")

    Title = Label(tit_frame3, text="Top 3 First Moves as White : ", font=("Arial", 18, "underline", "bold"),
                  padx=20, pady=20)
    Title.grid(padx=0, pady=(20, 0), row=4, column=1, columnspan=6, sticky="w")

    intro_text = "These are the top 3 first moves made by user as white. ( #1, #2, #3 from Left to Right. )  \n"

    Title = Label(tit_frame3, text=intro_text, font=("Arial", 18), padx=20, pady=20, anchor="e", justify=LEFT)
    Title.grid(padx=(60, 0), pady=0, row=5, column=1, columnspan=10, sticky="w")

    k = resize_img(400, u + "/top_opening_move_as_white_1.png")
    mg = Label(tit_frame3, image=k)
    mg.image = k
    mg.grid(row=6, column=0, columnspan=3, sticky="nsew")

    try:
        k = resize_img(400, u + "/top_opening_move_as_white_2.png")
        mg = Label(tit_frame3, image=k)
        mg.image = k
        mg.grid(row=6, column=3, columnspan=3, sticky="nsew")
    except:
        pass

    try:
        k = resize_img(400, u + "/top_opening_move_as_white_3.png")
        mg = Label(tit_frame3, image=k)
        mg.image = k
        mg.grid(row=6, column=6, columnspan=3, sticky="nsew")
    except:
        pass

    Title = Label(tit_frame3, text="First Opening Move Heatmap as White : ", font=("Arial", 18, "underline", "bold"),
                  padx=20, pady=20)
    Title.grid(padx=0, pady=(20, 0), row=7, column=1, columnspan=6, sticky="w")

    intro_text = "This is the heatmap of the first moves made as white. Darker squares represent higher frequency.  \n"

    Title = Label(tit_frame3, text=intro_text, font=("Arial", 18), padx=20, pady=20, anchor="e", justify=LEFT)
    Title.grid(padx=(60, 0), pady=0, row=8, column=1, columnspan=10, sticky="w")

    k = resize_img(500, u + "/heatmap_starting.png")
    mg = Label(tit_frame3, image=k)
    mg.image = k
    mg.grid(row=9, column=2, columnspan=3, sticky="nsew", padx=(0, 0))

    k = resize_img(500, u + "/heatmap_landing.png")
    mg = Label(tit_frame3, image=k)
    mg.image = k
    mg.grid(row=9, column=5, columnspan=3, sticky="nsew", padx=(0, 0))

    Title = Label(tit_frame3, text="Top 20 Most Played Defences as Black :", font=("Arial", 18, "underline", "bold"),
                  padx=20, pady=20)
    Title.grid(padx=0, pady=(20, 0), row=10, column=1, columnspan=6, sticky="w")

    intro_text = "This is a frequency countplot chart of the user's top 20 most played defences as black in respond to white's first move.  \n"

    Title = Label(tit_frame3, text=intro_text, font=("Arial", 18), padx=20, pady=20, anchor="e", justify=LEFT)
    Title.grid(padx=(60, 0), pady=0, row=11, column=1, columnspan=10, sticky="w")

    k = resize_img(1200, u + "/top_op_bl.png")
    mg = Label(tit_frame3, image=k)
    mg.image = k
    mg.grid(row=12, column=0, columnspan=10, sticky="nsew")

    Title = Label(tit_frame3, text="Correlation Heatmap of the Features in the Dataset :",
                  font=("Arial", 18, "underline", "bold"),
                  padx=20, pady=20)
    Title.grid(padx=0, pady=(20, 0), row=13, column=1, columnspan=6, sticky="w")

    intro_text = "This a heatmap of correlation between all the features of the downloaded dataset. Higher number means higher correlation.\n"

    Title = Label(tit_frame3, text=intro_text, font=("Arial", 18), padx=20, pady=20, anchor="e", justify=LEFT)
    Title.grid(padx=(60, 0), pady=0, row=14, column=1, columnspan=10, sticky="w")

    k = resize_img(800, u + "/corr_heatmap.png")
    mg = Label(tit_frame3, image=k)
    mg.image = k
    mg.grid(row=15, column=2, columnspan=5, sticky="nsew")

    Title = Label(tit_frame3, text="Player's Elo Rating in the last 150 Rated Blitz Games :",
                  font=("Arial", 18, "underline", "bold"),
                  padx=20, pady=20)
    Title.grid(padx=0, pady=(20, 0), row=16, column=1, columnspan=6, sticky="w")

    intro_text = "This a line graph of the user's ELO rating. Upward graph indicates positive progress.\n"

    Title = Label(tit_frame3, text=intro_text, font=("Arial", 18), padx=20, pady=20, anchor="e", justify=LEFT)
    Title.grid(padx=(60, 0), pady=0, row=17, column=1, columnspan=10, sticky="w")

    k = stretch_img(1200, 600, u + "/rating_ladder_red.png")
    mg = Label(tit_frame3, image=k)
    mg.image = k
    mg.grid(row=18, column=1, columnspan=7, sticky="nsew")

    Title = Label(tit_frame3, text="Types of different Time Class Control Games played :",
                  font=("Arial", 18, "underline", "bold"),
                  padx=20, pady=20)
    Title.grid(padx=0, pady=(20, 0), row=19, column=1, columnspan=6, sticky="w")

    intro_text = "Different Classes of time control are blitz, bullet, classical, puzzle, chess960 and rapid.\n"

    Title = Label(tit_frame3, text=intro_text, font=("Arial", 18), padx=20, pady=20, anchor="e", justify=LEFT)
    Title.grid(padx=(60, 0), pady=0, row=20, column=1, columnspan=10, sticky="w")

    k = resize_img(800, u + "/time_class.png")
    mg = Label(tit_frame3, image=k)
    mg.image = k
    mg.grid(row=21, column=2, columnspan=5, sticky="nsew")

    Title = Label(tit_frame3, text="How much of a fight the user puts up when losing :",
                  font=("Arial", 18, "underline", "bold"),
                  padx=20, pady=20)
    Title.grid(padx=0, pady=(20, 0), row=22, column=1, columnspan=6, sticky="w")

    intro_text = "These are all the games where the user lost. More number of moves in the games means the user put up a good fight\nbefore resigning. Less number of moves indicate that the player blundered early on in the game.\n"

    Title = Label(tit_frame3, text=intro_text, font=("Arial", 18), padx=20, pady=20, anchor="e", justify=LEFT)
    Title.grid(padx=(60, 0), pady=0, row=23, column=1, columnspan=10, sticky="w")

    k = stretch_img(1200, 600, u + "/fight.png")
    mg = Label(tit_frame3, image=k)
    mg.image = k
    mg.grid(row=24, column=1, columnspan=7, sticky="nsew")

    Title = Label(tit_frame3, text="Overall Result of all the Games played :",
                  font=("Arial", 18, "underline", "bold"),
                  padx=20, pady=20)
    Title.grid(padx=0, pady=(20, 0), row=25, column=1, columnspan=6, sticky="w")

    intro_text = "This is a frequency plot of the result of all the games, the user has played on the website.\n"

    Title = Label(tit_frame3, text=intro_text, font=("Arial", 18), padx=20, pady=20, anchor="e", justify=LEFT)
    Title.grid(padx=(60, 0), pady=0, row=26, column=1, columnspan=10, sticky="w")

    k = resize_img(1200, u + "/overall_results.png")
    mg = Label(tit_frame3, image=k)
    mg.image = k
    mg.grid(row=27, column=1, columnspan=7, sticky="nsew")

    Title = Label(tit_frame3, text="Overall Result of all the Games played :",
                  font=("Arial", 18, "underline", "bold"),
                  padx=20, pady=20)
    Title.grid(padx=0, pady=(20, 0), row=28, column=1, columnspan=6, sticky="w")

    intro_text = "This is a pie chart of the result of all the games, the user has played on the website.\n"

    Title = Label(tit_frame3, text=intro_text, font=("Arial", 18), padx=20, pady=20, anchor="e", justify=LEFT)
    Title.grid(padx=(60, 0), pady=0, row=29, column=1, columnspan=10, sticky="w")

    k = resize_img(800, u + "/result_pi.png")
    mg = Label(tit_frame3, image=k)
    mg.image = k
    mg.grid(row=30, column=2, columnspan=5, sticky="nsew")

    Title = Label(tit_frame3, text="Percentage of Wins, Draws and Losses as White and Black :",
                  font=("Arial", 18, "underline", "bold"),
                  padx=20, pady=20)

    Title.grid(padx=0, pady=(20, 0), row=31, column=1, columnspan=6, sticky="w")

    intro_text = "These are the donut plots of the percentage of wins, draws and losses. Left side is where the user played as White,\nright side figure is when the user played as Black.\n"

    Title = Label(tit_frame3, text=intro_text, font=("Arial", 18), padx=20, pady=20, anchor="e", justify=LEFT)
    Title.grid(padx=(60, 0), pady=0, row=32, column=1, columnspan=10, sticky="w")

    k = resize_img(500, u + "/result_as_wh.png")
    mg = Label(tit_frame3, image=k)
    mg.image = k
    mg.grid(row=33, column=2, columnspan=3, sticky="nsew", padx=(0, 0))

    k = resize_img(500, u + "/result_as_bl.png")
    mg = Label(tit_frame3, image=k)
    mg.image = k
    mg.grid(row=33, column=5, columnspan=3, sticky="nsew", padx=(0, 0))

    Title = Label(tit_frame3, text="Result of Top 5 Openings as White :",
                  font=("Arial", 18, "underline", "bold"),
                  padx=20, pady=20)
    Title.grid(padx=0, pady=(20, 0), row=34, column=1, columnspan=6, sticky="w")

    intro_text = "These graphs are very important for Strength / Weakness Analysis. Longer Red bar indicates the opening played by\n the user the most, but also loses the most. Longest green bar indicates the strongest most played opening. \n"

    Title = Label(tit_frame3, text=intro_text, font=("Arial", 18), padx=20, pady=20, anchor="e", justify=LEFT)
    Title.grid(padx=(60, 0), pady=0, row=35, column=1, columnspan=10, sticky="w")

    k = resize_img(1100, u + "/result_top_5_wh.png")
    mg = Label(tit_frame3, image=k)
    mg.image = k
    mg.grid(row=36, column=1, columnspan=7, sticky="nsew")

    Title = Label(tit_frame3, text="Result of Top 5 Openings as Black :",
                  font=("Arial", 18, "underline", "bold"),
                  padx=20, pady=20)
    Title.grid(padx=0, pady=(20, 0), row=37, column=1, columnspan=6, sticky="w")

    intro_text = "These graphs indicate the Strength / Weakness Analysis for the defences played by the user as Black. \n"

    Title = Label(tit_frame3, text=intro_text, font=("Arial", 18), padx=20, pady=20, anchor="e", justify=LEFT)
    Title.grid(padx=(60, 0), pady=0, row=38, column=1, columnspan=10, sticky="w")

    k = resize_img(1100, u + "/result_top_5_bl.png")
    mg = Label(tit_frame3, image=k)
    mg.image = k
    mg.grid(row=39, column=1, columnspan=7, sticky="nsew")

    Label(tit_frame3, text="\n\n\n\n\n\n\n").grid(row=40, column=0, columnspan=10, sticky="nsew")


#############################################################
# Game Prediction Tab

frame4 = Frame(tab4)
frame4.pack(fill="both", expand=True)

# Scroll Bar Implementation

my_canvas4 = Canvas(frame4)
my_canvas4.pack(side=LEFT, fill=BOTH, expand=True)
my_scrollbar4 = ttk.Scrollbar(frame4, orient=VERTICAL, command=my_canvas4.yview)
my_scrollbar4.pack(side=RIGHT, fill=Y)
my_canvas4.configure(yscrollcommand=my_scrollbar4.set)
my_canvas4.bind('<Configure>', lambda e: my_canvas4.configure(scrollregion=my_canvas4.bbox("all")))
second_frame4 = Frame(my_canvas4)
my_canvas4.create_window((0, 0), window=second_frame4, anchor="nw", width=1517)

f4 = Frame(second_frame4)
f4.pack(fill="both", pady=10, expand=True)

tit_frame4 = Frame(f4)
tit_frame4.pack(fill="x")

assign_grid(tit_frame4, 9)

pz4 = resize_img(50, "img_files/chess.png")

Label(tit_frame4, image=pz4).grid(row=0, column=2, sticky="e", padx=0)

Title = Label(tit_frame4, text="Game Prediction", font=("Arial", 25), padx=40, pady=20, borderwidth=5, relief="sunken")
Title.grid(padx=20, pady=20, row=0, column=2, columnspan=5)

Label(tit_frame4, image=pz4).grid(row=0, column=6, sticky="w")

Title = Label(tit_frame4, text="Enter your username :", font=("Arial", 22, "bold"), padx=20, pady=20)
Title.grid(padx=0, pady=(20, 0), row=1, column=1, columnspan=6, sticky="w")

username_input_own = Entry(tit_frame4, width=30, borderwidth=3, font=("Arial", 15))
username_input_own.insert(0, 'your_username')
username_input_own.grid(row=2, column=4, padx=(5, 0), pady=(25, 0), ipady=8)

Title = Label(tit_frame4, text="Enter your opponent's username :", font=("Arial", 22, "bold"), padx=20, pady=20)
Title.grid(padx=0, pady=(20, 0), row=3, column=1, columnspan=6, sticky="w")

username_input_opp = Entry(tit_frame4, width=30, borderwidth=3, font=("Arial", 15))
username_input_opp.insert(0, 'opponents_username')
username_input_opp.grid(row=4, column=4, padx=(5, 0), pady=(25, 0), ipady=8)


def tut_click():
    from tkinter import messagebox
    u1 = username_input_own.get()
    u2 = username_input_opp.get()
    messagebox.showinfo("Loading", "Building Logistic Regression Classifier Model, Please Wait.")
    import prediction as pred
    di = pred.predict(u1, u2)
    messagebox.showinfo("Completed", "Analysis Complete.")

    t1 = "Your Rating : " + str(di["user_rating"])

    Title = Label(tit_frame4, text=t1, font=("Arial", 18), padx=20, pady=20)
    Title.grid(padx=0, pady=(20, 0), row=8, column=3, columnspan=3)

    t1 = "Your Opponent's Rating : " + str(di["opp_rating"])

    Title = Label(tit_frame4, text=t1, font=("Arial", 18), padx=20, pady=20)
    Title.grid(padx=0, pady=(20, 0), row=9, column=3, columnspan=3)

    t1 = "Rating Difference : " + str(di["rating_diff"])

    Title = Label(tit_frame4, text=t1, font=("Arial", 18), padx=20, pady=20)
    Title.grid(padx=0, pady=(20, 0), row=10, column=3, columnspan=3)

    t1 = di["summ1"]

    Title = Label(tit_frame4, text=t1, font=("Arial", 18), padx=20, pady=20)
    Title.grid(padx=0, pady=(20, 0), row=11, column=3, columnspan=3)

    t1 = di["ord_acc"]

    Title = Label(tit_frame4, text=t1, font=("Arial", 18), padx=20, pady=20)
    Title.grid(padx=0, pady=(20, 0), row=12, column=3, columnspan=3)

    t1 = di["cat_acc"]

    Title = Label(tit_frame4, text=t1, font=("Arial", 18), padx=20, pady=20)
    Title.grid(padx=0, pady=(20, 0), row=13, column=3, columnspan=3)

    # Label(tit_frame4, text="").grid(row=14)

    t1 = di["result"]

    Title = Label(tit_frame4, text=t1, font=("Arial", 18), padx=40, pady=40, borderwidth=5, relief=GROOVE)
    Title.grid(padx=0, pady=(20, 0), row=15, column=3, columnspan=3)


Label(tit_frame4, text="").grid(row=6)

Tutorial_bttn = Button(tit_frame4, text="Request Analysis", font=("Arial", 15), padx=20, pady=8, command=tut_click)
Tutorial_bttn.grid(row=7, column=4, sticky="ns", pady=(30, 0))

for x in range(8, 23):
    Label(tit_frame4, text=" \n\n\n\n\n").grid(row=x)

#############################################################
# About

frame5 = Frame(tab5)
frame5.pack(fill="both", expand=True)

# Scroll Bar Implementation

my_canvas5 = Canvas(frame5)
my_canvas5.pack(side=LEFT, fill=BOTH, expand=True)
my_scrollbar5 = ttk.Scrollbar(frame5, orient=VERTICAL, command=my_canvas5.yview)
my_scrollbar5.pack(side=RIGHT, fill=Y)
my_canvas5.configure(yscrollcommand=my_scrollbar5.set)
my_canvas5.bind('<Configure>', lambda e: my_canvas5.configure(scrollregion=my_canvas5.bbox("all")))
second_frame5 = Frame(my_canvas5)
my_canvas5.create_window((0, 0), window=second_frame5, anchor="nw", width=1517)

f5 = Frame(second_frame5)
f5.pack(fill="both", pady=10, expand=True)

tit_frame5 = Frame(f5)
tit_frame5.pack(fill="x")

assign_grid(tit_frame5, 9)

pz5 = resize_img(50, "img_files/chess.png")

Label(tit_frame5, image=pz5).grid(row=0, column=3, sticky="e", padx=0)

Title = Label(tit_frame5, text="About", font=("Arial", 25), padx=40, pady=20, borderwidth=5, relief="sunken")
Title.grid(padx=600, pady=20, row=0, column=2, columnspan=5)

Label(tit_frame5, image=pz5).grid(row=0, column=5, sticky="w")

quote = "“I don’t believe in psychology. I believe in good moves.” \n\n                                                 - Robert James Fischer"

Title = Label(tit_frame5, text=quote, font=("Arial", 15, "italic"), padx=40, pady=20, borderwidth=1, relief=GROOVE)
Title.grid(padx=20, pady=20, row=1, column=4, columnspan=1, sticky="nsew")

Label(tit_frame5, text="\nThis software was written by :\n", font=("Arial", 18, "underline")).grid(row=2, column=4,
                                                                                                   columnspan=1)

Label(tit_frame5, text="Yogen Ghodke", borderwidth=1, font=("Arial", 18, "bold"),
      relief=GROOVE, pady=20, padx=20).grid(row=3, column=4, columnspan=1)

Label(tit_frame5, text="\nSpecial Thanks to :", borderwidth=5, font=("Arial", 18, "underline")).grid(row=4, column=4,
                                                                                                     columnspan=1)
Label(tit_frame5, text="\nFreeCodeCamp,   Corey Schaffer", borderwidth=5, font=("Arial", 18, "bold")).grid(row=5,
                                                                                                                 column=4,
                                                                                                                 columnspan=1)
Label(tit_frame5, text="\n(YouTubers)", borderwidth=5, font=("Arial", 18, "bold")).grid(row=6,
                                                                                                             column=4,
                                                                                                             columnspan=1)

#############################################################


root.mainloop()
