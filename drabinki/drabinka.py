import math

zawodnicy = {}
zawodnicy[1] = 'JanB'
zawodnicy[2] = 'BartekB'
zawodnicy[3] = 'TomekA'
zawodnicy[4] = 'TomekT'
zawodnicy[5] = 'AndrzejW'
zawodnicy[6] = 'PsikutaS'
zawodnicy[7] = 'LolekW'
zawodnicy[8] = 'MichałB'
zawodnicy[9] = 'RafałK'
zawodnicy[10] ='OlekE'
zawodnicy[11] = 'GrzesiekB'

lz = len(zawodnicy)
wykladnik = math.trunc(math.sqrt(lz))
a=0
tabPozostali = []
for i in range(0,lz+1):
    if(i > 2**wykladnik):
        tabPozostali.append(zawodnicy[i])
print(tabPozostali)




