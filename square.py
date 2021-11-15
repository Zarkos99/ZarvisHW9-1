# A python script that squares all x values from 0 and 19 utilizing function sq()
def sq():
    global x
    s = x ** 2
    print x, '^2 = ', s
for x in range(20):
    sq()
