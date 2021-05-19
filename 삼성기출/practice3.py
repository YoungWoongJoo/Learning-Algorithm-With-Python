"""
어른 상어(407p) 백준19237(https://www.acmicpc.net/problem/19237)

1<=상어번호<=m (모두 서로 다른 번호))
1의 번호를 가진 상어는 나머지 모두를 쫓아낼 수 있음
n*n 크기 공간 안에 m개의 칸에 상어 한마리씩 있음

1. 맨 처음, 모든 상어는 자신의 위치에 자신의 냄새를 뿌림
2. 그 후 1초마다 모든 상어가 동시에 상하좌우로 이동
3. 이동이 끝난 후, 한 칸에 여러 마리 상어가 있으면 번호가 제일 작은 상어 외의 나머지는 밖으로 사라짐
4. 냄새는 상어가 k번 이동하고 나면 사라짐

각 상어가 이동할때, 인접한 칸 중 아무 냄새가 없는 칸 쪽으로
	(그러한 칸이 없으면 자신의 냄새가 있는 칸 쪽으로)
	(중복될 때는 특정 우선순위 따라서 정함. )

1번 상어만 남게 되기까지 몇 초가 걸리는지를 구하는 프로그램을 작성하시오.

입력
첫 줄에는 N, M, k가 주어진다. (2 ≤ N ≤ 20, 2 ≤ M ≤ N2, 1 ≤ k ≤ 1,000)

그 다음 줄부터 N개의 줄에 걸쳐 격자의 모습이 주어진다. 0은 빈칸이고, 0이 아닌 수 x는 x번 상어가 들어있는 칸을 의미한다.

그 다음 줄에는 각 상어의 방향이 차례대로 주어진다. 1, 2, 3, 4는 각각 위, 아래, 왼쪽, 오른쪽을 의미한다.

그 다음 줄부터 각 상어의 방향 우선순위가 상어 당 4줄씩 차례대로 주어진다. 각 줄은 4개의 수로 이루어져 있다. 하나의 상어를 나타내는 네 줄 중 첫 번째 줄은 해당 상어가 위를 향할 때의 방향 우선순위, 두 번째 줄은 아래를 향할 때의 우선순위, 세 번째 줄은 왼쪽을 향할 때의 우선순위, 네 번째 줄은 오른쪽을 향할 때의 우선순위이다. 각 우선순위에는 1부터 4까지의 자연수가 한 번씩 나타난다. 가장 먼저 나오는 방향이 최우선이다. 예를 들어, 우선순위가 1 3 2 4라면, 방향의 순서는 위, 왼쪽, 아래, 오른쪽이다.

맨 처음에는 각 상어마다 인접한 빈 칸이 존재한다. 따라서 처음부터 이동을 못 하는 경우는 없다.

출력
1번 상어만 격자에 남게 되기까지 걸리는 시간을 출력한다. 단, 1,000초가 넘어도 다른 상어가 격자에 남아 있으면 -1을 출력한다.

"""

import sys
input=sys.stdin.readline

def move():	#각 상어 이동

def move_all_shark(shark,smell,now_dir,priority_dir):	#모든 상어 이동

def smell_process(shark,smell,now_dir,priority_dir):	#뿌려놓았던 냄새 시간 1초 감소, 현재 자리 냄새뿌리기

n,m,k=map(int,input().split())
shark=[]	#상어 위치
smell=[[None]*n for _ in range(n)]	#상어 냄새

for i in range(n):
	shark.append(list(map(int,input().split())))
	for j in range(n):
		if shark[i][j]!=0:
			smell[i][j]=[shark[i][j],k] #맨 처음, 모든 상어는 자신의 위치에 자신의 냄새를 뿌림

now_dir=list(map(int,input().split()))	#현재 상어들의 방향
priority_dir=[]

for _ in range(4*m):
	priority_dir.append(list(map(int,input().split())))	#상어들의 우선순위 방향

t=0	#걸린 시간

while True:
	t+=1

	move_all_shark(shark,smell,now_dir,priority_dir)

	smell_process(shark,smell,now_dir,priority_dir)

	if m==1: #1번 상어만 남았을 경우 시간출력
		print(t)
		return
	
	if t>1000 and m>1:	#1000초가 지나도 1번 외의 다른 상어가 남아있으면 -1출력
		print(-1)
		return