# # list = [10,9,8,7,6,5,4,3,2,1]
# for i in range(-10,0):
#     n = i * -1
#     print(n)  
#     if n == 1:
#         print('Старт!')

# request = int(input('Введите число: '))
# n = request * -1
# for i in range(n,0):
#     int = i * -1
#     print(int)


# list = [1,2,3,4,5,6,7,8,9]
# list2 = [9,8,7,6,5,4,3,2,1]

# for i in list:
#     print(f'{i} * 9 = {i * 9}')


# num = 12345
# str_num = str(num)
# list_str = list(str_num)
# int_list = []
# for i in list_str:


request = int(input('Введите число: '))
while request == 0:
    request += request 
else:
    print(sum(request))






