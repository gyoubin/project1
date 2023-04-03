##메서드 선언부
def add_func(n1, n2):
    return n1+n2
    

def sub_func(n1,n2):
    return n1-n2

def mul_func(n1,n2):
    return n1*n2

def div_func(n1,n2):
    return n1/n2

def squ_func(n1):
    return n1*n1

##전역 변수부(클래스 변수, 인스턴스 변수)
num1, num2, result= 100, 200, 0


##메인 코드부
result=add_func(num1, num2)
print(num1, '+', num2, '=', result)

result =sub_func(num1, num2)
print(num1,'-',num2,'=',result)

result=mul_func(num1, num2)
print(num1,'x',num2,'=',result)

result=div_func(num1, num2)
print(num1,'/',num2,'=',result)

result=squ_func(num1)
print(num1,'^2 =',result)
