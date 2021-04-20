"""
부품 찾기

문제
동빈이네 전자 매장에는 부품이 N개 있다. 각 부품은 정수 형태의 고유한 번호가 있다. 어느 날 손님이 M개의 종류의 부품을 대량으로 구매하겠다며 당일 날 견적서를 요청했다. 동빈이는 때를 놓치지 않고 손님이 문의한 부품 M개 종류를 모두 확인해서 견적서를 작성해야 한다. 이때 가게 안에 부품이 모두 있는지 확인하는 프로그램을 작성해보자.
예를 들어 가게의 부품이 총 5개일 때 부품 번호가 다음과 같다고 하자.

N=5
[8, 3, 7, 9, 2]

손님은 총 3개의 부품이 있는지 확인 요청했는데 부품 번호는 다음과 같다.

M=3
[5, 7, 9]

이때 손님이 요청한 부품 번호의 순서대로 부품을 확인해 부품이 있으면 yes를, 없으면 no를 출력한다. 구분은 공백으로 한다.

입력
첫째 줄에 정수 N이 주어진다. (1<=N<=1,000,000)
둘째 줄에는 공백으로 구분하여 N개의 정수가 주어진다. 이때 정수는 1보다 크고 1,000,000 이하이다.
셋째 줄에는 정수 M이 주어진다. (1<=M<=100,000)
넷째 줄에는 공백으로 구분하여 M개의 정수가 주어진다. 이때 정수는 1보다 크고 10억 이하이다.

출력
첫째 줄에 공백으로 구분하여 각 부품이 존재하면 yes를, 없으면 no를 출력한다.

"""

import sys

n=int(input())

n_item=list(map(int,sys.stdin.readline().rstrip().split()))

n_item.sort()

m=int(input())

m_item=list(map(int,sys.stdin.readline().rstrip().split()))

def binary_search(arr,target,start,end):
	while start<=end:
		mid=(start+end)//2

		if arr[mid]==target:
			return mid
		
		elif arr[mid]>target:
			end=mid-1
		else:
			start=mid+1
	return None

for item in m_item:
	result=binary_search(n_item,item,0,n)
	if result!=None:
		print('yes', end=' ')
	else:
		print('no', end=' ')

#계수정렬과 set()함수(집합자료형)를 이용하여 풀 수도 있다.