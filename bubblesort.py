# Bubble sort
# Ordinamento degli elementi di una lista, perfetto per valori sia nimerici che alfanumerici
def sort(lista):
    for cicli in range(len(lista)-1, 0, -1):
        for riga in range(cicli):
            if lista[riga] > lista[riga + 1]:
                lista[riga], lista[riga + 1] = lista[riga + 1], lista[riga]

#miaLista=[23, 5, 78, 1211, 3, 56, 78, 12, 4, 51, 4096, 255]
miaLista=["Simone", "Piera", "Carlo", "Susanna", "Marina", "Giulia", "Clio", "Savera", "Gemma", "Laura", "Claudio", "Sergio", "Marco"]
sort(miaLista)
print(miaLista)
