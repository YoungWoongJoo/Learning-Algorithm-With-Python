"""
블록 이동하기(355p) 카카오기출(https://programmers.co.kr/learn/courses/30/lessons/60063)

문제 설명
로봇개발자 "무지"는 한 달 앞으로 다가온 "카카오배 로봇경진대회"에 출품할 로봇을 준비하고 있습니다. 준비 중인 로봇은 2 x 1 크기의 로봇으로 "무지"는 "0"과 "1"로 이루어진 N x N 크기의 지도에서 2 x 1 크기인 로봇을 움직여 (N, N) 위치까지 이동 할 수 있도록 프로그래밍을 하려고 합니다. 로봇이 이동하는 지도는 가장 왼쪽, 상단의 좌표를 (1, 1)로 하며 지도 내에 표시된 숫자 "0"은 빈칸을 "1"은 벽을 나타냅니다. 로봇은 벽이 있는 칸 또는 지도 밖으로는 이동할 수 없습니다. 로봇은 처음에 아래 그림과 같이 좌표 (1, 1) 위치에서 가로방향으로 놓여있는 상태로 시작하며, 앞뒤 구분없이 움직일 수 있습니다.

로봇이 움직일 때는 현재 놓여있는 상태를 유지하면서 이동합니다. 예를 들어, 위 그림에서 오른쪽으로 한 칸 이동한다면 (1, 2), (1, 3) 두 칸을 차지하게 되며, 아래로 이동한다면 (2, 1), (2, 2) 두 칸을 차지하게 됩니다. 로봇이 차지하는 두 칸 중 어느 한 칸이라도 (N, N) 위치에 도착하면 됩니다.

로봇은 다음과 같이 조건에 따라 회전이 가능합니다.

위 그림과 같이 로봇은 90도씩 회전할 수 있습니다. 단, 로봇이 차지하는 두 칸 중, 어느 칸이든 축이 될 수 있지만, 회전하는 방향(축이 되는 칸으로부터 대각선 방향에 있는 칸)에는 벽이 없어야 합니다. 로봇이 한 칸 이동하거나 90도 회전하는 데는 걸리는 시간은 정확히 1초 입니다.

"0"과 "1"로 이루어진 지도인 board가 주어질 때, 로봇이 (N, N) 위치까지 이동하는데 필요한 최소 시간을 return 하도록 solution 함수를 완성해주세요.

제한사항
board의 한 변의 길이는 5 이상 100 이하입니다.
board의 원소는 0 또는 1입니다.
로봇이 처음에 놓여 있는 칸 (1, 1), (1, 2)는 항상 0으로 주어집니다.
로봇이 항상 목적지에 도착할 수 있는 경우만 입력으로 주어집니다.
"""

from collections import deque

def get_next_pos(now_pos,new_board):
	next_pos=[]
	now_pos=list(now_pos)
	x1,y1,x2,y2=now_pos[0][0],now_pos[0][1],now_pos[1][0],now_pos[1][1]

	dx=[1,-1,0,0]
	dy=[0,0,1,-1]

	for d in range(4):
		nx1,ny1,nx2,ny2=x1+dx[d],y1+dy[d],x2+dx[d],y2+dy[d]

		if new_board[nx1][ny1]==0 and new_board[nx2][ny2]==0:	#한칸씩 4방향따라 움직인 후 빈공간이면
			next_pos.append({(nx1,ny1),(nx2,ny2)})

		if x1==x2:	#로봇이 가로방향으로 놓여있을때
			for i in [1,-1]:
				if new_board[x1+i][y1]==0 and new_board[x2+i][y2]==0:	#위아래 전부 빈공간이면 회전
					next_pos.append({(x1,y1),(x1+i,y1)})
					next_pos.append({(x2,y2),(x2+i,y2)})
		if y1==y2:	#로봇이 세로방향으로 놓여있을때
			for i in [1,-1]:
				if new_board[x1][y1+i]==0 and new_board[x2][y2+i]==0:	#좌우 전부 빈공간이면 회전
					next_pos.append({(x1,y1),(x1,y1+i)})
					next_pos.append({(x2,y2),(x2,y2+i)})

	return next_pos

def solution(board):
	cost = 0
	board_len=len(board)
	new_board=[[1]*(board_len+2) for _ in range(board_len+2)]

	for i in range(board_len):
		for j in range(board_len):
			new_board[i+1][j+1]=board[i][j]	#인덱스 접근을 쉽게 하기위해 board바깥을 벽으로 둘러쌈

	q=deque()
	visited=[]	#방문한 곳
	now_pos={(1,1),(1,2)}	#시작지점	,	로봇이 좌표2개를 차지하여 순서상관없는 집합자료형을 이용
	q.append((now_pos,0))	#처음시작지점, 0초
	visited.append(now_pos)

	while q:	#bfs
		now_pos,cost=q.popleft()
		if (board_len,board_len) in now_pos:	#목표지점 도달했으면 걸린시간 반환
			return cost
		
		for next_pos in get_next_pos(now_pos,new_board):	#갈 수 있는 다음 좌표들중에서
			if next_pos not in visited:	#방문하지 않은 곳이면 큐에 추가
				q.append((next_pos,cost+1))
				visited.append(next_pos)

	return cost