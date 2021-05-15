"""
탑승구(395p) 

공항에는 g개의 탑승구가 있으며, 각각의 탑승구는 1번부터 g번까지의 번호로 구분된다.
공항에는 p개의 비행기가 차례대로 도착할 예정이며, i번째 비행기를 1번부터 gi번째(1<=gi<=g) 탑승구 중 하나에 영구적으로 도킹해야 합니다. 이때, 다른 비행기가 도킹하지 않은 탑승구에만 도킹할 수 있다.

또한 p개의 비행기를 순서대로 도킹하다가 만약에 어떠한 탑승구에도 도킹할 수 없는 비행기가 나오는 경우, 그 시점에서 공항의 운행을 중지한다. 공항의 관리자는 최대한 많은 비행기를 공항에 도킹하고자 한다.
비행기를 최대 몇 대 도킹할 수 있는지를 출력하는 프로그램을 작성하세요.

입력조건
첫째 줄에 탑승구의 수 g(1<=g<=100,000)
둘째 줄에 비행기의 수 p(1<=p<=100,000)
다음 p개의 줄에 각 비행기가 도킹할 수 있는 탑승구의 정보 gi(1<=gi<=g)
(이는 i번째 비행기가 1번부터 gi번째 탑승구 중 하나에 도킹할 수 있다는 의미)

출력조건
첫째 줄에 도킹할 수 있는 비행기의 최대 개수를 출력
"""

import sys
input=sys.stdin.readline

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

g=int(input())
parent=[i for i in range(g+1)]
p=int(input())
gi=[]
for _ in range(p):
	gi.append(int(input()))

count=0

for x in gi:
	px=find_parent(parent,x)
	if px==0:	#루트 노드가0이면 도킹x(할당이다되었다는뜻))
		break
	union_parent(parent,px,px-1)	#루트 노드가 0이 아니면 1보다 작은번호와 유니온
	count+=1

print(parent)
print(count)