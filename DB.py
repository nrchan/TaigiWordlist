from phingImConvert import *
import itertools
import pandas as pd

def exhaust(s):
    numify = PhingImtoNUM(s)
    splitted = toneSeperation(numify)

    seperator = []
    for i in range(len(splitted)):
        if all(c in "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" for c in splitted[i]):
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
            amount *= 3
        else:
            amount *= len(splitted[i])

    # If the amount is less than 16000, we can accept all possible combinations.
    if amount < 16000:
        splitted_provide = []
        for i in range(len(splitted)):
            splitted_provide.append([])
            if seperator[i]:
                splitted_provide[i].append("")
                if splitted[i] != " ":
                    splitted_provide[i].append(" ")
                if splitted[i] != "-":
                    splitted_provide[i].append("-")
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
    #read all words from the file
    with open("TaigiDatabase.csv") as f:
        db = pd.read_csv(f)

    #add new column for POJ
    db["POJ"] = db["TL"].apply(TLtoPOJ)
    #add stringified words to the database as new column named "possible_input_TL"
    db["possible_input_TL"] = db["TL"].apply(stringify)
    #add stringified words to the database as new column named "possible_input_POJ"
    db["possible_input_POJ"] = db["POJ"].apply(stringify)
    #add new column named "frequency", initialize it to 0 since we don't have any frequency data
    db["frequency"] = 0

    #save the database
    db.to_csv("TaigiInputDatabase.csv", index = False)