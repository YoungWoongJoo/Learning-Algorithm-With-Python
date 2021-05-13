"""
정확한 순위(386p)

학생들의 성적을 비교한 결과가 주어질 때, 성적 순위를 정확히 알 수 있는 학생은 모두 몇 명인지 계산하는 프로그램을 작성하세요.

첫째 줄에 학생들의 수 N, 두 학생의 성적을 비교한 횟수 M
다음 M개의 각 줄에는 두 학생의 성적을 비교한 결과를 나타내는 두 양의 정수 A와 B가 주어집니다. 이는 A번 학생의 성적이 B번 학생보다 낮다는 것을 의미합니다.
"""

import sys
input=sys.stdin.readline
INF=int(1e9)

n,m=map(int,input().split())
graph=[[INF]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
	graph[i][i]=0

for _ in range(m):
	a,b=map(int,input().split())
	graph[a][b]=1	#a가 b보다 작다(a-b 방향 그래프))

for k in range(1,n+1):
	for a in range(1,n+1):
		for b in range(1,n+1):
			graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b])

count=0
result=0

for a in range(1,n+1):
	for b in range(1,n+1):
		if graph[a][b]!=INF or graph[b][a]!=INF:	#a에서b 혹은 b에서a가 값이 있으면 비교가능
			count+=1
	if count==n:
		result+=1

print(result)
