import unicodedata

'''
        Fonction qui supprimes les accents
'''

def formalizeStr(str):
    return unicodedata.normalize('NFD', unicode(str,'utf-8')).encode('ascii', 'ignore').lower()