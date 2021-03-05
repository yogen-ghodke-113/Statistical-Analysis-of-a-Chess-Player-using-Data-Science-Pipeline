def visualize_data(username):
    import os
    os.system("python unt.py " + username)
    os.system("python heatmap1.py " + username)
    os.system("python heatmap2.py " + username)
    os.system("python heatmap3.py " + username)

# visualize_data("tyrange")
