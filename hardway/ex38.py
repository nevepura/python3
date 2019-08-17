ten_things = 'pasta pizza mandolino spaghetti mafia mare sole core'
# 8 now

target = ten_things.split(' ')
print(f'target len is: {len(target)}')

more_things =   [
                    'yellow',
                    'orange',
                    'black',
                    'white',
                    'blue',
                ]

while len(target) != 10:
    to_add = more_things.pop()
    target.append(to_add)
    print(f'There are {len(target)} in target now.')

print(f'Target is ready: {target};\nits length is: {len(target)}')

print(target[1])
print(target[-1])
print(target.pop())
print(' '.join(target))
print(' = '.join(target[3:6]))


a =[1,2,3]
lastitem = a.pop()
# print(a[2]) # error: list index out of range