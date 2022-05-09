'''
1º: preço do combustível
2º: criar função para encontrar distâncias
3º: entrada das distâncias
4º: entrada das rotas
5º: >>> Importante // Revisar --- SOMATÓRIA DAS ROTAS
6º: Custo Total
'''

dists = [] # lista de distâncias
rotas = [] # lista de rotas


n = int(input())
for x in range(n):
    temp = []
    for y in range(n):
        if x == y:
            temp.append(0)
        elif x < y:
            temp.append(int(input()))
        elif x > y:
            temp.append(dists[y][x])
    dists.append(temp)



route = int(input()) # quantidade de rotas
cid_f = int(input())
rotas.append(cid_f)
for x in range(route-1):
    rotas.append(int(input()))

rotas.append(rotas[0])

#Valor do combustível
vd = float(input())

# Controle de somatória das rotas
somatoriaR = 0


for z in range(len(rotas) - 1):
    x = rotas[z]
    y = rotas[z+1]
    somatoriaR += dists[x - 1][y - 1]

# Custeio
print(f"R$ {(somatoriaR * vd)/3:.2f}")