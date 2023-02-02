

def input_class():
    return input('С каким классом работаем? ').upper()

def input_subject():
    return input('Предмет: ').lower()

def who_answer():
    return input('К доске пойдет...  ')

def what_mark():
    return input('Ответ на отметку: ')

def list_of_child(journal: dict):
    for i, child in enumerate(journal, 1):
        print(f'{i}.{child:20} {journal.get(child)}')                