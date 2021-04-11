
import solucao_candidata
from typing import Final

# cria soluções
a=solucao_candidata.solucao_candidata()
a.f=[1,5]
a.nome="A"

b=solucao_candidata.solucao_candidata()
b.f=[2,3]
b.nome="B"

c=solucao_candidata.solucao_candidata()
c.f=[4,1]
c.nome="C"

d=solucao_candidata.solucao_candidata()
d.f=[1.5,4]
d.nome="D"


solucoes=[a,b,c,d]
solucoesaux:Final = [a,b,c,d]
vr = 0
# para cada individuo x distance = 0, e cálculo do tamanho
for x in solucoes:
    vr=vr+1
    x.distance=0

tamanho = vr 
m = 2



# distance de de um indivíduo a diferença entre seus dois vizinhos
for x in range(m):
    vetorcomp = []
    for item in solucoes:
        vetorcomp.append(item.f)
    # ordenar
    vetorcomp.sort(reverse=True)
    for z in range(len(vetorcomp)):
        for it in solucoesaux:
            if it.f[0] == vetorcomp[z][0] and it.f[1] == vetorcomp[z][1]:
                solucoes[z]=it

    # pontos extremos com valores de distance infinito
    solucoes[0].distance=float("inf")
    solucoes[len(solucoes)-1].distance=float("inf")
    y=1
    for y in range(len(solucoes)-1):
        aux = (solucoes[y+1].f[x] - solucoes[y-1].f[x])/(solucoes[tamanho-1].f[x]-solucoes[0].f[x])
        solucoes[y].distance = solucoes[y].distance + aux 
for x in solucoes:
    print(x.nome,x.distance,sep=" = ")
 