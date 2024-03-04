import pandas as pd

if __name__ == '__main__':
    df = pd.read_csv('TaigiDatabase.csv')

    #make sure every single character in hanji has an entry
    character = set()
    for hanji in df['Hanji']:
        for char in hanji:
            character.add(char)
    for char in character:
        if char not in df['Hanji'].values:
            print(char)