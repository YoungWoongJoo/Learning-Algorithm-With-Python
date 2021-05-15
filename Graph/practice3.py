"""
어두운 길(397p)

한 마을은 n개의 집과 m개의 도로로 구성되어 있다. 각 집은 0번부터 n-1번까지의 번호로 구분된다.
모든 도로에는 가로등이 구비되어 있는데, 특정한 도로의 가로등을 하루 동안 켜기 위한 비용은 해당 도로의 길이와 동일하다. 

예를 들어 2번 집과 3번 집 사이를 연결하는 길이가 7인 도로가 있다고 해보자.
하루동안 이 가로등을 켜기 위한 비용은 7이 된다.

정부에서는 일부 가로등을 비활성화하되, 마을에 있는 임의의 두 집에 대하여 가로등이 켜진 도로만으로도 오갈 수 있도록 만들고자 한다. 결과적으로 일부 가로등을 비활성화하여 최대한 많은 금액을 절약하고자한다.
마을의 집과 도로 정보가 주어졌을 때, 일부 가로등을 비활성화하여 절약할 수 있는 최대 금액을 출력하는 프로그램을 작성하세요.

입력조건
첫째 줄에 집의 n(1<=n<=200,000), 도로의 수 m(n-1<=m<=200,000)
다음 m개의 줄에 각 도로에 대한 정보 x,y,z
(0<=x,y<n) (x번 집과 y번 집 사이에 양방향 도로가 있으며, 그 길이가 z)
단, x와 y가 동일한 경우는 없으며, 모든 도로의 길이 합은 2^31보다 작다

출력조건
첫째 줄에 일부 가로등을 비활성화하여 절약할 수 있는 최대 금액을 출력
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

n,m=map(int,input().split())

q=[]

for i in range(m):
	x,y,z=map(int,input().split())
	heapq.heappush(q,(z,x,y))

parent=[i for i in range(n)]

total=0

while q:	#최소 신장 트리(크루스칼 알고리즘)
	cost,a,b=heapq.heappop(q)	#비용이 적은 도로부터
	
	if find_parent(parent,a)!=find_parent(parent,b):	#도로의 양쪽지점(집)이 같은 루트노드가 아니면
		union_parent(parent,a,b)	#유니온
	else:	#a와 b가 같은 집합에 속하면 도로 비활성화
		total+=cost

print(total)