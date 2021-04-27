"""
문자열 재정렬

문제
알파벳 대문자와 숫자 (0~9)로만 구성된 문자열이 입력으로 주어집니다. 이때 모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤에, 그 뒤에 모든 숫자를 더한 값을 이어서 출력합니다. 예를 들어 K1KA5CB7이 입력으로 들어오면, ABCKK13을 출력합니다.

입력
첫째 줄에 하나의 문자열 S가 주어집니다. (1<=S의길이<=10000)

출력
첫째 줄에 문제에서 요구하는 정답을 출력합니다.
"""

s=input()

sum=0
char_list=[]

for value in s:
	if value.isalpha():	#입력받은 문자열의 문자가 알파벳이면 리스트에 추가
		char_list.append(value)
	else:
		sum+=int(value)	#문자가 알파벳이 아니면 숫자형변환하여 누적

char_list.sort()	#알파벳문자열 오름차순 정렬

if sum!=0:	#입력받은 문자열 안에 숫자가 하나이상있으면 정렬된 리스트 마지막에 추가
	char_list.append(str(sum))

print(''.join(char_list))