import random
import time

piece_main = [
'N          ',
'N          ',
'N          ',
'N          ',
'N          ',
'N          ',
'N          ',
'N          ',
'N P   Z    ',
'XXXXXXXXXXX',
'XXXXXXXXXXX'
]

piece_1 = [
'           ',
'  Z        ',
'           ',
'           ',
'           ',
'        Z  ',
'       XX  ',
'           ',
'           ',
'XXX    XXXX',
'XXX    XXXX',
]

piece_2 = [
'           ',
'    Z      ',
'           ',
'     Z     ',
'           ',
'           ',
'       X   ',
'           ',
'      Z    ',
'XXXX    XXX',
'XXXX    XXX',
]

piece_3 = [
'           ',
'           ',
'           ',
'           ',
' XXXX      ',
'           ',
'        X  ',
'           ',
'        Z  ',
'XXX    XXXX',
'XXX    XXXX',
]

piece_4 = [
'      Z    ',
'           ',
' XXXX      ',
'           ',
'   Z     X ',
'           ',
'       XX  ',
'           ',
'      Z    ',
'XZXXX  X  X',
'XXXXX  X  X',
]

piece_5 = [
'    Z      ',
'           ',
'        Z  ',
'           ',
'    Z      ',
'   XX      ', 
' XX        ', 
'XX      ZZ ', 
'XXXX       ',
'XXXXXXX    ',
'XXXXXXX  XX ', 
]

parede = [
'N',
'N',
'N',
'N',
'N',
'N',
'N',
'N',
'N',
'N',
'N',
]

pecas = [];

def geradorPeca():
    peca = [];

    piso = 'XXXXXXXXXXX'
    ceu = '           '
    zumbi = 'Z'
    bloco = 'X'

    for i in range(11):
        if(i < 4):
            peca.append(ceu)

        if(i >= 4 and i <= 9):
            parte = []
            for i in range(11):
                if(random.randint(0, 4) % 2 == 0):
                    parte.append(bloco)
                else:
                    parte.append(' ')

        if(i >= 10):
            peca.append(piso)

geradorPeca()

fase = [piece_1,piece_2, piece_3, piece_4, piece_5]

for i in range(30):
    ran = random.randint(0, fase.__len__() - 1)
    for a in range(len(fase[ran])):
        piece_main[a] += fase[ran][a]
piece_main += parede

# gerarZumbi = True
# def geraZumbi():
#     for i in range(fase.__len__()):
#         print(fase[i])
        
# geraZumbi()

tam_plataforma = 64
width = 1280
height = len(piece_main) * tam_plataforma
