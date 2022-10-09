lista = [["1", "Mikel", "infor"], ["2", "Fernando", "administracion"], ["3", "Juan", "comercio"]]

print(lista)
lista = sorted(lista, key = lambda  x:x[2]) #iterable, iteable, clave
print(lista)