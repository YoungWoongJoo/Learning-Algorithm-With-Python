"""
문자열 뒤집기

다솜이는 0과 1로만 이루어진 문자열 S를 가지고 있습니다. 다솜이는 이 문자열 S에 있는 모든 숫자를 전부 같게 만들려고 합니다. 다솜이가 할 수 있는 행동은 S에서 연속된 하나 이상의 숫자를 잡고 모두 뒤집는 것입니다.  뒤집는 것은 1을 0으로, 0은 1로 바꾸는 것을 의미합니다.

예를 들어 S=0001100일 때,
1. 전체를 뒤집으면 1110011
2. 4번부터 5번째 문자까지 뒤집으면 1111111이 되어서 두 번만에 모두 같은 수자로 만들 수 있다.

하지만, 처음부터 4~5번째 문자만 뒤집으면 한번에 0000000이 되어서 1번 만에 모두 같은 숫자로 만들 수 있다.

문자열 S가 주어졌을 때, 다솜이가 해야 하는 행동의 최소 횟수를 출력하세요.

입력
첫째 줄에 0과 1로만 이루어진 문자열 S가 주어집니다. S의 길이는 100만보다 작습니다.

출력
첫째 줄에 다솜이가 해야 하는 행동의 최소 횟수를 출력합니다.
"""

num_list = list(map(int,list(input())))

zero_to_one_count = 0
one_to_zero_count = 0

if num_list[0]==0:	#첫 연속된 숫자 뒤집기
	zero_to_one_count+=1
else:
	one_to_zero_count+=1

for i in range(len(num_list)-1):	#0->1, 1->0 숫자 뒤집는 횟수 계산
	if num_list[i] != num_list[i+1]:
		if num_list[i+1] == 1:
			one_to_zero_count+=1
		else:
			zero_to_one_count+=1

print(min(zero_to_one_count,one_to_zero_count))