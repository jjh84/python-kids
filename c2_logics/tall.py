# -*- coding:utf-8 -*-

#
# 키가 180보다 크거나 같으면, "키가 크다."를 출력
# 키가 150보다 크거나 같고 180보다 작으면, "키가 보통이다."를 출력
# 그외 나머지는 "키가 작다."를 출력
#

print("키를 입력하세요.")
키 = int(input())

if 키 >= 180:
    print("키가 크다.")
elif 키 >= 150 and 키 < 180:
    print("키가 보통이다.")
else:
    print("키가 작다.")
