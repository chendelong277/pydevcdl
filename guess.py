import random as r

for i in range(2):
    number=r.randint(1,100)
    running=1
    while running:
        guess = int(input('猜大小！请输入一个数字:'))
        if guess==666:
            print('彩蛋！游戏结束。')
            if i != 2:
                print('请再来一局游戏')
            break
        if guess==0:
            print('不算数，再来一次！')
            continue
        if guess==number:
            print('你猜对了！')
            print('但是这个游戏没有奖励...')
            running=0
            if i != 2:
                print('请再来一局游戏')
        elif guess <= number:
            print('数字小了，请再试一次')
        else:
            print('数字大了，请再试一次')

print('游戏结束。')