Num1 = 0
Num2 = 0
arith = 0
out = 0

while True:
    Num1 = int(input("처음 값을 입력하세요 : "))
    Num2 = int(input("나중 값을 입력하세요 : "))

    print("-(빼기), +(더하기), x(곱하기), /(나누기)")
    arith = int(input("원하는 작업을 선택하세요 : "))
    
    if (arith == '+'):      out = (Num1 + Num2)
    elif (arith == '-'):    out = (Num1 - Num2)
    elif (arith == 'x'):    out = (Num1 * Num2)
    elif (arith == '/'):    out = (Num1 / Num2)

    else:
        print("값이 잘못되었습니다. 다시 입력하세요.")
        out = ''

    print(out)