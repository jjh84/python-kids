# -*- coding:utf-8 -*-

#
# 입력한 숫자가 짝수인지 홀수인지 판단하는 프로그램
# 주어진 숫자를 2로 나누었을 때 나머지가 0이면 짝수이고 그렇지 않으면 홀수 이다.
#

print('숫자를 입력하세요.')
숫자 = int(input())

if 숫자 % 2 == 0:
    print("짝수 입니다.")
else:
    print("홀수 입니다.")
