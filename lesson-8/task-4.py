# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определите параметры, общие для приведённых типов. В классах-наследниках реализуйте параметры,
# уникальные для каждого типа оргтехники.


class Store:

    def add_item(self, item: dict) -> None:
        if hasattr(self, item.type):
            getattr(self, item.type).append(item)
        else:
            setattr(self, item.type, [item])


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

store.add_item(printer_hp)
store.add_item(printer_epson)
store.add_item(scanner_hp)
store.add_item(xerox_hp)

print(store.printer)
print(store.scanner)
print(store.xerox)
