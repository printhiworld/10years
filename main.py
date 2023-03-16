def alphabetic(s):
    '''if len(s) == 1:
        return True'''
    a = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(len(s)-1):
        for j in range(1,len(s)):
            if a.index(s[i]) > a.index(s[j]):
                return s
    return True

print(alphabetic('cell'))