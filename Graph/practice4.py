"""
행성 터널(398p) 백준2887(https://www.acmicpc.net/problem/2887)

문제
때는 2040년, 이민혁은 우주에 자신만의 왕국을 만들었다. 왕국은 N개의 행성으로 이루어져 있다. 민혁이는 이 행성을 효율적으로 지배하기 위해서 행성을 연결하는 터널을 만들려고 한다.

행성은 3차원 좌표위의 한 점으로 생각하면 된다. 두 행성 A(xA, yA, zA)와 B(xB, yB, zB)를 터널로 연결할 때 드는 비용은 min(|xA-xB|, |yA-yB|, |zA-zB|)이다.

민혁이는 터널을 총 N-1개 건설해서 모든 행성이 서로 연결되게 하려고 한다. 이때, 모든 행성을 터널로 연결하는데 필요한 최소 비용을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 행성의 개수 N이 주어진다. (1 ≤ N ≤ 100,000) 다음 N개 줄에는 각 행성의 x, y, z좌표가 주어진다. 좌표는 -109보다 크거나 같고, 109보다 작거나 같은 정수이다. 한 위치에 행성이 두 개 이상 있는 경우는 없다. 

출력
첫째 줄에 모든 행성을 터널로 연결하는데 필요한 최소 비용을 출력한다.

"""

import sys
input=sys.stdin.readline
import heapq

def find_parent(parent,x):
	if x!=parent[x]:
		parent[x]=find_parent(parent,parent[x])
	return parent[x]

def union_parent(parent,a,b):
	a=find_parent(parent,a)
	b=find_parent(parent,b)

	if a<b:
		parent[b]=a
	else:
		parent[a]=b

n=int(input())
x=[]
y=[]
z=[]

for i in range(n):	#각 x,y,z 좌표와 인덱스
	a,b,c=map(int,input().split())
	x.append((a,i))
	y.append((b,i))
	z.append((c,i))

x.sort()	#각 x,y,z 축을 기준으로 정렬했을 때 가장 짧은 터널
y.sort()
z.sort()

parent=[i for i in range(n)]

q=[]

for i in range(n-1):	#x,y,z 좌표값 차이중 가장 작은 것을 기준이므로 우선순위큐에 넣는다
	heapq.heappush(q,(abs(x[i+1][0]-x[i][0]),x[i][1],x[i+1][1]))
	heapq.heappush(q,(abs(y[i+1][0]-y[i][0]),y[i][1],y[i+1][1]))
	heapq.heappush(q,(abs(z[i+1][0]-z[i][0]),z[i][1],z[i+1][1]))

result=0

while q:
	cost,a,b=heapq.heappop(q)

	if find_parent(parent,a)!=find_parent(parent,b):
		union_parent(parent,a,b)
		result+=cost

print(result)