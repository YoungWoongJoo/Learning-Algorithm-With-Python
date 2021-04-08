"""
모험가 길드

한 마을에 모험가가 N명 있습니다. 모험가 길드에서는 N명의 모험가를 대상으로 '공포도'를 측정했는데, '공포도'가 높은 모험가는 쉽게 공포를 느껴 위험 상황에서 제대로 대처할 능력이 떨어집니다. 모험가 길드장은 모험가 그룹을 안전하게 구성하고자 공포도가 X인 모험가는 반드시 X명 이상으로 구성한 모험가 그룹에 참여해야 하도록 규정했습니다. 

N명의 모홈가에 대한 정보가 주어졌을 때, 여행을 떠날 수 있는 그룹 수의 최댓값을 구하는 프로그램을 작성하시오.

몇 명의 모험가는 마을에 남아 있어도 되기 때문에, 모든 모험가를 특정한 그룹에 넣을 필요는 없다.

입력
첫째 줄에 모험가의 수 N이 주어집니다.(1<=N<=100000)
둘째 줄에 각 모험가의 공포도의 값을 N 이하의 자연수로 주어지며, 각 자연수는 공백으로 구분합니다.

출력
여행을 떠날 수 있는 그룹 수의 최댓값을 출력합니다.
"""

n=int(input())
person = list(map(int,input().split()))

person.sort() #오름차순 정렬해서 작은 공포도 모험가부터 그룹결성
group_count = 0
person_in_current_group = 0

for i in person:
	person_in_current_group += 1
	
	if person_in_current_group>=i:
		person_in_current_group = 0
		group_count += 1
	
print(group_count)