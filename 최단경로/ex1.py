"""
미래 도시

방문 판매원 A는 많은 회사가 모여 있는 공중 미래 도시에 있다. 공중 미래도시에는 1번부터 N번까지의 회사가 있는데 특정 회사끼리는 서로 도로를 통해 연결되어 있다.

특정 회사끼리는 양방향으로 이동할 수 있고, 1만큼의 시간이 걸린다.

A는 1번 회사에서 출발하여 K번 회사를 방문한 뒤 X번 회사로 가는 것이 목표다.

이때 A는 가능한 한 빠르게 이동하고자 한다. A가 회사 사이를 이동하게 되는 최소 시간을 계산하는 프로그램을 작성하시오.

입력
첫째 줄에 전체 회사의 개수 N과 경로의 개수 M이 공백으로 구분되어 차례로 입력
(1<=n,m<=100)
둘째 줄부터 M+1번째 줄에는 연결된 두 회사의 번호가 공백으로 구분되어 주어진다.
M+2번째 줄에는 X와 K가 공백으로 구분되어 차례대로 주어진다.(1<=K<=100)

출력
첫째 줄에 방문 판매원 A가 K번 회사를 거쳐 X번 회사로 가는 최소 이동 시간을 출력
만약 X번 회사에 도달할 수 없다면 -1을 출력

"""

import sys
input=sys.stdin.readline
INF=int(1e9)

n,m=map(int,input().split())
graph=[[INF]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
	graph[i][i]=0

for i in range(m):
	a,b=map(int,input().split())
	graph[a][b]=1
	graph[b][a]=1

x,k=map(int,input().split())

for i in range(1,n+1):
	for a in range(1,n+1):
		for b in range(1,n+1):
			graph[a][b]=min(graph[a][b],graph[a][i]+graph[i][b])

result = graph[1][k]+graph[k][x]

if result>=INF:
	print(-1)
else:
	print(result)
