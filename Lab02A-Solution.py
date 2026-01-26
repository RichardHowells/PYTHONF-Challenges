
int_list = [10, 20, 30, 40]
int_list.append(45)
int_list.append(46)
int_list.insert(4, 44)
int_list.insert(4, 43)
int_list.insert(1, 15)
int_list.insert(3, 25)

print(int_list)

print(int_list[0::2])

print(int_list[1::2])

print(int_list[::-1])

int_list[0] = 5
print(int_list)