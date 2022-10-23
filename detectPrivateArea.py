import unicodedata
import pandas as pd

def isPrivateArea(char):
    return unicodedata.category(char) == 'Co'

if __name__ == '__main__':
    list = pd.read_csv("TaigiDatabase.csv")

    for index, row in list.iterrows():
        entry = row["Hanji"]
        for c in entry:
            if isPrivateArea(c):
                print(index)
                break

"""
word changed:
𫝛
𰣻(疒哥)
𪜶
𫝏
𫝺
𫞼
𫝻
𫟂
𬦰(足百)
"""