t = (4, 7, 9)
s = "Ich bin ein String"
l = [45, 98, "787", [3, 4]]
t2 = (4, 8, [45, 98])

t[0]
# t[3]          # IndexError('tuple index out of range')
# t(3)          # TypeError: 'tuple' object is not callable
s[4]
# s[4] = "x"    # TypeError: 'str' object does not support item assignment
# l[2][0] = "g" # TypeError: 'str' object does not support item assignment
l[3][0] = "g"
l
t2[2][0] = 42