class Employee:
    def __init__(self, name: str, iden: str) -> None:
        self.name = name
        self.iden = iden

    def get_info(self) -> str:
        return f'Имя: {self.name}, Идентификационный номер: {self.iden}'


class Manager(Employee):
    def __init__(self, name: str, iden: str, departament: str) -> None:
        Employee.__init__(self, name, iden)
        self.departament = departament

    def manage_project(self) -> str:
        return f'Менеджер {self.name} управляет в отделе: {self.departament}'

class Technician(Employee):
    def __init__(self, name: str, iden: str, specialization: str) -> None:
        Employee.__init__(self, name, iden)
        self.specialization = specialization

    def perform_maintenance(self) -> str:
        return f'Тех. специалист {self.name} обслуживает в области {self.specialization}'

class TechManager(Manager, Technician):
    def __init__(self, name: str, iden: str, specialization:str, departament: str) -> None:
        Manager.__init__(self, name, iden, departament)
        Technician.__init__(self, name, iden, specialization)
        self.team = []

    def add_employee(self, employee: str) -> None:
        self.team.append(employee)

    def get_team_info(self) -> str:
        return "Список подчинённых:\n" + "\n".join(self.team)


emp_1 = Employee('Кирилл', '1')
emp_2 = Employee('Максим', '2')
emp_3 = Employee('Илья', '3')
print('Список сотрудников:')
print(emp_1.get_info())
print(emp_2.get_info())
print(emp_3.get_info())

mng_1 = Manager('Сергей', '4', 'IT')
print('Список менеджеров:')
print(mng_1.get_info())
print(mng_1.manage_project())

thc_1 = Technician('Павел', '5', 'Серверное оборудование')
thc_2 = Technician('Иван', '6', 'Техническое оборудование')
print('Список специалистов:')
print(thc_1.get_info())
print(thc_2.get_info())
print(thc_1.perform_maintenance())
print(thc_2.perform_maintenance())

thcmng_1 = TechManager('Аркадий', '7', 'Настройка оборудования', 'IT')
print('Тех. менеджер:')
print(thcmng_1.get_info())
print(thcmng_1.manage_project())
print(thcmng_1.perform_maintenance())
thcmng_1.add_employee(emp_1.get_info())
thcmng_1.add_employee(emp_2.get_info())
thcmng_1.add_employee(emp_3.get_info())
thcmng_1.add_employee(mng_1.get_info())
thcmng_1.add_employee(thc_1.get_info())
thcmng_1.add_employee(thc_2.get_info())
print(thcmng_1.get_team_info())


