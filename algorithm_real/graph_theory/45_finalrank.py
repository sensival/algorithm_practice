# 문제
# 올해 ACM-ICPC 대전 인터넷 예선에는 총 n개의 팀이 참가했다. 팀은 1번부터 n번까지 번호가 매겨져 있다. 놀랍게도 올해 참가하는 팀은 작년에 참가했던 팀과 동일하다.
# 올해는 인터넷 예선 본부에서는 최종 순위를 발표하지 않기로 했다. 그 대신에 작년에 비해서 상대적인 순위가 바뀐 팀의 목록만 발표하려고 한다. (작년에는 순위를 발표했다) 
# 예를 들어, 작년에 팀 13이 팀 6 보다 순위가 높았는데, 올해 팀 6이 팀 13보다 순위가 높다면, (6, 13)을 발표할 것이다.
# 창영이는 이 정보만을 가지고 올해 최종 순위를 만들어보려고 한다. 작년 순위와 상대적인 순위가 바뀐 모든 팀의 목록이 주어졌을 때, 
# 올해 순위를 만드는 프로그램을 작성하시오. 하지만, 본부에서 발표한 정보를 가지고 확실한 올해 순위를 만들 수 없는 경우가 있을 수도 있고, 일관성이 없는 잘못된 정보일 수도 있다. 
# 이 두 경우도 모두 찾아내야 한다.

# 입력
# 첫째 줄에는 테스트 케이스의 개수가 주어진다. 테스트 케이스는 100개를 넘지 않는다. 각 테스트 케이스는 다음과 같이 이루어져 있다.

# 팀의 수 n을 포함하고 있는 한 줄. (2 ≤ n ≤ 500)
# n개의 정수 ti를 포함하고 있는 한 줄. (1 ≤ ti ≤ n) ti는 작년에 i등을 한 팀의 번호이다. 1등이 가장 성적이 높은 팀이다. 모든 ti는 서로 다르다.
# 상대적인 등수가 바뀐 쌍의 수 m (0 ≤ m ≤ 25000)
# 두 정수 ai와 bi를 포함하고 있는 m줄. (1 ≤ ai < bi ≤ n) 상대적인 등수가 바뀐 두 팀이 주어진다. 같은 쌍이 여러 번 발표되는 경우는 없다.
# 출력
# 각 테스트 케이스에 대해서 다음을 출력한다.

# n개의 정수를 한 줄에 출력한다. 출력하는 숫자는 올해 순위이며, 1등팀부터 순서대로 출력한다. 
# 만약, 확실한 순위를 찾을 수 없다면 "?"를 출력한다. 데이터에 일관성이 없어서 순위를 정할 수 없는 경우에는 "IMPOSSIBLE"을 출력한다.

# 입력
# 3
# 5
# 5 4 3 2 1
# 2
# 2 4
# 3 4
# 3
# 2 3 1
# 0
# 4
# 1 2 3 4
# 3
# 1 2
# 3 4
# 2 3

# 출력
# 5 3 2 4 1
# 2 3 1
# IMPOSSIBLE

from collections import deque

# 테스트 케이스만큼 반복
for tc in range(int(input())):
    n = int(input())
    # 진입 차수 배열 생성
    indegree = [0] * (n + 1)
    graph = [[False]*(n + 1) for i in range(n + 1)]
    # 작년 순위 입력
    data = list(map(int, input().split()))
    # 간선 정보 초기화
    for i in range(n):
        for j in range(i + 1, n):
            graph[data[i]][data[j]] = True
            indegree[data[j]] += 1


    # 변경된 순위 정보 입력받기
    m = int(input())
    for i in range(m):
        a, b = map(int, input().split())
        # 간선 방향 뒤집기
        if graph[a][b]:
            graph[a][b] = False
            graph[b][a] = True
            indegree[a] += 1
            indegree[b] -= 1

        else:
            graph[a][b] = True
            graph[b][a] = False
            indegree[a] -= 1
            indegree[b] += 1

    # 위상정렬 시작
    result = []
    q = deque()

    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)


    certain = True
    cycle = False

    # 노드의 개수만큼 반복
    for i in range(n):
        # 큐가 비어있으면 사이클이 발생했다는 의미
        if len(q) == 0:
            cycle = True
            break

        # 큐에 원소가 2개면 가능한 정렬결과가 여러개
        if len(q) >= 2:
            certain = False
            break
    
        # 큐에서 원소 꺼내기
        now = q.popleft()
        result.append(now)

        # 해당노드와 연결된 노드들의 진입차수에서 1 빼기
        for j in range(1, n + 1):
            if graph[now][j]:
                indegree[j] -= 1
                # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
                if indegree[j] == 0:
                    q.append(j)



    if cycle:
        print("impossible")
    elif not certain:
        print("?")
    else:
        for i in result:
            print(i, end=' ')
        print()

