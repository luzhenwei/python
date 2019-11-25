
import random
import numpy
NUM = 20
resultList = [];
for i in range(NUM):
    m = random.randint(65,90)
    n = chr(m)
    resultList.append(n)
print(resultList)

##列表推导式

result = [chr(random.randint(65,90))  for i in range(NUM)]
print(result)

##引用numpy 实现打印随机数

numpyResult = [chr(i) for i in numpy.random.randint(65,90,[NUM,1])]

print(numpyResult)
