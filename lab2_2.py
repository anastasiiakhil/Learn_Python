import sys

x = int(sys.argv[1])
y = int(sys.argv[2])
z = int(sys.argv[3])

if x < 0 or y < 0 or z not in [0,1]:
    print('error')
else:
    s = 'Every body sing a song:{}'
    s1 = x * 'la-'
    s1 = s1[0:-1]
    s2 = y * (s1+' ')
    s3 = str('!' if z is 1 else '.')
    rez = s.format(s2[0:-1] + s3)
    print(rez)
