import math
Ax = float(input())
Ay = float(input())
Bx = float(input())
By = float(input())
def distancia_pontos(Ax,Ay,Bx,By):
    dAB=math.sqrt(((Bx-Ax)**2) +((By-Ay)**2))
    return dAB
print("%.2f"%distancia_pontos(Ax,Ay,Bx,By))