"""
정렬된 배열에서 특정 수의 개수 구하기(367p)

문제
N개의 원소를 포함하고 있는 수열이 오름차순으로 정렬되어 있다. 이때 이 수열에서 x가 등장하는 횟수를 계산하세요. 예를 들어 수열 [1, 1, 2, 2, 2 ,2 ,3]이 있을 때 x = 2라면, 현재 수열에서 값이 2인 원소가 4개이므로 4를 출력한다.
단, 이 문제는 시간 복잡도 O(logN) 으로 알고리즘을 설계하지 않으면 '시간 초과' 판정을 받는다.

입력
첫째 줄에 n과 x가 정수형태로 공백으로 구분되어 입력
(1<=n<=1000000),(-10^9<=x<=10^9)
둘째 줄에 n개의 원소가 정수 형태로 공백으로 구분되어 입력

출력
수열의 원소 중에서 값이 x인 원소의 개수 출력
단, 값이 x인 원소가 하나도 없다면 -1 출력
"""

def count_x(data,x):
	first_index=first_search(data,x,0,len(data)-1)	#x가 처음 등장한 인덱스

	if first_index==None:
		return 0

	last_index=last_search(data,x,0,len(data)-1)	#x가 마지막으로 등장한 인덱스

	result = last_index-first_index+1	#x의 개수
	return result

def first_search(data,x,start,end):
	if start>end:
		return None
	mid=(end-start)//2

	if (mid==0 or x>data[mid-1]) and data[mid]==x:	#원소가 하나 남았거나 mid가 x가 처음등장한 인덱스이면
		return mid
	elif data[mid]>=x:	#중간 인덱스의 값이 x보다 크거나 같으면 중간 인덱스를 기준으로 왼쪽을 탐색
		return first_search(data,x,start,mid-1)
	else:	#중간 인덱스의 값이 x보다 작으면 mid+1 인덱스부터 오른쪽으로 탐색
		return first_search(data,x,mid+1,end)

def last_search(data,x,start,end):
	if end<start:
		return None
	mid=(end-start)//2

	if (mid==0 or x<data[mid+1]) and data[mid]==x:	#원소가 하나 남았거나 mid가 x가 마지막등장한 인덱스이면
		return mid
	elif data[mid]>x:	#중간 인덱스의 값이 x보다 크면 중간 인덱스를 기준으로 왼쪽을 탐색
		return last_search(data,x,start,mid-1)
	else:	#중간 인덱스의 값이 x보다 작거나 같으면 mid 인덱스부터 오른쪽으로 탐색
		return last_search(data,x,mid,end)

n,x=int(input().split())
data=list(map(int,input().split()))

result=count_x(data,x)

if result==0:
	print(-1)
else:
	print(result)