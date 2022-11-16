l = [1, 3, "m"]
print(l)
l.append("v")
print(l)

numbers = [n for n in range(1, 6)]
for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2
print(numbers)

### 1 ###
lv = []
for i in range(1, 6):
    lv.append(i)
print(lv)

### 2 ###
# list comprehension
lt = [n for n in range(1, 6)]
print(lt)
