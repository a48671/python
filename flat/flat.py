arr = [1, 2, 3, [4, 5, [6, 7], 8], 9]


def flat(array: list) -> list:
    task_stack: list = []

    new_array: list = []

    index: int = 0

    def flatting(array_from_stack: list):

        for i, el in enumerate(array_from_stack):
            if type(el) == list:
                flatted_array = el + [array_from_stack[a] for a in range(i + 1, len(array_from_stack))]
                task_stack.append(lambda: flatting(flatted_array))
                break
            else:
                new_array.append(el)

    while index < len(array):

        item = array[index]

        if len(task_stack) > 0:
            task = task_stack.pop(0)
            task()
            continue
        elif type(item) == list:
            flatting(item)
            index += 1
            continue
        else:
            new_array.append(item)
            index += 1
            continue

    return new_array


print(flat(arr))
