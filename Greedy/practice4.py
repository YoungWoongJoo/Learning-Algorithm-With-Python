"""
만들 수 없는 금액

동네 편의점의 주인은 N개의 동전을 가지고 있습니다. 이때 N개의 동전을 이용하여 만들 수 없는 양의 정수 금액 중 최솟값을 구하는 프로그램을 작성하세요.

예를 들어, N=5이고, 각 동전이 각각 3원, 2원, 1원, 1원, 9원짜리 동전이라고 가정할 때, 만들 수 없는 양의 정수 금액 중 최솟값은 8원이다.

또 다른 예시로, N=3이고, 각 동전이 각각 3원, 5원, 7원짜리 동전이라고 가정할때, 만들 수 없는 양의 정수 금액 중 최솟값은 1원이다.

입력
첫째 줄에는 동전의 개수를 나타내는 양의 정수 N이 주어진다.(1<=N<=1000)
둘째 줄에는 각 동전의 화폐 단위를 나타내는 N개의 자연수가 주어지며, 각 자연수는 공백으로 구분한다. 각 화폐 단위는 1000000 이하의 자연수

출력
첫째 줄에는 주어진 동전들로 만들 수 없는 양의 정수 금액 중 최솟값을 출력한다.
"""

coin_count=int(input())
coin_unit=list(map(int,input().split()))
coin_unit.sort()
price=1

for i in range(coin_count):	#작은 화폐부터 더해가며 만들수있는지 확인
	if price<coin_unit[i]:		
		break
	else:											
		price+=coin_unit[i]

print(price)