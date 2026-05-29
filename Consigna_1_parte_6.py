A = {101, 102, 103, 104, 105, 106}
B = {104, 105, 106, 107, 108}
C = {102, 105, 109}

todos = A | B | C

criticos = []
no_criticos = []

for usuario in todos:
    
    p = usuario in A
    q = usuario in B
    r = usuario in C
    
    if (p or q) and r:
        criticos.append(usuario)
    else:
        no_criticos.append(usuario)

print("Usuarios críticos: ", criticos)
print("Usuarios no críticos: ", no_criticos)
