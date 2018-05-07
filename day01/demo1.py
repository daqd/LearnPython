# 输出语句
print("Hello World!")

# 定义变量
message = "定义一个小小的变量！"
print('哈哈！'+message)

# 简单的几个方法
methodTest = 'hello,mengyu Mi!'
print(methodTest.title())
print(methodTest.upper())
print(methodTest.lower())

# 简单的数字运算
print((2+3)**2)

# 定义数字，打印数字
num = 23
print('刚刚定义的数字为：'+str(num))

# Python成为列表 JS中成为数组
Array = ['mao','gou','zhu']
print(Array[0].title())

# 末尾追加元素
Array.append('ren')
print(Array[-1].title())

# 指定位置追加元素
Array.insert(2,'shen')
print(Array)

###### 数组练习 #######
# 你现在是真新镇的小智，你打算开启你的宠物小精灵的冒险之旅了。你在出发之前就已经有很多的小伙伴了：皮卡丘、小火龙、杰尼龟、妙蛙种子、以及火爆猴。
# 1、创建一个列表将你的宠物小精灵装进列表
animals = ['皮卡丘','小火龙','杰尼龟','妙蛙种子','火爆猴']

# 2、对你的每一只宠物小精灵都打一个招呼，说一句话
print('hello '+animals[0])
print('hello '+animals[1])
print('hello '+animals[2])
print('hello '+animals[-2])
print('hello '+animals[-1])

# 3、火爆猴突然生病了，所以火爆猴就离开了队伍
animals.pop()
print(animals)

# 5、火爆猴走了以后大钳蟹自告奋勇说想加入你的队伍，于是大钳蟹加入
animals.append('大钳蟹')

# 6、对大钳蟹打一个招呼
print('hello ' + animals[-1])

# 7、这时候大木博士对你说他的臭臭泥也想跟你一起旅行，所以你又把臭臭泥加了进来，并且打印一条跟臭臭泥打招呼的话。
animals.insert(0,'臭臭泥')
print('hello ' + animals[0])

# 8、这时候你觉得这么多小伙伴应该排排位，谁是大哥谁是二哥要分清楚，于是你把列表重新排序了一下，顺序必须是：臭臭泥、杰尼龟、皮卡丘、妙蛙种子、小火龙。
animals.sort()
print(animals)
# 9、你想了一下，你觉得你刚才把顺序给弄反了，于是你把排序给反过来了：小火龙、妙蛙种子、皮卡丘、杰尼龟、臭臭泥
animals.reverse();
print(animals)
# 10、你终于要出发了，然后你又在终端上面确认了一下到底有多少个宠物小精灵跟你一起上路。
print(len(animals))

# 循环列表
for aniItem in animals:
    print(aniItem)

# 元组
Demo = (1,2,3,4)
## 注：元组中的项不可单独修改，可以全部重新赋值

 