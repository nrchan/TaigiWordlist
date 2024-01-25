from phingImConvert import *
import itertools

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
            
    splitted_provide = []
    for i in range(len(splitted)):
        splitted_provide.append([])
        if seperator[i]:
            splitted_provide[i].append("")
            splitted_provide[i].append(" ")
        for j in range(len(splitted[i])):
            splitted_provide[i].append(splitted[i][:j+1])

    # Now, we have all possible combinations of these splits. We can use itertools.product to get all possible combinations of these combinations.
    combinations = list(itertools.product(*splitted_provide))

    # Finally, we can join these combinations to get all possible results. We will use a one-liner here to test copilot's abiblity
    joined_combination = ["".join(combination) for combination in combinations]
    # Remove empty string and space and duplicatation
    joined_combination = list(set(filter(lambda x: x != "" and x != " ", joined_combination)))
    
    return joined_combination

if __name__ == "__main__":
    possible_input = exhaust("Tsi̍t-ê")

    stringify = "$" + "$".join(possible_input) + "$"
    print(stringify)