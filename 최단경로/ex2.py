"""
전보

N개의 도시가 있다.
각 도시는 다른 도시로 메시지를 전송할 수 있다.
도시 사이에 통로가 설치되어 있어야 하며, 메시지를 보낼 때는 일정 시간이 소요된다.

메시지는 도시 C에서 출발하여 각 도시 사이에 설치된 통로를 거쳐, 최대한 많이 퍼져나갈 것이다. 각 도시의 번호와 통로가 설치되어 있는 정보가 주어졌을 때, 도시 C에서 보낸 메시지를 받게 되는 도시의 개수는 총 몇 개이며 도시들이 모두 메시지를 받는 데까지 걸리는 시간은 얼마인지 계산하는 프로그램을 작성하시오.

입력
첫째 줄에 도시의 개수 N, 통로의 개수 M, 메시지를 보내고자 하는 도시 C
(1<=n<=30000, 1<=m<=200000, 1<=c<=n)
둘째 줄부터 M + 1번째 줄에 걸쳐서 통로에 대한 정보 X(특정 도시), Y(다른 특정 도시), Z(메시지가 전달되는 시간)
(1<=x,y<=n, 1<=z<=1000)

출력
첫째 줄에 도시 C에서 보낸 메시지를 받는 도시의 총 개수와 총 걸리는 시간을 공백으로 구분하여 출력

"""

import sys
import heapq
input=sys.stdin.readline

INF=int(1e9)

n,m,c=map(int,input().split())
start=c
graph=[[] for _ in range(n+1)]
distance=[INF]*(n+1)

for _ in range(m):
	x,y,z=map(int,input().split())
	graph[x].append((y,z))

def dijkstra(start):
	distance[start]=0
	q=[]
	heapq.heappush(q,(0,start))

	while q:
		dist,now=heapq.heappop(q)

		if dist>distance[now]:
			continue
		
		for item in graph[now]:
			cost=dist+item[1]
			if cost<distance[item[0]]:
				distance[item[0]]=cost
				heapq.heappush(q,(cost,item[0]))

dijkstra(start)

count=0
max_distance=0

for d in distance:
	if d!=INF:
		count+=1
		max_distance=max(d,max_distance)

#count-1은 자기자신에게 보내는 시간은 뺀다
print(count-1,max_distance)	