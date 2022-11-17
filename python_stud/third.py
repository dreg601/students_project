A = int(input())
H = int(input())
B = int(input())

if A<=H and B>=H:
    print('Это нормально')
elif A<H or B<H:
    print('Пересып')
elif A>H and B>H:
    print('Недосып')