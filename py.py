
palavra = 'comprovações'
palavra = 'várias'
palavra = 'divertidamente'
palavra = 'corredor'
# palavra = 'correr'
removeVerb = False

# Precisa organizar sabagaça aqui eim mano hue


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
    if(palavra[tam-2:] == 'õe' or palavra[tam-2:] == 'ão'):
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
    if(palavra[-3:] == 'dor'):
        palavra = palavra[:-3]
        tam = len(palavra)
        return True
    return False

# Redução de Verbo


def VerbReduction():
    global palavra, tam
    if(any(palavra[-5:] == f for f in ['entar', 'ficar'])):
        palavra = palavra[:-5]
        tam = len(palavra)
        return True
    if(any(palavra[-4:] == f for f in ['izar'])):
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
    # Ainda precisa fazer essa parte
    print(palavra)


tam = len(palavra)
PluralReduction()
wordEndA = True if (palavra[tam - 1] == 'a') else False
if(wordEndA):
    feminineReduction()
AugmentativeReduction()
AdverbReduction()
if(not NounReduction()):
    if(not VerbReduction()):
        RemoveVowel()
RemoveAceents()
