#i = 1
#while i <= 100 :
#    if i % 2 == 0 :
#        print(i,end=' ')
#        
#    i = i + 1

#while True :
#    ans = input('종료하시겠습니까?(y/n)')
#    if ans == 'y':
#        break
#    print('다시 입력')
    
#print('프로그램 종료')

i = 0
ss = 0
while i <= 10 :

    i = i + 1
    if i % 2 == 0 :
        ss = ss + i
        continue

    print(i,'입니다')
    print('다음으로 넘어가용~')
    
print('1에서',i,'까지의 짝수 합은',ss,'입니다')
