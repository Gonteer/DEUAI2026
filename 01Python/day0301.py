import random

lotto = set()

while len(lotto) < 6 :

    lotto.add(random.randint(1,46))

print('이번주 로또 예상 번호는',sorted(lotto),'입니다.')
