class TestCase: #создали класс
    def __init__(self): #вызвали конструктор init, добавили поля из задания
        self.steps = {}
        self.result = None

    def set_step(self, step_number, step_text): #метод чтобы что-то делать
        self.steps[step_number] = step_text #добавляем в словарь шаг тест-кейса

    def delete_step(self, step_number):
        self.steps.pop(step_number) #удаляем шаг по step_number

    def set_result(self, result):
        self.result = result #результат по result

    def get_test_case(self): #вывод на печать словаря с шагами и результатами
        report = {
            'Шаги': self.steps,
            'Ожидаемый результат': self.result

        }
        print(report)

test_case_1 = TestCase()
test_case_1.set_step(1, 'Перейти на сайт')
test_case_1.set_step(3, 'Перейти в раздел Товары')
test_case_1.delete_step(3)
test_case_1.set_step(2, 'Перейти в раздел Товары')
test_case_1.set_step(3, 'Нажать кнопку «В корзину» у первого товара')
test_case_1.set_result('Товар окажется в корзине')
test_case_1.get_test_case()

test_case_2 = TestCase()
test_case_2.set_step(1, 'Перейти на сайт')
test_case_2.set_step(2, 'Перейти в раздел Корзина')
test_case_2.set_step(3, 'Нажать кнопку "Удалить"')
test_case_2.set_result('Товар удален из корзины')
test_case_2.get_test_case() 