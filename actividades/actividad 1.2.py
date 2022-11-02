for k in range (1, 501):
    for c in range (1, 501 ):
        x = k**2 + c**2
        for i in range (1, 501):
            h = i**2
            if x== h:
                print("ca=",k,"co=",c,"h=", i)