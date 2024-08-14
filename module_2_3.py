my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
i = 0
# Только положительные до "0"
while i < len(my_list):
    if my_list[i] <= 0:
         print(f'Нули ничто! {my_list[i]}')
         break
    else:
    #elif my_list[i] > 0:
        print(f'{my_list[i]} - это не отрицательное число')
        i += 1
# Только все положительные
while i < len(my_list):
    if my_list[i] >= 0:  #in [0, -5, -6]:
        i += 1
        continue
    else:
        print(f'{my_list[i]} - отрицание недопустимо')
        i += 1

