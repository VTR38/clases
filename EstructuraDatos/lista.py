lista = []

while True:

 elemento = input("Ingresa un elemento para agregar a la lista (o escribe 'fin' para detenerse): ")


 if elemento.lower() == 'fin':
   break


 lista.append(elemento)
 print("La lista resultante es:", lista)