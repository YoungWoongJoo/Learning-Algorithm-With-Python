"""
고정점 찾기(368p)

문제
고정점Fixed Point이란, 수열의 원소 중에서 그 값이 인덱스와 동일한 원소를 의미합니다. 예를 들어 수열 a = {-15, -4, 2, 8, 13}이 있을 때 a[2]=2이므로, 고정점은 2가 됩니다.
하나의 수열이 N개의 서로 다른 원소를 포함하고 있으며, 모든 원소가 오름차순으로 정렬되어 있습니다. 이때 이 수열에서 고정점이 있다면, 고정점을 출력하는 프로그램을 작성하세요. 만약 고정점이 없다면 -1을 출력합니다.
단, 이 문제는 시간 복잡도 O(logN)으로 알고리즘을 설계하지 않으면 '시간 초과' 판정을 받습니다.

입력
첫째 줄에 N이 입력됩니다. (1≤N≤1,000,000)
둘째 줄에 N개의 원소가 정수 형태로 공백으로 구분되어 입력됩니다. (-10^9≤각 원소의 값 ≤10^9)

출력
고정점을 출력한다. 고정점이 없다면 -1을 출력합니다.
"""

def binary_search(data,x,start,end):	#이진탐색
	mid=(end+start)//2

	if start>end:
		return False
	
	if data[mid]=x:	#고정점 원소를 찾았으면 true
		return True
	elif data[mid]>x:	#mid 인덱스의 원소가 x보다 크면 왼쪽 탐색
		return binary_search(data,x,start,mid-1)
	else:
		return binary_search(data,x,mid,end)

n=int(input())
data=list(map(int,input().split()))

result=[]

for x in data:
	if x>=0: #원소가 음수이면 고정점이 불가능하므로 건너뛴다.
		if binary_search(data,x,0,n-1):
			result.append(x)

if len(result)==0:
	print(-1)
else:
	print(result)