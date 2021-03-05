import requests
import get_data as gd


def predict(u1,u2):
    di = {}

    req = "https://api.chess.com/pub/player/" + u1 + "/stats"
    user_rating = requests.get(req).json()["chess_blitz"]["last"]["rating"]
    req = "https://api.chess.com/pub/player/" + u2 + "/stats"
    opp_rating = requests.get(req).json()["chess_blitz"]["last"]["rating"]

    di["user_rating"] = user_rating
    di["opp_rating"] = opp_rating


    diff = user_rating - opp_rating

    di["rating_diff"] = diff



    import statsmodels.api as sm
    import pandas as pd
    import numpy as np

    try:
        df = pd.read_csv(u1 + '/chess_dataset_adv.csv')
    except:
        gd.driver_fn(u1)
        df = pd.read_csv(u1 + '/chess_dataset_adv.csv')

    X = df['rating_difference']
    y = df['result_val_for_player']

    logit_model = sm.Logit(y, X)
    result = logit_model.fit()
    report = str(result.summary2())
    di["summ1"] = report
    print(result.summary2())

    from sklearn import metrics
    from sklearn.metrics import confusion_matrix
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LogisticRegression
    import mord as mrd

    x = df['rating_difference'].values
    y = df['result_val_for_player'].values

    # converts y from 0, 0.5 and 1 to 0, 1 and 2 as mord.LogisticIT only takes integer values
    y = y * 2
    y = y.astype(int)

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)
    x_train = x_train.reshape(-1, 1)
    x_test = x_test.reshape(-1, 1)

    ord_model = mrd.LogisticIT().fit(x_train, y_train)
    y_pred_ord = ord_model.predict(x_test)
    ord_accuracy = ord_model.score(x_test, y_test)
    ord_cfm = confusion_matrix(y_test, y_pred_ord)

    cat_model = LogisticRegression(solver='lbfgs', multi_class='multinomial').fit(x_train, y_train)
    y_pred_cat = cat_model.predict(x_test)
    cat_accuracy = cat_model.score(x_test, y_test)
    cat_cfm = confusion_matrix(y_test, y_pred_cat)

    # print('Accuracy of ordinal logistic regression classifier on test set: {:.2f}%  \n'.format(ord_accuracy * 100))

    # print(ord_cfm)
    # print(
    #     '\n Accuracy of categorical logistic regression classifier on test set: {:.2f}% \n'.format(cat_accuracy * 100))
    # print(cat_cfm)

    di["ord_acc"] = 'Accuracy of ordinal logistic regression classifier on test set: {:.2f}%  \n'.format(ord_accuracy * 100)
    di["cat_acc"] = 'Accuracy of categorical logistic regression classifier on test set: {:.2f}% \n'.format(cat_accuracy * 100)

    diff = np.array([diff]).reshape(1, -1)
    result = ord_model.predict_proba(diff)
    result = result[0]
    user_win_prob = result[2] * 100

    if 0 <= user_win_prob < 40:
        result = 'Loss'
    elif 40 <= user_win_prob < 60:
        result = 'Draw'
    elif 60 <= user_win_prob <= 100:
        result = 'Win'
    else:
        result = 'error'

    di["result"] = f'Result: {result} \n\n Your winning probability against the opponent : {user_win_prob :.2f} %'

    # print(f'Result: {result} \n'
    #       f'Your winning probability against opponent : {user_win_prob :.2f} %')

    return di




#k1 = predict("tyrange","sudesh2911")
#print(k1)