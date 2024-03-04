import pandas as pd

if __name__ == '__main__':
    df = pd.read_csv('TaigiDatabase.csv')

    df['Hanji'] = pd.Categorical(df.Hanji, categories=df["Hanji"].unique().tolist(), ordered=True)
    df['TL'] = pd.Categorical(df.TL, ordered=True)
    df.sort_values(["Hanji","TL"], inplace=True)

    #drop duplicates, case insensitive
    df['Hanji'] = df['Hanji'].str.lower()
    df['TL'] = df['TL'].str.lower()
    df.drop_duplicates(inplace=True)
    
    df.to_csv('TaigiDatabase.csv',index=False,encoding='utf-8-sig')