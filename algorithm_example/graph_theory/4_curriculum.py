# N개의 강의를 듣고자 하고 각 강의마다 선행 과목이 있다. 모든 강의는 1번 부터 N번까지의 번호를 가진다. n개의 강의 정보가 주어졌을 때, n개의 과목을 수강하기까지 걸리는 최소 시간을 각각 구하시오
# 첫째 줄에 수강하고자하는 강의의 수가 주어진다. 다음 n개의 줄에는 각 강의들의 강의 시간과 선행 과목이 주어진다. 각줄의 끝은 -1로 끝난다.
# 입력 예시
# 5
# 10 -1
# 10 1 -1
# 4 1 -1
# 4 3 1 -1
# 3 3 -1

# 교재 풀이

from collections import deque
import copy

v = int(input())

indegree = [0] * (v + 1)

graph = [[] for i in range(v + 1)]

time = [0] * (v + 1)


for i in range(1, v + 1):
    data = list(map(int, input().split()))
    time[i] = data[0]
    for x in data[1:-1]:
        indegree[i] += 1
        graph[x].append(i)


def topology_sort():
    result = copy.deepcopy(time)
    q = deque()

    # 진입차수가 0인 차수 찾아 큐에 넣기
    for i in range(1, v+1):
        if indegree[i] == 0: 
            q.append(i)
        
    while q:
        # 큐에서 꺼내서 result로 넣음
        now = q.popleft()
        result.append(now) 

        # now와 연결된 간선 삭제
        for i in graph[now]:
            result[i] = max(result[i], result[now] + time[i])
            indegree[i] -= 1
            # 간선 삭제 했을때 차수 0이면 큐에 넣기
            if indegree[i] == 0:
                q.append(i)
        
    for i in range(1, v +1):
        print(result[i])


topology_sort()


