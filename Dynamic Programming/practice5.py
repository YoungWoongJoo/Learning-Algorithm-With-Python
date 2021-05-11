"""
못생긴 수(31p) 

못생긴 수란 오직 2, 3, 5만을 소인수로 가지는 수를 의미한다. 1은 못생긴 수라고 가정한다. 이때 n번째 못생긴 수를 찾는 프로그램을 작성하시오. 예를 들어 11번째 못생긴 수는 15입니다.
(1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, ...)

입력
첫째 줄에 n이 입력(1부터 1000까지)

출력
n번째 못생긴 수 출력
"""

n=int(input())

dp=[0]*n
dp[0]=1

i2,i3,i5=0,0,0
next2,next3,next5=2,3,5

for i in range(1,n):
	dp[i]=min(next2,next3,next5)

	#못생긴 수에 2 or 3 or 5를 곱한 수도 못생긴 수

	if dp[i]==next2:
		i2+=1
		next2=dp[i2]*2
	if dp[i]==next3:
		i3+=1
		next3=dp[i3]*3
	if dp[i]==next5:
		i5+=1
		next5=dp[i5]*5

print(dp[n-1])
		