num=0
a=0
try:
    while 1:
        while a==0:
                try:
                    n=int(input("부를 숫자의 개수를 입력하세요(1,2,3만 입력 가능):"))

                    if n!=1 and n!=2 and n!=3 :
                        print('1,2,3 중 하나를 입력하세요')
                    else:
                        for i in range(n) :
                            num+=1
                            print('playerA:',num)
                            if num==31:
                                raise Exception
                        n=0
                        a=1
                except ValueError:
                    print('정수를 입력하세요.')
        a=0

        while a==0:
                try:
                    n=int(input("부를 숫자의 개수를 입력하세요(1,2,3만 입력 가능):"))

                    if n!=1 and n!=2 and n!=3 :
                        print('1,2,3 중 하나를 입력하세요')
                    else:
                        for i in range(n) :
                            num+=1
                            print('playerB:',num)
                            if num==31:
                                raise Exception
                        n=0
                        a=1
                except ValueError:
                    print('정수를 입력하세요.')
        a=0
except Exception:
    print()
