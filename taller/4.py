def texto(x):
    print(
        x.capitalize(),'\n',
        x.center(20),'\n',
        x.lower(),'\n',
        x.lstrip(),'\n',
        x.split(),'\n',
        x.strip(),'\n',
        x.swapcase(),'\n',
        x.title(),'\n',
        x.upper() )
x = input('digita tu frace: ')
texto(x)