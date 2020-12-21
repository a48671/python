isInputMode = True

products = []
current_product = {}

isAddProduct = False

while isInputMode:

    if not isAddProduct:
        isAddProduct = input('Хотите добавить товар? да/нет: ')

    if isAddProduct != 'нет' and isAddProduct != 'да':
        print('Ответ может быть либо "да" либо "нет"')
        isAddProduct = False
        continue

    elif isAddProduct == 'нет':
        break
    if 'name' not in current_product:
        name = input('Введите название товара: ')
        current_product['name'] = name
    elif 'price' not in current_product:
        try:
            price = float(input('Введите цену товара: '))
            current_product['price'] = price
        # не знаю какой здесь class исключения указать
        except:
            print('Цена может состоять только из цифр')
            continue
    elif 'quantity' not in current_product:
        try:
            quantity = int(input('Введите количество товара: '))
            current_product['quantity'] = quantity
        # не знаю какой здесь class исключения указать
        except:
            print('Количество может состоять только из цифр')
            continue
    elif 'units' not in current_product:
        units = input('Введите еденицу измерения товара: ')
        current_product['units'] = units
    else:
        isAddProduct = False
        products.append((len(products), current_product))
        current_product = {}


analytics = {
    'название': [],
    'цена': [],
    'количество': [],
    'ед': []
}

print(products)

for product in products:
    product_data = product[1]
    analytics['название'].append(product_data['name'])
    analytics['количество'].append(product_data['quantity'])
    analytics['цена'].append(product_data['price'])
    analytics['ед'].append(product_data['units'])

print(analytics)
