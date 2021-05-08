"""
금광(375p)

n × m 크기의 금광이 있다. 금광은 1 × 1 크기의 칸으로 나누어져 있으며, 각 칸은 특정한 크기의
금이 들어 있다
채굴자는 첫 번째 열부터 출발하여 금을 캐기 시작한다. 맨 처음에는 첫 번째 열의 어느 행에서든 출발할 수 있다.
이후에 m - 1번에 걸쳐서 매번 오른쪽 위, 오른쪽, 오른쪽 아래 3가지 중 하나의 위치로 이동해야 한다.
결과적으로 채굴자가 얻을 수 있는 금의 최대 크기를 출력하는 프로그램을 작성하라


입력
첫째줄 T(1<=t<=1000)
매 테스트케이스 첫째줄에 n,m 공백구분(1<=n,m<=20), 
둘째줄에 n*m개의 위치에 금 개수 공백입력(각위치 0부터100까지)

출력
테스트케이스마다 채굴자가 얻을 수 있는 금의 최대 크기
각 테스트케이스마다 줄바꿈
"""


import sys
input=sys.stdin.readline

for tc in range(int(input())):	#테스트케이스마다
	n,m=map(int,input().split())
	arr=list(map(int,input().split()))

	dp=[]
	index=0
	for i in range(n):	#dp테이블 초기화
		dp.append(arr[index:index+m])
		index+=m

	for j in range(1,m):
		for i in range(n):
			if i==0:	#가장 위쪽 행이면 왼쪽 위에서 못옴
				left_up=0	#왼쪽위에서오는경우 0
			else:
				left_up=dp[i-1][j-1]
			if i==n-1:	#가장 아래쪽 행이면 왼쪽 아래에서 못옴
				left_down=0
			else:
				left_down=dp[i+1][j-1]
			left=dp[i][j-1]
			
			dp[i][j]+=max(left_up,left_down,left)	#세가지 위치에서 가장 많은 금의 양을 더함
	
	result=0
	for i in range(n):
		result=max(result,dp[i][m-1])	#금의 양 최대치 갱신
	
	print(result)