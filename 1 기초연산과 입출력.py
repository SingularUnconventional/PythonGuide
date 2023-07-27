"""
변수에 값을 할당하는 방법이다.
변수는 변하는 수로 직접 선언하고 변경할 수 있다.
"""

#a는 1로 정한다.
a = 1

#b는 2로 정한다.
b = 2

#c는 23으로 정한다.
c = 23

#c를 a와 b를 더한 값으로 변경한다.
c = a + b

"""
여기서 중요한 것은 a = b 일때 a를 b로 정하는 거기 때문에 순서가 바뀌면 안된다.
값을 정했으므로 이 값을 직접 확인해야 하는데 이 방법으로 print 라는 함수를 사용한다.
print는 실행했을때 나오는 창에 우리가 볼 수 있도록 값을 보여주는 함수이다.
"""

#1을 보여준다.
print(1)
#--> 1

"""
문자를 출력하기 위해서는 큰따옴표("")나 따옴표('')를 사용한다.
"""

#Hello, world를 출력한다.
print('Hello, world')
#--> Hello, world

#위에서 정한 값인 c를 출력한다.
#여기선 c의 값이 1인 a와 2인 b가 더해진 값이므로 3을 가지게 된다. 그렇기 때문에 3이 출력된다.
print(c)
#--> 3


"""
우리가 실행 도중에 값을 입력받는 방법으로 input을 사용할 수 있다.
"""

#'값을 입력하세요'가 출력되고 키보드 입력을 받을 수 있게 된다.
print('값을 입력하세요')
input()
#이는 input('값을 입력하세요') 로 줄일 수 있다.

#우리는 앞에서 "a = 1"이 "a를 1로 정한다." 라는 것을 배웠다. 그러면 a의 값을 입력받은 값으로 하려면 어떻게 해야할까
a = input('값을 입력하세요')
#이렇게 하면 a의 값은 우리가 입력한 값으로 만들 수 있다.

#입력받은 값을 출력한다.
print(a)

# '-->'는 실행결과를 나타내며, '==>' 이후에 값은 능동적인 입력값이다.
"""
-->
1
Hello, world
3
'값을 입력하세요' ==> 1234
'값을 입력하세요' ==> asdf
asdf
"""