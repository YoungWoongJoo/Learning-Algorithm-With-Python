"""
화성 탐사(388p) 

화성 탐사 기계가 존재하는 공간은 N x N 크기의 2차원 공간이며, 각각의 칸을 지나기 위한 비용(에너지 소모량)이 존재합니다. 가장 왼쪽 위 칸인 [0][0] 위치에서 가장 오른쪽 아래 칸인 [N-1][N-1] 위치로 이동하는 최소 비용을 출력하는 프로그램을 작성하세요. 화성 탐사 기계는 특정한 위치에서 상하좌우 인접한 곳으로 1칸씩 이동할 수 있습니다.

첫째 줄에 테스트 케이스의 수 T(1 <= T <= 10)가 주어집니다.
매 테스트 케이스의 첫째 줄에는 탐사 공간의 크기를 의미하는 정수 N이 주어집니다. 이어서 N개의 줄에 걸쳐 각 칸의 비용이 주어지며 공백으로 구분합니다.

"""

import heapq
import sys
input=sys.stdin.readline
INF=int(1e9)

dx=[0,0,1,-1]
dy=[1,-1,0,0]

def move(graph,energy,x,y):	#다익스트라 알고리즘
	energy[0][0]=graph[0][0]

	q=[]
	heapq.heappush(q,(energy[0][0],(x,y)))

	while q:
		now_e,pos=heapq.heappop(q)	#현재 좌표와 현재 좌표까지의 최소에너지
		now_x,now_y=pos[0],pos[1]

		for d in range(4):
			next_x,next_y=now_x+dx[d],now_y+dy[d]
			if next_x>=0 and next_x<len(graph) and next_y>=0 and next_y<len(graph):	#다음 좌표가 공간안에 있을때
				next_e=graph[next_x][next_y]	#다음 칸으로가기위한 에너지

				if energy[next_x][next_y]<now_e+next_e:	
					continue
				else:	#다음좌표까지의 최소에너지보다 새로운 최소에너지가 작을때
					energy[next_x][next_y]=now_e+next_e
					heapq.heappush(q,(energy[next_x][next_y],(next_x,next_y)))


t=int(input())
for _ in range(t):
	n=int(input())
	graph=[]
	for _ in range(n):
		graph.append(list(map(int,input().split())))

	energy=[[INF]*n for _ in range(n)]

	move(graph,energy,0,0)

	print(energy[n-1][n-1])