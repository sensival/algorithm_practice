# 주어진 수들을 활용해서 M번 더하는 문제 같은수는 연속 K번을 초과하여 나올수 없음. 
# 2,4,5,4,6으로 이루어진 배열이 있을때 M이 8이고 K가 3이라고 가정했을때 6+6+6+5+6+6+6+5=46
# M을 K+1로 나눈 몫이 수열(6+6+6+5)의 반복횟수
# 가장 큰수가 더해지는 횟수 int(M/(k+1))*K + M%(K+1)


# 교재 풀이
n,m,k=map(int, input().split())
data=list(map(int, input().split()))

data.sort()
first=data[n-1] #가장큰수
second=data[n-2] #두번째로 큰수, 세번째로 큰 수는 필요없음. 어차피 두번째로 큰 수 더하면 다음 항에 가장 큰 수 쓸 수 있음

count=int(m/(k+1))*k
count+=m%(k+1)

result=0
result += count*first
result += (m-count)*second

print(result)