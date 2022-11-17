from math import fmod


A = float(input())
B = float(input())
func = (input())

if (B==0 and (func=='/' or func=='mod' or func=='div')):
    print('Деление на 0!')
elif func== '+':
    print(A + B)
elif func== '-':
    print(A - B)
elif func== '/':
    print(A / B)
elif func== '*':
    print(A * B)
elif func== 'mod':
    print(fmod(A, B))
elif func== 'pow':
    print(pow(A, B))
elif func== 'div':
    print(int(A//B))
