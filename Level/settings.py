import random

piece_main = [
'X          ',
'X          ',
'X          ',
'X          ',
'X          ',
'X          ',
'X          ',
'X          ',
'X P   Z    ',
'XXXXXXXXXXX',
'XXXXXXXXXXX'
]

piece_1 = [
'           ',
'           ',
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
'           ',
'           ',
'           ',
'           ',
'           ',
'       X   ',
'           ',
'      Z    ',
'XXXXXXXXXXX',
'XXXXXXXXXXX',
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
'           ',
'           ',
' XXXX      ',
'           ',
'         X ',
'           ',
'       XX  ',
'           ',
'      Z    ',
'XXXXXXXXXXX',
'XXXXXXXXXXX',
]

piece_5 = [
'           ',
'           ',
'           ',
'           ',
'    Z      ',
'   XX      ', 
' XX        ', 
'XX         ', 
'XXXX     XX',
'XXXXXXX  XX',
'XXXXXXX  XX ', 
]

parede = [
'X',
'X',
'X',
'X',
'X',
'X',
'X',
'X',
'X',
'X',
'X',
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

        print(peca)

geradorPeca()

fase = [piece_1,piece_2, piece_3, piece_4, piece_5, parede]
for i in range(len(fase)):
    for a in range(len(fase[i])):
        piece_main[a] += fase[i][a]

tam_plataforma = 64
width = 1280
height = len(piece_main) * tam_plataforma
