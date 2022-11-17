from math import sqrt


A = int(input())
B = int(input())
C = int(input())

P = (A+B+C)/2
S = sqrt(P*(P-A)*(P-B)*(P-C))
print(S)
