# -*- coding:utf-8 -*-

#
# Assignment 5
#
# 어떤 수 2개를 입력 받아 두 수를 더한 후
# 그 결과가 100보다 크면 "100보다 커요."를 출력하고
# 그 외에는 "100보다 작아요."를 출력하는 프로그램을 작성하세요.
#
# 예:
# 첫 번째 숫자를 입력하세요
# 50
# 두 번째 숫자를 입력하세요
# 70
# 100보다 커요.
print("첫 번째 숫자를 입력하세요.")
숫자1 = int(input())
print("두 번째 숫자를 입력하세요.")
숫자2 = int(input())
더한값 = 숫자1 + 숫자2
if 숫자1 + 숫자2 > 100:
    print("100보다 커요")
else:
    print("100보다 작아요")
