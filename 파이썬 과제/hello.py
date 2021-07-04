for i in range(1,101):
    if i%3==0 and i%5==0:
        print('FizzBuzz')
    elif i%3==0:
        print('Fizz')
    elif i%5==0:
        print('Buzz')
    else:
        print(i)

for i in range(1,101):
    if i%15==0:
        print('FizzBuzz')
    elif i%3==0:
        print('Fizz')
    elif i%5==0:
        print('Buzz')
    else:
        print(i)

for i in range(1,101):
    print('Fizz'*(i%3==0)+'Buzz'*(i%5==0) or i)
        # 뭘 출력*언제 출력 + 뭘 출력*언제 출력
          # 둘 다 True면 앞 합쳐서 출력 둘 다 false면 뒤의 i
