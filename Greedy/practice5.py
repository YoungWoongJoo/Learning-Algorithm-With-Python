"""
볼링공 고르기

A,B 두 사람이 볼링을 치고 있습니다. 두 사람은 서로 무게가 다른 볼링공을 고르려고 합니다. 볼링공은 총 N개가 있으며 각 볼링공마다 무게가 적혀 있고, 공의 번호는 1번부터 순서대로 부여됩니다. 또한 같은 무게의 공이 여러 개 있을 수 있지마, 서로 다른 공으로 간주합니다. 볼링공의 무게는 1부터 M까지의 자연수 형태로 존재합니다.

N개의 공의 무게가 각각 주어질 때, 두 사람이 볼링공을 고르는 경우의 수를 구하는 프로그램을 작성하세요.

입력
첫째 줄에 볼링공의 개수 N, 공의 최대 무게 M이 공백으로 구분되어 각각 자연수 형태로 주어집니다.(1<=N<=1000, 1<=M<=10)
둘째 줄에 각 볼링공의 무게 K가 공백으로 구분되어 순서대로 자연수 형태로 주어집니다.
(1<=K<=M)

출력
첫째 줄에 두 사람이 볼링공을 고르는 경우의 수를 출력합니다.
"""

from itertools import combinations

n,m = map(int,input().split())
k=list(map(int,input().split()))

weight_count = [0]*m
result=0

for i in k:
	#weight_count[0]은 무게가 1인 공의 개수, weight_count[1]은 무게가 2인 공의 개수
	weight_count[i-1]+=1

for i in range(m):
	n -= weight_count[i]				#A가 먼저 고르고 남은 것을 B가 골라야하기 때문에
	result += weight_count[i]*n			

print(result)
