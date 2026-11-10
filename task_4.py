new_tasks = ['task_001', 'task_011', 'task_007', 'task_015', 'task_005']
completed_tasks = ['task_002', 'task_012', 'task_006']

#1.Переносим task_005 в другой список с помощью метода pop() в одно действие. Индекс не передаем, pop по умолчанию удалит и вернет последний элемент, т.е.task_005.
completed_tasks.append(new_tasks.pop())

#2.Удаляем task_007 из списка по значению методом remove().
new_tasks.remove('task_007')

#3.Выводим с помощью print() последний запрос на экран по индексу -1 (первый с конца).
print(new_tasks[-1])