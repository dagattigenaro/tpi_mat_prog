x = [0,5,10,15,20,25,30,40,50]

A = []
B = []
C = []

for i in range(len(x)):

    a = 40*x[i] + 200
    b = 70*x[i] + 50
    c = -2*(x[i]**2) + 80*x[i] + 100

    A.append(a)
    B.append(b)
    C.append(c)
for i in range(len(x)):

    print("x =",x[i])
    print("A =",A[i])
    print("B =",B[i])
    print("C =",C[i])
    print("-----------------")

horas = int(input("Ingrese cantidad de horas: "))

a = 40*horas + 200
b = 70*horas + 50
c = -2*(horas**2) + 80*horas + 100

if a <= b and a <= c:
    print("Plan más económico: A")
    print("Costo:",a)
elif b <= a and b <= c:
    print("Plan más económico: B")
    print("Costo:",b)
else:
    print("Plan más económico: C")
    print("Costo:",c)