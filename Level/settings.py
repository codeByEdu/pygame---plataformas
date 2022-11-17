import random
level_map = [
'                                                              ',
'                                                              ',
'                                                              ',
'        XXXX                                                  ',
'                          XXX                                 ',
'                 XX                                           ',
'               XX                  XX              XXXX       ',
'              XX                   XXXX                       ',
'  P   Z     XXXX     XX  XXXXX  XXXXXXX                       ',
'XXXXXXXXXX  XXXXXXX  XX  XXXXX  XXXXXXXXXXXXXXX  XXXXXXXXXXX  ',
'XXXXXXXXXX  XXXXXXX  XX  XXXXXX XXXXXXXXXXXXXXX  XXXXXXXXXXX  ']

piece_main = [
'           ',
'           ',
'           ',
'       XXXX',
'           ',
'           ',
'           ',
'           ',
'  P   Z    ',
'XXXXXXXXXXX',
'XXXXXXXXXXX']
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







piece_1 = [
'           ',
'           ',
'           ',
'           ',
'           ',
'        Z  ',
'       XXXX',
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
'       XXXX',
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
'       XXXX',
'           ',
'        Z  ',
'XXX    XXXX',
'XXX    XXXX',
]
piece_4 = [
'           ',
'           ',
'XXXXX      ',
'           ',
'         XX',
'           ',
'       XXXX',
'           ',
'      Z    ',
'XXXXXXXXXXX',
'XXXXXXXXXXX',
]
fase = [piece_1,piece_2, piece_3, piece_4, piece_5]
for i in range(0,3):
    for a in range(len(fase[i])):
        piece_main[a] += fase[i][a] 



tam_plataforma = 64
width = 1200
height = len(piece_main) * tam_plataforma
