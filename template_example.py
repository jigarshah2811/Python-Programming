template = '''\
def {name}power(exp):
    return {base} ** exp
'''

"""
list_names = {
        ('name' :'two', base : 2),
        ('name' : 'three', base : 3),
        ('name' : 'four', base : 4)
    }

for name in list_names:
    exec template.format(name)
"""
lists = [[] for i in range(3)]
print lists

# exec template.format('name={0.name}, base={0.base}').[format(list_name) for list_name in list_names]
exec template.format(name='two', base=2)
exec template.format(name='three', base=3)
exec template.format(name='four', base=4)

print twopower(3)
print threepower(3)
print fourpower(3)
