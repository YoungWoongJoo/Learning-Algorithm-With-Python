"""
커리큘럼

온라인으로 컴퓨터공학 강의를 듣고 있다. 이때 각 온라인 강의는 선수 강의가 있을 수 있는데, 선수 강의가 있는 강의는 선수 강의를 먼저 들어야만 해당 강의를 들을 수 있다.
예를 들어 '알고리즘'강의의 선수 강의로 '자료구조'와 '컴퓨터 기초'가 존재한다면, '자료구조'와 '컴퓨터 기초'를 모두 들은 이후에 '알고리즘'강의를 들을 수 있다.

총 N개의 강의 듣고자 한다. 모든 강의는 1번부터 N번까지의 번호를 가진다. 또한 동시에 여러 개의 강의를 들을 수 있다고 가정한다. 예를 들어 N=3일 때, 3번 강의의 선수 강의로 1번과 2번 강의가 있고, 1번과 2번 강의는 선수 강의가 없다고 가정하자. 그리고 각 강의에 대하여 강의 시간이 다음과 같다고 가정하자.

1번 강의 : 30시간
2번 강의 : 20시간
3번 강의 : 40시간

이 경우 1번 강의를 수강하기까지의 최소 시간은 30시간, 2번 강의를 수강하기까지의 최소 시간은 20시간, 3번 강의를 수강하기까지의 최소 시간은 70시간이다.

N개의 강의 정보가 주어졌을 때, N개의 강의에 대하여 수강하기까지 걸리는 최소 시간을 각각 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 동빈이가 듣고자 하는 강의의 수 N(1<=N<=500)
다음 N개의 줄에는 각 강의의 강의 시간과 그 강의를 듣기 위해 먼저 들어야 하는 강의들의 번호가 자연수로 주어지며, 각 자연수는 공백으로 구분한다. 이때 강의 시간은 100000 이하의 자연수이다.
각 강의 번호는 1부터 N까지로 구성되며, 각 줄은 -1로 끝난다.

출력
N개의 강의에 대하여 수강하기까지 걸리는 최소 시간을 한줄에 하나씩 출력한다.

"""

from collections import deque
import copy
import sys
input=sys.stdin.readline

n=int(input())
indegree=[0]*(n+1)
graph=[[] for i in range(n+1)]
times=[0]*(n+1)

for i in range(1,n+1):
	input_data=list(map(int,input().split()))
	times[i]=input_data[0]
	for data in input_data[1:-1]:
		indegree[i]+=1
		graph[data].append(i)

def topology_sort():
	result=copy.deepcopy(times)
	q=deque()
	
	for i in range(1,n+1):
		if indegree[i]==0:
			q.append(i)
	
	while q:
		now=q.popleft()

		for i in graph[now]:
			result[i]=max(result[i],result[now]+times[i])
			indegree[i]-=1
			if indegree[i]==0:
				q.append(i)

	for t in result[1:]:
		print(t)

topology_sort()