import pandas as pd

df = pd.read_csv('./nato.csv')

dict_nato = {val.letter: val.code for(key, val) in df.iterrows()}

while True:

    input_word = input("Enter a word : ")
    input_word = input_word.upper()

    list_nato = [dict_nato[i] for i in input_word]
    print(list_nato)
    print('\n')
