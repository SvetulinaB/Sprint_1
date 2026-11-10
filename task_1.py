time_string = '1h 45m,360s,25m,30m 120s,2h 60s'

#1.Используем метод replace(), чтобы поменять запятые в time_string на пробел
time_string_1 = time_string.replace(',', ' ')

#2.Разделителем split() разделим содержимое строки, чтобы получить список
time_list = time_string_1.split()

#3.Переменная для результата
total_min = 0

#4.Создаем цикл с условием: если h (убираем текст, превращаем в число (int)), умножаем на 60; если m, оставляем; если s, делим на 60. Все добавляем в результат total_min.
for time in time_list:
    if 'h' in time:
        h_text = time.replace('h', '')
        h_number = int(h_text)
        total_min += h_number * 60

    elif 'm' in time:
        m_text = time.replace('m', '')
        m_number = int(m_text)
        total_min += m_number

    elif 's' in time:
        s_text = time.replace('s', '')
        s_number = int(s_text)
        total_min += s_number//60

#5.Выводим результат
print(total_min)