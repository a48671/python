# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определите параметры, общие для приведённых типов. В классах-наследниках реализуйте параметры,
# уникальные для каждого типа оргтехники.


class Store:

    def add_item(self, item: dict, quantity: int) -> None:
        if not isinstance(quantity, int):
            print('quantity not a number')
            return

        if hasattr(self, item.type):
            for index in range(quantity):
                getattr(self, item.type).append(item)
        else:
            for index in range(quantity):
                if index == 0:
                    setattr(self, item.type, [item])
                else:
                    getattr(self, item.type).append(item)


    def get_quantity_all(self):
        count = 0
        for item in self.__dict__:
            count += len(getattr(self, item))
        return count

    def get_quantity_by_type(self, equipment_type: str):
        if hasattr(self, equipment_type):
            return len(getattr(self, equipment_type))
        else:
            return 0


class Equipment:

    def __init__(self, equipment_type: str, name: str):
        self.type = equipment_type
        self.name = name


class Scanner(Equipment):

    def __init__(self, equipment_type: str, name: str, model: str, dpi: str):
        super().__init__(equipment_type, name)
        self.model = model
        self.dpi = dpi

    def __str__(self):
        return f'equipment_type: {self.type}, name: {self.name}, model: {self.model}'


class Xerox(Equipment):

    def __init__(self, equipment_type: str, name: str, model: str, copy_quantity: int):
        super().__init__(equipment_type, name)
        self.model = model
        self.copy_quantity = copy_quantity

    def __str__(self):
        return f'equipment_type: {self.type}, name: {self.name}, model: {self.model}'


class Printer(Equipment):

    def __init__(self, equipment_type: str, name: str, model: str, print_type: str):
        super().__init__(equipment_type, name)
        self.model = model
        self.print_type = print_type

    def __str__(self):
        return f'equipment_type: {self.type}, name: {self.name}, model: {self.model}'


printer_hp = Printer('printer', 'Printer HP', 'hp1010', 'laser')
print(printer_hp)
printer_epson = Printer('printer', 'Printer Epson', 'epson 520p', 'color')
print(printer_epson)
scanner_hp = Scanner('scanner', 'Scanner HP', 'hp310', 1200)
print(scanner_hp)
xerox_hp = Scanner('xerox', 'Xerox HP', 'hp540', 10000)
print(xerox_hp)

store = Store()

store.add_item(printer_hp, 2)
store.add_item(printer_epson, 1)
store.add_item(scanner_hp, 10)
store.add_item(xerox_hp, 3)

print('all equipment: ', store.get_quantity_all())
print('printers: ', store.get_quantity_by_type('printer'))
print('scanners: ', store.get_quantity_by_type('scanner'))
print('xerox: ', store.get_quantity_by_type('xerox'))
print('abracadabra: ', store.get_quantity_by_type('abracadabra'))

