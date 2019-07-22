mobile1 = '+989126939411'
mobile2 = '09126939411'
mobile3 = '9126939411'

if 13 >= len(mobile1) >= 10:
    print("mobile1 => " + mobile1 + " => " + str(len(mobile1)))

if 13 >= len(mobile2) >= 10:
    print("mobile2 => " + mobile2 + " => " + str(len(mobile2)))

if 13 >= len(mobile3) >= 10:
    print("mobile3 => " + mobile3 + " => " + str(len(mobile3)))

print(mobile1[-10:-7] + "***" + mobile1[-3:])
print(mobile2[-10:-7] + "***" + mobile2[-3:])
print(mobile3[-10:-7] + "***" + mobile3[-3:])


#
# result = {
#   'a': lambda x: x * 5,
#   'b': lambda x: x + 7,
#   'c': lambda x: x - 2
# }[value](x)

def test2():
    return 'dfgsfsdf' * 10


def f(x):
    return {
        'a': 1,
        'b': 2,
        'c': test2()
    }.get(x, 9)


f('c')
