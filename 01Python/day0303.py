def happ (v1, v2=100) :

    hap = 0
    for i in range(v1,v2+1) :
        hap += i

    #return hap
    print('두 수의 합은', hap, '입니다')


aa = happ(v2=1000,v1=10)
#print('두 수의 합은', aa, '입니다')
