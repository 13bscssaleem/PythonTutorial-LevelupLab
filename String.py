testlist = [1,2,3,2,2,2]

testlist.append(100)
testlist.append(1000)

testlist.reverse()
testlist.pop()
test2=testlist.copy()
testlist.remove(2)
testlist.insert(1,200)
testlist.sort()
#testlist.clear()
print(testlist.count(2))
print(testlist)

# list as stack --- last in first out
stack = [1,2,3]

stack.pop()

print(stack)

stack.append(222)
print(stack)

#queue

from collections import deque
queue = deque(["anderson","Peterson", "Johnson"])

queue.popleft()

print(queue)

queue.append("Terry")

print(queue)

#first in first out!
