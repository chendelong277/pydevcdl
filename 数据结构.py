def list():
    shoplist=['apple','mango','carrot','banana']
    print('I have', len(shoplist), 'items to purchase')

    print('These items are:', end=' ')
    for item in shoplist:
        print(item, end=' ')
    print('\nI alse have to buy rice.')
    shoplist.append('rice')
    print('My shoplist is now:', shoplist)
    shoplist.sort()
    print('Sorted shopping list is', shoplist)

    print('The first item I will buy is', shoplist[0])
    olditem=shoplist[0]
    del shoplist[0]
    print('I bought the', olditem)
    print('My shopping list is now', shoplist)

def tuple():
    zoo = ('python', 'elephent', 'penguin')
    print('Number if animals in the zoo is', len(zoo))

    new_zoo= 'monkey', 'camel', zoo
    print('Number of cages in the new zoo are', len(new_zoo))
    print('All animals in the new zoo are:', new_zoo)
    print('Animals brought from the old zoo are:', new_zoo[2])
    print('Last animal brought from the old zoo is ', new_zoo[2][2])
    print('Number of animals in the new zoo is ', len(new_zoo)-1+len(new_zoo[2]))
    print(len(new_zoo[2]))

def dict():
    #"ab"是地址（address）簿（book）的缩写
    ab={
        'Swaroop' : 'swaroop@swaroopch.com',
        'Larry' : 'larry@wall.org',
        'Matsumoto': 'matz@ruby-lang.com',
        'Spammer': 'spammer@hotmail.com'
    }
    print("Swaroop's address is ", ab['Swaroop'])

    #删除一对键值=值配对
    del ab['Swaroop']

    print('\nThere are {} contacts in the address-book\n'.format(len(ab)))

    for name,address in ab.items():
        print('Contact {} at {}'.format(name,address))

    #添加一堆键值-值配对
    ab['Guidio']='guidio@python.org'

    if 'Guidio' in ab:
        print("Guidio's address is ", ab['Guidio'])
list()
tuple()
dict()
