class a:
    v=1
class b(a):
    pass  
o=b()
print(issubclass(b,a))