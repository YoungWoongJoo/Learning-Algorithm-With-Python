"""
뱀(327p) 삼성전자 SW 역량테스트 (백준 3190번 문제)

문제
 'Dummy' 라는 도스게임이 있다. 이 게임에는 뱀이 나와서 기어다니는데, 사과를 먹으면 뱀 길이가 늘어난다. 뱀이 이리저리 기어다니다가 벽 또는 자기자신의 몸과 부딪히면 게임이 끝난다.

게임은 NxN 정사각 보드위에서 진행되고, 몇몇 칸에는 사과가 놓여져 있다. 보드의 상하좌우 끝에 벽이 있다. 게임이 시작할때 뱀은 맨위 맨좌측에 위치하고 뱀의 길이는 1 이다. 뱀은 처음에 오른쪽을 향한다.

뱀은 매 초마다 이동을 하는데 다음과 같은 규칙을 따른다.

먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.
만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다.
사과의 위치와 뱀의 이동경로가 주어질 때 이 게임이 몇 초에 끝나는지 계산하라.

입력
첫째 줄에 보드의 크기 N이 주어진다. (2 ≤ N ≤ 100) 다음 줄에 사과의 개수 K가 주어진다. (0 ≤ K ≤ 100)

다음 K개의 줄에는 사과의 위치가 주어지는데, 첫 번째 정수는 행, 두 번째 정수는 열 위치를 의미한다. 사과의 위치는 모두 다르며, 맨 위 맨 좌측 (1행 1열) 에는 사과가 없다.

다음 줄에는 뱀의 방향 변환 횟수 L 이 주어진다. (1 ≤ L ≤ 100)

다음 L개의 줄에는 뱀의 방향 변환 정보가 주어지는데,  정수 X와 문자 C로 이루어져 있으며. 게임 시작 시간으로부터 X초가 끝난 뒤에 왼쪽(C가 'L') 또는 오른쪽(C가 'D')로 90도 방향을 회전시킨다는 뜻이다. X는 10,000 이하의 양의 정수이며, 방향 전환 정보는 X가 증가하는 순으로 주어진다.

출력
첫째 줄에 게임이 몇 초에 끝나는지 출력한다.

"""

import sys
input=sys.stdin.readline

n=int(input())
k=int(input())

board=[[0]*(n+1) for _ in range(n+1)]

for _ in range(k):
	i,j=map(int,input().split())
	board[i][j]=2	#사과는 2

l=int(input())
r=[]
for i in range(l):
	x,d=input().split()
	r.append((int(x),d))	#자료형을 주의하자

dx=[0,1,0,-1]
dy=[1,0,-1,0]

q=[(1,1)]
board[1][1]=1
now_x,now_y=1,1
d=0
count=0
index=0

while True:
	now_x,now_y=now_x+dx[d],now_y+dy[d]
	count+=1
	#맵밖이나 자기 몸을 만나는 경우가 아니면
	if now_x>=1 and now_x<=n and now_y>=1 and now_y<=n and board[now_x][now_y]!=1:
		q.append((now_x,now_y))
		if board[now_x][now_y]!=2:
			x,y=q.pop(0)
			board[x][y]=0
		board[now_x][now_y]=1
	
	else:
		print(count)
		break

	if index<l and r[index][0]==count:	#방향전환
		if r[index][1]=='L':
			d=(d-1)%4
		elif r[index][1]=='D':
			d=(d+1)%4
		index+=1