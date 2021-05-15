"""
최종 순위(399p) 백준3665(https://www.acmicpc.net/problem/3665)

문제
올해 ACM-ICPC 대전 인터넷 예선에는 총 n개의 팀이 참가했다. 팀은 1번부터 n번까지 번호가 매겨져 있다. 놀랍게도 올해 참가하는 팀은 작년에 참가했던 팀과 동일하다.

올해는 인터넷 예선 본부에서는 최종 순위를 발표하지 않기로 했다. 그 대신에 작년에 비해서 상대적인 순위가 바뀐 팀의 목록만 발표하려고 한다. (작년에는 순위를 발표했다) 예를 들어, 작년에 팀 13이 팀 6 보다 순위가 높았는데, 올해 팀 6이 팀 13보다 순위가 높다면, (6, 13)을 발표할 것이다.

창영이는 이 정보만을 가지고 올해 최종 순위를 만들어보려고 한다. 작년 순위와 상대적인 순위가 바뀐 모든 팀의 목록이 주어졌을 때, 올해 순위를 만드는 프로그램을 작성하시오. 하지만, 본부에서 발표한 정보를 가지고 확실한 올해 순위를 만들 수 없는 경우가 있을 수도 있고, 일관성이 없는 잘못된 정보일 수도 있다. 이 두 경우도 모두 찾아내야 한다.

입력
첫째 줄에는 테스트 케이스의 개수가 주어진다. 테스트 케이스는 100개를 넘지 않는다. 각 테스트 케이스는 다음과 같이 이루어져 있다.

팀의 수 n을 포함하고 있는 한 줄. (2 ≤ n ≤ 500)
n개의 정수 ti를 포함하고 있는 한 줄. (1 ≤ ti ≤ n) ti는 작년에 i등을 한 팀의 번호이다. 1등이 가장 성적이 높은 팀이다. 모든 ti는 서로 다르다.
상대적인 등수가 바뀐 쌍의 수 m (0 ≤ m ≤ 25000)
두 정수 ai와 bi를 포함하고 있는 m줄. (1 ≤ ai < bi ≤ n) 상대적인 등수가 바뀐 두 팀이 주어진다. 같은 쌍이 여러 번 발표되는 경우는 없다.
출력
각 테스트 케이스에 대해서 다음을 출력한다.

n개의 정수를 한 줄에 출력한다. 출력하는 숫자는 올해 순위이며, 1등팀부터 순서대로 출력한다. 만약, 확실한 순위를 찾을 수 없다면 "?"를 출력한다. 데이터에 일관성이 없어서 순위를 정할 수 없는 경우에는 "IMPOSSIBLE"을 출력한다.

"""

import sys
input=sys.stdin.readline
from collections import deque

t=int(input())
for tc in range(t):	#테스트케이스 반복
	n=int(input())	#팀의 수

	indegree=[0]*(n+1)	#진입차수

	graph=[[0]*(n+1) for _ in range(n+1)]	#방향그래프(순위가 높은쪽에서 낮은쪽)

	ti=list(map(int,input().split()))	#작년 팀순위

	for i in range(n):
		for j in range(i+1,n):	#위상정렬 알고리즘 이용
			graph[ti[i]][ti[j]]=1
			indegree[ti[j]]+=1

	m=int(input())

	for i in range(m):
		a,b=map(int,input().split())
		if graph[a][b]==1:	#a의 등수가 b의 등수보다 높으면
			graph[a][b]=0
			graph[b][a]=1
			indegree[b]-=1
			indegree[a]+=1
		else:
			graph[a][b]=1
			graph[b][a]=0
			indegree[b]+=1
			indegree[a]-=1

	result=[]	#현재 순위 정보
	q=deque()

	for i in range(1,n+1):
		if indegree[i]==0: #진입차수가 가장낮은 팀번호(1등팀)
			q.append(i)
		
	unique=True
	cycle=False

	for i in range(n):	#팀의 수만큼 반복
		if len(q)==0: #큐가 비어있으면 싸이클발생(impossible출력))
			cycle=True
			break
		if len(q)>1: #큐안에 2개이상있으면 정렬결과 중복(?출력)
			unique=False
			break
		
		now=q.popleft()
		result.append(now)

		for j in range(1,n+1):
			if graph[now][j]==1:
				indegree[j]-=1
				if indegree[j]==0:
					q.append(j)

	if cycle:
		print('IMPOSSIBLE')
	elif not unique:
		print('?')
	else:
		for i in result:
			print(i,end=' ')
		print()