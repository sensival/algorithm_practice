# 거슬러 줘야 할 동전 갯수 세기 

# 교재 풀이
n=int(input("거스름돈 입력(ex.1260):"))
count=0

coin_types=[500,100,50,10]

for coin in coin_types:
    count += n // coin
    n %= coin

print(count)