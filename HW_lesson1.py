# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) 


# a  = '130'
# b = int (a[0])
# c = int (a[1])
# d = int (a[2])
# print (type(b))
# print (b + c + d) 


# ____________________________
# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# *Пример:*
# 6 -> 1  4  1
# 24 -> 4  16  4
#     60 -> 10  40  10

# print ('Введите итоговую суумму журавликов')
# s = int (input())   
# p = (s / 6)             
# k = ((s / 6)*4)         
# se = p
# print (f' {s} -> {p} {k} {se}')


# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*

# 385916 -> yes
# 123456 -> no


# print ('введите номер Вашего билета!')
# NumTicket = input ()
# print (NumTicket)

# a = int (NumTicket[0])
# b = int (NumTicket[1])
# c = int (NumTicket[2])
# d = int (NumTicket[3])
# e = int (NumTicket[4])
# f = int (NumTicket[5])

# if (a + b + c == d + e + f):
#     print (f'{NumTicket} -> yes')


# else:
#      print (f'{NumTicket} -> no')























