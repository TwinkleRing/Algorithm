a, b = input().split()
x = int(a)
y = int(b)


sum = 0
while(x <= y):
    sum = sum + x
    x = x+1

print(sum)


def adder(a, b):
    	if a == b:
		return a
	elif a < b:
		return sum(list(range(a, b+1)))
	else:
		return sum(list(range(b, a+1)))


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( adder(3, 5))