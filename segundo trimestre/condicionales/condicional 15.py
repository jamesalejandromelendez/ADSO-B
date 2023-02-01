año=int(input('Digite el año: '))

A= año % 19
B= año % 4
C= año % 7
D= (19*A+24) % 30
E= (2*B+4*C+6*D+5) % 7
N= (22+D+E)

if N>31:
    print('el domingo de pascua sera el dia', N-31, 'de abril')
else:
    print('el domingo de pascua sera el dia', N, 'de marzo')