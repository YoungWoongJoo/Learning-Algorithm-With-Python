"""
숨바꼭질(390p)

동빈이는 숨바꼭질을 하면서 술래로부터 잡히지 않도록 숨을 곳을 찾고 있습니다. 동빈이는 1~N번까지의 헛간 중에서 하나를 골라 숨을 수 있으며, 술래는 항상 1번 헛간에서 출발합니다. 전체 맵에는 총 M개의 양방향 통로가 존재하며, 하나의 통로는 서로 다른 두 헛간을 연결합니다. 또한 전체 맵은 항상 어떤 헛간에서 다른 어떤 헛간으로 도달이 가능한 형태로 주어집니다.

동빈이는 1번 헛간으로부터 최단 거리가 가장 먼 헛간이 가장 안전하다고 판단하고 있습니다. 이때 최단 거리의 의미는 지나야 하는 길의 최소 개수를 의미합니다. 동빈이가 숨을 헛간의 번호를 출력하는 프로그램을 작성하세요.

입력조건
첫째 줄에는 n,m 공백으로 구분하여 입력
(2<=n<=20,000),(1<=m<=50,000)
이후 m개의 줄에 걸쳐서 서로 연결된 두 헛간 a와 b의 번호가 공백으로 구분되어 입력
(1<=a,b<=n)

출력조건
첫 번째는 숨어야 하는 헛간 번호를(만약 거리가 같은 헛간이 여러 개면 가장 작은 번호를 출력)
두 번째는 그 헛간까지의 거리를,
세 번째는 그 헛간과 같은 거리를 갖는 헛간의 개수를 출력
"""

import sys
input=sys.stdin.readline
INF=int(1e9)

n,m=map(int,input().split())
graph=[[INF]*(n+1) for _ in range(n+1)]

for _ in range(m):
	a,b=map(int,input().split())
	graph[a][b]=1
	graph[b][a]=1	#양방향그래프이므로 b->a에도 거리를 입력

for i in range(1,n+1):
	graph[i][i]=0

for k in range(1,n+1):
	for a in range(1,n+1):
		for b in range(1,n+1):
			graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b]) #각 a에서 b까지의 최단거리

max_val=max(graph[1][1:])	#최단거리중 최대값
index=graph[1].index(max_val)	#최단거리중 최대값을 가지는 헛간번호
count=graph[1][1:].count(max_val)	#최단거리 최대값을 가지는 헛간 개수

print(index,max_val,count)