"""
아기 상어(402p) 백준16236(https://www.acmicpc.net/problem/16236)

문제
N×N 크기의 공간에 물고기 M마리와 아기 상어 1마리가 있다. 공간은 1×1 크기의 정사각형 칸으로 나누어져 있다. 한 칸에는 물고기가 최대 1마리 존재한다.

아기 상어와 물고기는 모두 크기를 가지고 있고, 이 크기는 자연수이다. 가장 처음에 아기 상어의 크기는 2이고, 아기 상어는 1초에 상하좌우로 인접한 한 칸씩 이동한다.

아기 상어는 자신의 크기보다 큰 물고기가 있는 칸은 지나갈 수 없고, 나머지 칸은 모두 지나갈 수 있다. 아기 상어는 자신의 크기보다 작은 물고기만 먹을 수 있다. 따라서, 크기가 같은 물고기는 먹을 수 없지만, 그 물고기가 있는 칸은 지나갈 수 있다.

아기 상어가 어디로 이동할지 결정하는 방법은 아래와 같다.

더 이상 먹을 수 있는 물고기가 공간에 없다면 아기 상어는 엄마 상어에게 도움을 요청한다.
먹을 수 있는 물고기가 1마리라면, 그 물고기를 먹으러 간다.
먹을 수 있는 물고기가 1마리보다 많다면, 거리가 가장 가까운 물고기를 먹으러 간다.
거리는 아기 상어가 있는 칸에서 물고기가 있는 칸으로 이동할 때, 지나야하는 칸의 개수의 최솟값이다.
거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기를 먹는다.
아기 상어의 이동은 1초 걸리고, 물고기를 먹는데 걸리는 시간은 없다고 가정한다. 즉, 아기 상어가 먹을 수 있는 물고기가 있는 칸으로 이동했다면, 이동과 동시에 물고기를 먹는다. 물고기를 먹으면, 그 칸은 빈 칸이 된다.

아기 상어는 자신의 크기와 같은 수의 물고기를 먹을 때 마다 크기가 1 증가한다. 예를 들어, 크기가 2인 아기 상어는 물고기를 2마리 먹으면 크기가 3이 된다.

공간의 상태가 주어졌을 때, 아기 상어가 몇 초 동안 엄마 상어에게 도움을 요청하지 않고 물고기를 잡아먹을 수 있는지 구하는 프로그램을 작성하시오.

입력
첫째 줄에 공간의 크기 N(2 ≤ N ≤ 20)이 주어진다.

둘째 줄부터 N개의 줄에 공간의 상태가 주어진다. 공간의 상태는 0, 1, 2, 3, 4, 5, 6, 9로 이루어져 있고, 아래와 같은 의미를 가진다.

0: 빈 칸
1, 2, 3, 4, 5, 6: 칸에 있는 물고기의 크기
9: 아기 상어의 위치
아기 상어는 공간에 한 마리 있다.

출력
첫째 줄에 아기 상어가 엄마 상어에게 도움을 요청하지 않고 물고기를 잡아먹을 수 있는 시간을 출력한다.

"""

import sys
from collections import deque
input=sys.stdin.readline
INF=int(1e9)

size=2
count=size
now_x,now_y=0,0

dx=[1,-1,0,0]
dy=[0,0,1,-1]

def bfs():
	dist=[[-1]*n for _ in range(n)]

	q=deque()
	dist[now_x][now_y]=0
	q.append((now_x,now_y))

	while q:
		x,y=q.popleft()

		for d in range(4):
			next_x=x+dx[d]
			next_y=y+dy[d]

			if next_x>=0 and next_x<n and next_y>=0 and next_y<n:	#다음 좌표가 공간 안에 있고
				#아직 방문하지 않앗고, 상어보다 물고기가 작거나 같으면(지나갈수 있으면)
				if dist[next_x][next_y]==-1 and data[next_x][next_y]<=size:	
					q.append((next_x,next_y))
					dist[next_x][next_y]=dist[x][y]+1

	return dist	#각 물고기의 위치까지의 최단거리

def find_fish(dist):
	min_dist=INF
	x,y=0,0
	for i in range(n):
		for j in range(n):
			if dist[i][j]>0 and 0<data[i][j]<size: # 빈공간이 아니고 최단거리에 있는 물고기중 상어보다 작으면
				if min_dist>dist[i][j]:
					min_dist=dist[i][j]
					x,y=i,j

	if min_dist==INF:
		return None

	return min_dist,x,y

n=int(input())	#공간 크기 n

data=[]

for i in range(n):
	data.append(list(map(int,input().split())))
	for j in range(n):
		if data[i][j]==9:
			now_x,now_y=i,j

result=0

while True:
	value=find_fish(bfs())

	if value==None:
		break
	
	data[value[1]][value[2]]=9	#물고기를 먹고 상어위치로 바꾸기
	result+=value[0]	#물고기 먹는 시간 추가
	data[now_x][now_y]=0	#원래있던 자리 빈공간으로 바꾸기
	now_x,now_y=value[1],value[2]

	count-=1	#사이즈가 커지기 위해 먹어야 하는 횟수 감소
	if count==0:	#횟수가 0이면
		size+=1	#사이즈 증가
		count=size	#사이즈가 커지기 위해 먹어야 하는 횟수 초기화
	
print(result)