"""
성적이 낮은 순서로 학생 출력하기

문제
N명의 학생의 성적 정보가 주어진다. 형식은 이름 성적 으로 주어지는데 이때 이들의 성적이 낮은 순으로 학생 이름을 출력하는 문제다.

입력
첫 번째 줄에 학생의 수 N이 입력된다. (1 <= N <= 100,000)
두 번째 줄 부터 N+1 번째 줄 까지 학생의 이름 그리고 성적이 공백으로 주어진다. 학생이름 길이는 100이하, 성적은 100이하 자연수로 주어진다.

출력
모든 학생의 이름을 성적이 낮은 순으로 출력하면된다. 동일한 성적은 자유롭게 출력하면된다.

"""

n=int(input())

score_list=[]

for i in range(n):
	name,score=input().split()
	score_list.append((name,int(score)))

score_list.sort(key=lambda x:x[1])

for data in score_list:
	print(data[0], end=' ')