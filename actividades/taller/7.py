def palabras():
    vocales = ['a','e','i','o','u']
    consonantes = ['b','c','d','f','g','h','j','k','m','n','l','ñ','p','q','r','s','t','v','x','z','w','y']
    tilde = ['à','è','ì','ò','ù']
    v,c,t,e = 0,0,0,0
    for i in x:
        if i in vocales:
            v += 1
        elif i in consonantes:
            c += 1
        elif i in tilde:
            t += 1
        else :
            e += 1
    print('cuenta con \n',v,'vocales\n',c,'consonantes\n',t,'vocales con tilde\n',e,'caracteres especiales ')

x = input('escribe una cadena: ') 
palabras()