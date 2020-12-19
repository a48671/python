state = {'total': 0, 'isContinue': True}

def list_to_sum(array):
    for item in array:
        if not item.isdigit() or item == 'z':
            state['isContinue'] = False
            break
        else:
            state['total'] = state['total'] + float(item)

while state['isContinue']:
    array = input('Input numbers: ').split()
    list_to_sum(array)
    print(f'Total: {state["total"]}')