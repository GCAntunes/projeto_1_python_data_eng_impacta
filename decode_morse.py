'''
O Código Morse é um sistema de representação de letras, algarismos e sinais de pontuação através
de um sinal codificado enviado de modo intermitente. Foi desenvolvido por Samuel Morse em 1837, 
criador do telégrafo elétrico, dispositivo que utiliza correntes elétricas para controlar eletroímãs 
que atuam na emissão e na recepção de sinais. 
O script tem a finalidade de decifrar uma mensagem em código morse e salvá-la em texto claro.
'''

import os
import sys
import datetime
import pandas as pd
from config import file_path, dict_morse

def decode_morse(msg):
    '''
    input : mensagem em código morse com as letras separadas por espaços
    output : palavra escrito em letras e algarismos
    '''
    msg_lstp = msg.split("  ")
    msg_lst = [msg_lsta.split(" ") for msg_lsta in msg_lstp]
    msg_claro = []
    print(msg_lst)
    for word in msg_lst:
        for letter in word:
            msg_claro.append(dict_morse[letter])
        msg_claro.append(" ")
    return "".join(msg_claro)
def save_clear_msg_csv_hdr(msg_claro):
    '''
    input : mensagem em texto claro
    output : palavra escrito em letras e algarismos, salva em arquivo csv
    '''
    now = datetime.datetime.now()
    df = pd.DataFrame([[msg_claro, now]], columns=["mensagem", "datetime"])
    hdr = not os.path.exists(file_path)
    df.to_csv(file_path, mode ="a", index = False, header=hdr)

if __name__ == "__main__":
    frases = []
    f = open("frases.txt", "r")
    for frase in f:
        frases.append(frase.strip())
    f.close()
    for frase in frases:
        msg_claro = decode_morse(frase)
        save_clear_msg_csv_hdr(msg_claro)
        print(msg_claro)
    #print(save_clear_msg_csv_hdr.__doc__)
    #print(pd.to_pickle.__doc__)

    