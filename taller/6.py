def verbos():
    x = input('digita tu verbo: ')
    pasado = ['è','aste','ò','amòs','aron','ì','iste','iò','imos','ieron']
    presente = ['o','as','a','amos','an','en','emos','es','e','os']
    futuro = ['erè','eràs','erà','eremos','erèis','eràn']
    
    for i in presente:
        if x.endswith(i):
            print('estas realizando una accion en presente ')  
    for i in futuro:
        if x.endswith(i):
            print('estas realizando una accion en futuro')
    for i in pasado:
        if x.endswith(i):
            print('estas realizando una accion en pasado')
verbos()