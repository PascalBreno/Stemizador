palavra = input('Insira a palavra: ')


# Redução de Plural
def PluralReduction():
    global palavra, tam
    if(palavra[tam - 1] == 's'):
        palavra = palavra[:tam-1]
    tam = len(palavra)

# Redução de feminino


def feminineReduction():
    global palavra
    palavra = palavra[:-1] + 'o'

# Redução do Aumentativo


def AugmentativeReduction():
    global palavra, tam
    if(any(palavra[-6:] == f for f in ['zarrão', 'eirão'])):
        palavra = palavra[:-6]
        tam = len(palavra)

    if(any(palavra[-5:] == f for f in ['alhão', 'arrão', 'anzil', 'astro', 'alhaz', 'arraz'])):
        palavra = palavra[:-5]
        tam = len(palavra)

    if(any(palavra[-4:] == f for f in ['aréu', 'arra', 'orra', 'ázio'])):
        palavra = palavra[:-4]
        tam = len(palavra)

    if((any(palavra[-3:] == f for f in ['eia', 'aça', 'aço', 'uça', 'eio']))):
        palavra = palavra[:-3]
        tam = len(palavra)

    if((any(palavra[-2:] == f for f in ['ão', 'az', 'ei']))):
        palavra = palavra[:-2]
        tam = len(palavra)


# Redução de Advérbio

def AdverbReduction():
    global palavra, tam
    if(palavra[-5:] == 'mente'):
        palavra = palavra[:-5]
    tam = len(palavra)

# Redução de substativo


def NounReduction():
    global palavra, tam
    if(palavra[-4:] == 'edor'):
        palavra = palavra[:-4]
        tam = len(palavra)
        return True
    if(any(palavra[-3:] == f for f in ['dor', 'eia'])):
        palavra = palavra[:-3]
        tam = len(palavra)
        return True
    if(any(palavra[-2:] == f for f in ['ei', 'ão'])):
        palavra = palavra[:-2]
        tam = len(palavra)
        return True
    return False

# Redução de Verbo


def VerbReduction():
    global palavra, tam
    if(any(palavra[-5:] == f for f in ['entar', 'ficar', 'ilhar', 'inhar', 'iscar'])):
        palavra = palavra[:-5]
        tam = len(palavra)
        return True
    if(any(palavra[-4:] == f for f in ['izar', 'ejar', 'icar', 'itar'])):
        palavra = palavra[:-4]
        tam = len(palavra)
        return True
    if(any(palavra[-3:] == f for f in ['ear'])):
        palavra = palavra[:-3]
        tam = len(palavra)
        return True
    if(any(palavra[-2:] == f for f in ['ar', 'er', 'ir'])):
        palavra = palavra[:-2]
        tam = len(palavra)
        return True
    tam = len(palavra)
    return False


def RemoveVowel():
    global palavra, tam
    if(any(palavra[-1:] == f for f in ['a', 'e', 'i', 'o', 'u'])):
        palavra = palavra[:-1]
        tam = len(palavra)


def RemoveAceents():
    global palavra
    palavra = palavra.replace("á", "a")
    palavra = palavra.replace("à", "a")
    palavra = palavra.replace("ã", "a")
    palavra = palavra.replace("é", "e")
    palavra = palavra.replace("ê", "e")
    palavra = palavra.replace("í", "i")
    palavra = palavra.replace("ó", "o")
    palavra = palavra.replace("ô", "o")
    palavra = palavra.replace("ú", "u")
    print('Radical: ' + palavra)


tam = len(palavra)
PluralReduction()
wordEndA = True if (palavra[tam - 1] == 'a') else False
if(wordEndA):
    feminineReduction()
AugmentativeReduction()
AdverbReduction()
print(palavra)
if(not NounReduction()):
    if(not VerbReduction()):
        RemoveVowel()
RemoveAceents()
