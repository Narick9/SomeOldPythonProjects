
import unittest


class Employee():
    """Представляет работника"""

    def __init__(self, first_name, last_name, salary):
        self.f_name = first_name
        self.l_name = last_name
        self.salary = salary

    def give_raise(self, increase=5000):
        """Увеличивает salary на increase (поумолчанию на 5000)"""
        self.salary += increase


class EmployeeTestCase(unittest.TestCase):
    """Тесты для класса Employee"""

    def setUp(self):
        """Создает работника для тестов"""
        self.worker = Employee("Bob", "Spanch", 50000)

    def test_give_default_raise(self):
        """Работает ли со значением по умолчанию?"""
        before_salary = self.worker.salary
        self.worker.give_raise()
        self.assertEqual(before_salary + 5000, self.worker.salary)

    def test_give_custom_raise(self):
        """"Работает ли со заданным значением?"""
        before_salary = self.worker.salary
        self.worker.give_raise(increase=6000)
        self.assertEqual(before_salary + 6000, self.worker.salary)

unittest.main()
        
