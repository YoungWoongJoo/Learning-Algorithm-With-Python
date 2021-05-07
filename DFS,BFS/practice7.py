"""
인구 이동(353p) 삼성기출 백준16234번(https://www.acmicpc.net/problem/16234)

문제
N×N크기의 땅이 있고, 땅은 1×1개의 칸으로 나누어져 있다. 각각의 땅에는 나라가 하나씩 존재하며, r행 c열에 있는 나라에는 A[r][c]명이 살고 있다. 인접한 나라 사이에는 국경선이 존재한다. 모든 나라는 1×1 크기이기 때문에, 모든 국경선은 정사각형 형태이다.

오늘부터 인구 이동이 시작되는 날이다.

인구 이동은 다음과 같이 진행되고, 더 이상 아래 방법에 의해 인구 이동이 없을 때까지 지속된다.

국경선을 공유하는 두 나라의 인구 차이가 L명 이상, R명 이하라면, 두 나라가 공유하는 국경선을 오늘 하루동안 연다.
위의 조건에 의해 열어야하는 국경선이 모두 열렸다면, 인구 이동을 시작한다.
국경선이 열려있어 인접한 칸만을 이용해 이동할 수 있으면, 그 나라를 오늘 하루 동안은 연합이라고 한다.
연합을 이루고 있는 각 칸의 인구수는 (연합의 인구수) / (연합을 이루고 있는 칸의 개수)가 된다. 편의상 소수점은 버린다.
연합을 해체하고, 모든 국경선을 닫는다.
각 나라의 인구수가 주어졌을 때, 인구 이동이 몇 번 발생하는지 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N, L, R이 주어진다. (1 ≤ N ≤ 50, 1 ≤ L ≤ R ≤ 100)

둘째 줄부터 N개의 줄에 각 나라의 인구수가 주어진다. r행 c열에 주어지는 정수는 A[r][c]의 값이다. (0 ≤ A[r][c] ≤ 100)

인구 이동이 발생하는 횟수가 2,000번 보다 작거나 같은 입력만 주어진다.

출력
인구 이동이 몇 번 발생하는지 첫째 줄에 출력한다.

"""

from collections import deque
import sys
input=sys.stdin.readline

n,l,r=map(int,input().split())
a=[]
for i in range(n):
	a.append(list(map(int,input().split())))

dx=[-1,0,1,0]
dy=[0,-1,0,1]

result=0	#인구이동횟수

def union_bfs(x,y,index):	#인구수 차이 확인하고 연합하기
	q=deque()
	united=[]	#연합된 국가의 좌표
	united.append((x,y))
	union[x][y]=index
	q.append((x,y))
	sum_population=a[x][y]	#연합 국가의 총 인구수

	while q:
		x,y=q.popleft()
		for d in range(4):	#상하좌우 국가 인구수 차이 확인
			nx=x+dx[d]
			ny=y+dy[d]

			#다음 좌표의 국가가 주어진 땅 범위안에있고 연합되지않은 국가이면
			if nx>=0 and nx<n and ny>=0 and ny<n and union[nx][ny]!=index:	
				if l<=abs(a[x][y]-a[nx][ny])<=r:
					union[nx][ny]=index
					q.append((nx,ny))
					united.append((nx,ny))
					sum_population+=a[nx][ny]
	
	if len(united)>1:	#인구이동이 가능하면(연합국가의 개수가 2개 이상이면)
		for i,j in united:
			a[i][j]=sum_population//len(united)
		return True

	return False

union=[[-1]*n for _ in range(n)]	#연합그래프 초기화
index=0

while True:	#루프마다 인구이동
	stop=True
	for i in range(n):	#시간을 줄이려면 큐를 이용해서 연합확인할때 이전 인구이동한 국가들만 확인하기
		for j in range(n):
			if union[i][j]!=index:
				if union_bfs(i,j,index):
					stop=False
	if stop:
		break
	index+=1

print(index)