"""
큰 수의 법칙
다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰수를 만드는 법칙
단, 배열의 특정한 인덱스에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없는 것이 특징이다.

배열의 크기 N, 숫자가 더해지는 횟수 M, 그리고 K가 주어질 때 큰 수의 법칙에 따른 결과를 출력하시오.

입력 조건
첫째 줄에 N(2<=N<=1000), M(1<=M<=10000), K(1<=K<=10000)의 자연수가 주어지며, 각 자연수는 공백으로 구분한다.
둘째 줄에 N개의 자연수가 주어진다. 각 자연수는 공백으로 구분한다.
입력으로 주어지는 K는 항상 M보다 작거나 같다.

출력 조건
첫째 줄에 큰 수의 법칙에 따라 더해진 답을 출력한다. 
"""

n,m,k = map(int,input().split())
list1 = list(map(int,input().split()))

list1.sort(reverse=True)

result=0
count=0

for i in range(0,m):
	count += 1
	if count<=k:
		result+=list1[0]
	else:
		result+=list1[1]
		count=0

print(result)