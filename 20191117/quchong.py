
import  random
import itertools

demoList = [random.randint(10,15)  for i in range(10)]
print(demoList)
resultList = []


for i in demoList:
    if i not in resultList:
        resultList.append(i)
print(resultList)

print(list(set(demoList)))

demoList.sort()
result2 = []
result1 = itertools.groupby(demoList);
for k,v in result1:
    result2.append(k)
print(result2)
