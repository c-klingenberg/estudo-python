def mysplit(strng):

# Lista que será o output da função
    output = []
    word = ''

# Percorrer a string em busca de elementos que não sejam um espaço
    for ch in strng:
        if not ch.isspace():
# Concatenar elementos da string que se encontram entre espaços 
            word = word + ch
# Toda vez que chegar a um espaço, vírgula ou ponto final, tornar a concatenação em um novo elemento de output
# Como incluir a última palavra sem precisar ter um espaço, vírgula etc no final?
        elif word != '':
            output.append(word)
            word = ''

    return output
            


print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
