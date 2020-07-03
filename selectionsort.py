# Selection sort
# Ordinamento degli elementi di una lista, perfetto per valori sia nimerici che alfanumerici
# Più veloce del "bubble-sort" perchè fa meno cicli e meno operazioni di swap (scambio del valore fra due variabili)
def sort(lista):
    indAlto = len(lista) - 1
    for indBasso in range(0, indAlto):
        indValMin = indBasso
        for riga in range(indBasso, indAlto):
            if lista[riga + 1] < lista[indValMin]:
                indValMin = riga + 1
        #[DEBUG]# print(lista)
        lista[indBasso], lista[indValMin] = lista[indValMin], lista[indBasso]

#miaLista=[23, 5, 78, 1211, 3, 56, 78, 12, 4, 51, 4096, 255]
miaLista=["Simone", "Piera", "Carlo", "Susanna", "Marina", "Giulia", "Clio", "Savera", "Gemma", "Laura", "Claudio", "Sergio", "Marco"]

sort(miaLista)
print(miaLista)