"""
First exercise

Доработать класс FlatIterator в коде ниже.
Должен получиться итератор, который принимает список списков и возвращает их плоское представление, т. е.
последовательность, состоящую из вложенных элементов.
Функция test в коде ниже также должна отработать без ошибок.

"""

class FlatIterator:

    def __init__(self, list_of_lists):
        self.list_of_lists = list_of_lists

    def __iter__(self):
        self.outside_index = 0
        self.inside_index = 0
        return self

    def __next__(self):
        while self.outside_index < len(self.list_of_lists):
            if self.inside_index < len(self.list_of_lists[self.outside_index]):
                item = self.list_of_lists[self.outside_index][self.inside_index]
                self.inside_index += 1
                return item
            else:
                self.inside_index = 0
                self.outside_index += 1

        raise StopIteration





def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()



"""
Second exercise

Доработать функцию flat_generator.
Должен получиться генератор, который принимает список списков и возвращает их плоское представление. 
Функция test в коде ниже также должна отработать без ошибок.

"""

import types



def flat_generator(list_of_lists):
    for lst in list_of_lists:
        i = 0
        while i < len(lst):
            yield lst[i]
            i += 1
"""
def flat_generator(list_of_lists):
    for lst in list_of_lists:
        for item in lst:
            yield item
"""

def test_2():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test_2()
