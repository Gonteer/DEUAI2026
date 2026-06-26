def mm (v1, v2) :

    if v1 > v2 :
        return v1, v2
    else :
        return v2, v1


a1 = input('첫번째 값 :')
a2 = input('두번째 값 :')

r1, r2 = mm(a1,a2)
print(r1,r2)
