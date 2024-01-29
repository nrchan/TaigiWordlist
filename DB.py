from phingImConvert import *
import itertools
import pandas as pd
import numpy as np
import csv_to_sqlite 
import sys
import csv

temp = []

def exhaust(s):
    splitted = PhingImtoNUM(s)

    #change "ⁿ" to "N" and "o͘" to "ou"
    for i in range(len(splitted)):
        splitted[i] = splitted[i].replace("ⁿ", "N")
        splitted[i] = splitted[i].replace("o͘", "ou")

    seperator = []
    for i in range(len(splitted)):
        if all(c in "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZÁÉÍÓÚḾŃáéíóúḿńÀÈÌÒÙM̀Ǹàèìòùm̀ǹÂÊÎÔÛM̂N̂âêîôûm̂n̂ǍĚǏǑǓM̌Ňǎěǐǒǔm̌ňĀĒĪŌŪM̄N̄āēīōūm̄n̄A̍E̍I̍O̍U̍M̍N̍a̍e̍i̍o̍u̍m̍n̍A̋E̋I̋ŐŰM̋N̋a̋e̋i̋őűm̋n̋o͘ⁿ" for c in splitted[i]):
            seperator.append(False)
        else:
            seperator.append(True)

    # We have n splits, every split can provide 1 to (lenght of split) characters, which should always start from the first character of the split with no skip.
    # For exmaple, "abc" can provide 1, 2, 3 characters, which are "a", "ab", "abc".
    # Then, we want to get all possible combinations of these splits.
    # For example, "abc", "def" can both provide 3 splits, which are "a", "ab", "abc", "d", "de", "def".
    # The combinations of these splits are:
    #     "a", "d"
    #     "a", "de"
    #     "a", "def"
    #     "ab", "d"
    #     "ab", "de"
    #     "ab", "def"
    #     "abc", "d"
    #     "abc", "de"
    #     "abc", "def"
    # If the split is a seperator, we can accept it provide from zero characters or a space. That is, if "abc" is a seperator, it can provide "", " ", "a", "ab", "abc".
            
    # We calculate the amount of possible combinations of these splits first.
    amount = 1
    for i in range(len(splitted)):
        if seperator[i]:
            amount *= 1
        else:
            amount *= len(splitted[i])

    temp.append(amount)

    # If the amount is less than a certain number, we can accept all possible combinations.
    if amount < 20000:
        splitted_provide = []
        for i in range(len(splitted)):
            splitted_provide.append([])
            if seperator[i]:
                splitted_provide[i].append("")
                # if splitted[i] != " ":
                #     splitted_provide[i].append(" ")
                # if splitted[i] != "-":
                #     splitted_provide[i].append("-")
            else:
                for j in range(len(splitted[i])):
                    splitted_provide[i].append(splitted[i][:j+1])

        # Now, we have all possible combinations of these splits. We can use itertools.product to get all possible combinations of these combinations.
        combinations = list(itertools.product(*splitted_provide))

        # Finally, we can join these combinations to get all possible results. We will use a one-liner here to test copilot's abiblity
        joined_combination = ["".join(combination) for combination in combinations]
    
    #Otherwise, we only provide the full string, the full string without tone number, and the first character of each split. (with space, with dash, and without space)
    else:
        joined_combination = ["".join(splitted)]
        joined_combination.append("".join([s for i, s in enumerate(splitted) if not seperator[i]]))
        joined_combination.append(" ".join([s for i, s in enumerate(splitted) if not seperator[i]]))
        joined_combination.append("-".join([s for i, s in enumerate(splitted) if not seperator[i]]))
        joined_combination.append("".join(splitted).translate(str.maketrans('', '', '0123456789')))
        joined_combination.append("".join([s for i, s in enumerate(splitted) if not seperator[i]]).translate(str.maketrans('', '', '0123456789')))
        joined_combination.append("".join([s for i, s in enumerate(splitted) if not seperator[i]]).translate(str.maketrans('', '', '0123456789')))
        first_characters = []
        for i in range(len(splitted)):
            if not seperator[i]:
                first_characters.append(splitted[i][0])
        joined_combination.append("".join(first_characters))
        joined_combination.append(" ".join(first_characters))
        joined_combination.append("-".join(first_characters))

    # Remove empty string and space and duplicatation
    joined_combination = list(set(filter(lambda x: x != "" and x != " ", joined_combination)))
    
    return joined_combination

def stringify(s):
    possible_input = exhaust(s)
    return "$" + "$".join(possible_input) + "$"

if __name__ == "__main__":
    # read all words from the file
    with open("TaigiDatabase.csv") as f:
        db = pd.read_csv(f)

    #add corpus here!
    with open("教育部例句俗諺.csv") as f:
        corpus = f.read()
    with open("台華新聞漢字.txt") as f:
        corpus += f.read()
    with open("閱讀閩客.csv") as f:
        corpus += f.read()
    corpus = corpus.replace(" ", "")

    #add new column for POJ
    db["POJ"] = db["TL"].apply(TLtoPOJ)
    #add stringified words to the database as new column named "possible_input_TL"
    db["possible_input_TL"] = db["TL"].apply(stringify)
    #add stringified words to the database as new column named "possible_input_POJ"
    db["possible_input_POJ"] = db["POJ"].apply(stringify)
    #add new column named "frequency"
    db["frequency"] = db["Hanji"].apply(lambda x: corpus.count(x))
    #add new column named "user_frequency", initialize it to 0 since we don't have any frequency data
    db["user_frequency"] = 0

    #save the database
    db.to_csv("TaigiInputDatabase.csv", index = False)

    options = csv_to_sqlite.CsvOptions(typing_style="full", encoding="utf-8")
    csv.field_size_limit(sys.maxsize)
    csv_to_sqlite.write_csv(["TaigiInputDatabase.csv"], "TaigiWord.sqlite", options)

    print(np.quantile(temp, 0.5))
    print(np.quantile(temp, 0.6))
    print(np.quantile(temp, 0.7))
    print(np.quantile(temp, 0.8))
    print(np.quantile(temp, 0.9))
    print(np.quantile(temp, 0.95))
    print(np.quantile(temp, 0.99))
    print(np.quantile(temp, 0.999))
    print(np.quantile(temp, 1.0))
