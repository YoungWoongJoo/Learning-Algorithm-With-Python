"""
여행 계획(393p)

어떤 한 나라에는 n개의 여행지가 있으며, 각 여행지는 1~n까지의 번호로 구분된다.
또한 임의의 두 여행지 사이에는 두 여행지를 연결하는 도로가 존재할 수 있다.
이때, 여행지가 도로로 연결되어 있다면 양방향으로 이동이 가능하다는 의미이다.
하나의 여행 계획을 세운 뒤에 이 여행 계획이 가능한지의 여부를 판단하고자 한다.

여행지의 개수와 여행지 간의 연결 정보가 주어졌을 때, 여행 계획이 가능한지의 여부를 판별하는 프로그램을 작성하세요.

입력조건
첫째 줄에 여행지의 수 n과 여행 계획에 속한 도시의 수 m (1<=n,m<=500)
다음 n개의 줄에 걸쳐 nxn 행렬을 통해 임의의 두 여행지가 서로 연결되어 있는지의 여부
(값이 1이면 서로 연결, 0이면 연결x)
마지막 줄에 여행 계획에 포함된 여행지의 번호들이 공백으로 구분되어 입력

출력조건
여행 계획이 가능하다면 YES, 불가능하면 NO를 출력
"""

import sys
input=sys.stdin.readline

def find_parent(parent,x):
	if x!=parent[x]:
		parent[x]=find_parent(parent,parent[x])
	return parent[x]


def union_parent(graph,parent,a,b):	#서로소집합 알고리즘
	a=find_parent(parent,a)
	b=find_parent(parent,b)

	if a<b:
		parent[b]=a
	if b<a:
		prent[a]=b
		

n,m=map(int,input().split())
graph=[]

for _ in range(n):
	graph.append(list(map(int,input().split())))

parent=[i for i in range(n)]

for a in range(n):
	for b in range(n):
		if graph[a][b]==1:
			union_parent(graph,parent,a,b)

plan=list(map(int,input().split()))

a=find_parent(parent,plan[0]-1)
result=True

for i in range(1,len(plan)):	#각 여행 경로의 부모노드가 같지 않으면 불가능한 여행
	b=find_parent(parent,plan[i]-1)
	if a!=b:
		result=False
		break
	a=b

if result:
	print('YES')
else:
	print('NO')