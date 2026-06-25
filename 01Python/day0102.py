s1 = int(input('국어 성적?'))
s2 = int(input('영어 성적?'))
s3 = int(input('수학 성적?'))

to = s1 + s2 + s3 #합계
avg = to / 3

print('당신의 과목 합계 점수는', to, '점, 평균은',avg,'점 입니다.')
'''
if avg >= 70 :
    print('합격입니다')
    print('다음학기에 봅시다')
else :
    print('다음학기에 뵙겠습니다')
'''
print('당신은',end=' ')

if avg >= 90 :
    print('A',end='')
elif avg >= 80 :
    print('B',end='')
elif avg >= 70 :
    print('C',end='')
elif avg >= 60 :
    print('D',end='')
else :
    print('F',end='')

print('입니다')


