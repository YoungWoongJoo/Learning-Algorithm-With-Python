"""
미로 탈출

N * M 크기의 직사각형 형태의 미로에 갇혀 있다.
미로에는 여러 마리의 괴물이 있어 이를피해 탈출해야한다.
현재 위치는 (1, 1)이고 미로의 출구는 (N, M)의 위치에 존재하며 한 번에 한 칸씩 이동할 수 있다.
이때 괴물이 있는 부분은 0으로, 괴물이 없는 부분은 1로 표시되어 있다.
미로는 반드시 탈출할 수 있는 형태로 제시된다. 이때 동빈이가 탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하시오.
칸을 셀 떄는 시작 칸과 마지막 칸을 모두 포함해서 계산한다.

입력조건
- 첫째 줄에 두 정수 N, M(4 <= N, M <= 200)이 주어집니다.
다음 N개의 줄에는 각각 M개의 정수(0혹은 1)로 미로의 정보가 주어진다.
각각의 수들은 공백 없이붙어서 입력으로 제시된다. 또한 시작 칸과 마지막 칸은 항상 1이다.

출력조건
- 첫째 줄에 최소 이동 칸의 개수를 출력한다.
"""

from collections import deque

n,m=map(int,input().split())
graph=[]
for i in range(n):
	graph.append(list(map(int,input())))

dx=[0,0,1,-1]
dy=[1,-1,0,0]

def bfs(start_x,start_y):
	queue=deque()
	queue.append((start_x,start_y))

	while queue:
		x,y=queue.popleft()

		for i in range(4):
			next_x=x+dx[i]
			next_y=y+dy[i]

			if next_x<0 or next_x>n-1 or next_y<0 or next_y>m-1:
				continue
			
			if graph[next_x][next_y]==0:
				continue
			
			if graph[next_x][next_y]==1:
				queue.append((next_x,next_y))
				graph[next_x][next_y]=graph[x][y]+1
	
	return graph[n-1][m-1]

print(bfs(0,0))