# N이 입력되면 00:00:00~N:59:59까지 3이 하나라도 포함되는 경우의 수를 구하는 프로그램
# 입력예시 5 출력 11475

# 나의 풀이
n=int(input())
count_3=0

for hr in range(n+1):
    for min in range(60):
        for sec in range(60):
            timestp=[hr,min,sec]
            timestp=map(str, timestp)
            timestp=''.join(timestp)
            if timestp.count('3') != 0:
                count_3 +=1

print(count_3)

# 교재 풀이
h=int(input())

count=0

for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i)+str(j)+str(k):
                count +=1

print(count)
