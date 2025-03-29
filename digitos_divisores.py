C = 0
N = int(input("Ingrese un numero : \n"))
for i in str(N):
    d = int(i)
    if d != 0 and N % d == 0:
        C += 1

print(f"El numero {N} tiene estos divisores {C}")