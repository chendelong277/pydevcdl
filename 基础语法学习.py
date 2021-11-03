print('''
There are two lines here, and this is the first one.
It's nice that you come.''')

print('{0:.3f}'.format(1.0/3))#1/3，保留三位小数
print('{0:_^11}'.format('hello'))
print("{name} wrote {book}".format(name='Swaroop', book='A byte of python'))
print("a", end='')
print('b')
i=5
print(i)
j=4
print('{num0}的{num1}次方等于{num2}'.format(num0=i,num1=j,num2=i**j))
i=i+1
print('{num0}加{num1}等于{num2}'.format(num0=i,num1=j,num2=i+j))
s='''This is the first line,
this is the second line.'''
print(f'{s}')