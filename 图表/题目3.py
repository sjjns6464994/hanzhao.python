import random

# 生成随机整数
target_num = random.randint(1, 50)
print("我已经准备好了一个1到50之间的整数，请您开始猜测吧！")

# 猜测次数和初始范围
guesses = 0
min_num = 1
max_num = 50

# 循环进行游戏
while guesses < 5:
    guess = int(input("请猜一个数字："))

    # 判断大小，并更新范围
    if guess == target_num:
        print("恭喜你，猜对了！")
        break
    elif guess < target_num:
        print("猜小了！")
        min_num = guess + 1
    else:
        print("猜大了！")
        max_num = guess - 1

    # 更新猜测次数
    guesses += 1

    # 输出当前猜测范围
    print("猜测范围现在是：{}-{}".format(min_num, max_num))

# 猜测次数用尽
if guesses == 5:
    print("很遗憾，您没有在规定次数内猜中数字，游戏结束！")