import random


def choose_secret(nombre_fichero):
    """Dado un nombre de fichero, esta funciÃ³n devuelve una palabra aleatoria de este fichero transformada a mayÃºsculas.
    Args:
      filename: El nombre del fichero. Ej. "palabras_reduced.txt"
    Returns:
      secret: Palabra elegida aleatoriamente del fichero transformada a mayÃºsculas. Ej. "CREMA"
    """
    lista = []
    f = open(nombre_fichero, mode="rt", encoding="utf-8")
    linea = f.readline()
    lista.append(linea)
    while linea != "" :
      linea = f.readline()
      lista.append(linea)
    f.close()
    rand=random.randint(1,30)
    secret=lista[rand]
    return secret.upper()
def compare_words(word, secret):
    """Dadas dos palabras en mayÃºsculas (word y secret), esta funciÃ³n calcula las posiciones de las letras de word que aparecen en la misma posiciÃ³n en secret, y las posiciones de las letras de word que aparecen en secret pero en una posiciÃ³n distinta.
    Args:
      word: Una palabra. Ej. "CAMPO"
      secret: Una palabra. Ej. "CREMA"
    Returns:
      same_position: Lista de posiciones de word cuyas letras coinciden en la misma posiciÃ³n en secret. En el caso anterior: [0]
      same_letter: Lista de posiciones de word cuyas letras estÃ¡n en secret pero en posiciones distintas. En el caso anterior: [1,2]
    """
    listaWord=[]
    listaSecret=[]
    same_position=[]
    same_letter=[]
    for char in p1:
      listaWord.append(char)
    for char in p2:
      listaSecret.append(char)
    for i in range(len(listaWord)):
      if(listaWord[i]==listaSecret[i]):
        same_position.append(i)
    for i in range(len(listaWord)):
      for j in range(len(listaSecret)):
        if(listaWord[i]==listaSecret[j] and i not in same_position):
          same_letter.append(i)
    return same_position, same_letter
def print_word(word, same_position, same_letter):
    """Dada una palabra, una lista same_position y otra lista same_letter, esta funciÃ³n crearÃ¡ un string donde aparezcan en mayÃºsculas las letras de la palabra que ocupen las posiciones de same_position, en minÃºsculas las letras de la palabra que ocupen las posiciones de same_letter y un guiÃ³n (-) en el resto de posiciones
    Args:
      word: Una palabra. Ej. "CAMPO"
      same_position: Lista de posiciones. Ej. [0]
      same_letter: Lista de posiciones. Ej. [1,2]
    Returns:
      transformed: La palabra aplicando las transformaciones. En el caso anterior: "Cam--"
    """
    lista=["-","-","-","-","-"]
    res=""
    for pos in same_position:
      lista[pos]=word[pos]
    for pos in same_letter:
      lista[pos]=word[pos].lower()
    for char in lista:
      res+=char
    return res
def choose_secret_advanced(nombre_fichero):
    """Dado un nombre de fichero, esta funciÃ³n filtra solo las palabras de 5 letras que no tienen acentos (Ã¡,Ã©,Ã­,Ã³,Ãº). De estas palabras, la funciÃ³n devuelve una lista de 15 aleatorias no repetidas y una de estas 15, se selecciona aleatoriamente como palabra secret.
    Args:
      filename: El nombre del fichero. Ej. "palabras_extended.txt"
    Returns:
      selected: Lista de 15 palabras aleatorias no repetidas que tienen 5 letras y no tienen acentos
      secret: Palabra elegida aleatoriamente de la lista de 15 seleccionadas transformada a mayÃºsculas
    """
    lista = []
    sinAcentos=[]
    selected=[]
    acentos="áéíóú"
    isAcento=False
    f = open(nombre_fichero, mode="rt", encoding="utf-8")
    linea = f.readline()
    lista.append(linea)
    while linea != "" :
      linea = f.readline()
      lista.append(linea)
    f.close()
    for word in lista:
      isAcento=False
      for char in word:
        if(char in acentos):
            isAcento=True
      if(isAcento==False):
        sinAcentos.append(word)
    for i in range(1,16):
      rnd=random.randint(0,len(sinAcentos)-1)
      palabra=sinAcentos.pop(rnd)
      selected.append(palabra)
    rndIndex=random.randint(0,15)
    secret=selected[rndIndex]
    return selected, secret.upper()
def check_valid_word():
    """Dada una lista de palabras, esta funciÃ³n pregunta al usuario que introduzca una palabra hasta que introduzca una que estÃ© en la lista. Esta palabra es la que devolverÃ¡ la funciÃ³n.
    Args:
      selected: Lista de palabras.
    Returns:
      word: Palabra introducida por el usuario que estÃ¡ en la lista.
    """

if __name__ == "__main__":
    secret=choose_secret("palabras_reduced.txt")
    print("Palabra a adivinar: "+secret)#Debug: esto es para que sepas la palabra que debes adivinar
    for repeticiones in range(0,6):
        word = input("Introduce una nueva palabra: ")
        same_position, same_letter = compare_words(word, secret)
        resultado=print_word(word, same_position, same_letter)
        print(resultado)
        if word == secret:
            print("HAS GANADO!!")
            exit()
    print("LO SIENTO, NO LA HAS ADIVINIDADO. LA PALABRA ERA "+secret)   

