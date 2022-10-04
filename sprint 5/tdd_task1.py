def test_sort(sorting_algorithm):
    """ Тестируем алгоритм, сортирующий список по возрастанию."""
    # Напечатать имя функции
    print(f'Тестируем: {sorting_algorithm.__doc__}')
    # Тест со списком, содержащим int и float
    source = [1, 3, 2.5, 4]
    sorted = [1, 2.5, 3, 4]
    assert sorting_algorithm(source) == sorted, (f'Ожидаемый результат: {sorted} для {sorting_algorithm.__name__}({sorting_algorithm(source)})')
    # Тест со списком, содержащим отрицательные величины, нулевое значение
    source = [1, -3, 0, 4]
    sorted = [-3, 0, 1, 4]
    assert sorting_algorithm(source) == sorted, (f'Ожидаемый результат: {sorted} для {sorting_algorithm.__name__}({sorting_algorithm(source)})')
    # Тест со списком, содержащим одинаковые числа
    source = [1, 2, 4, 2]
    sorted = [1, 2, 2, 4]
    assert sorting_algorithm(source) == sorted, (f'Ожидаемый результат: {sorted} для {sorting_algorithm.__name__}({sorting_algorithm(source)})')
    # Тест с пустым списком (всегда стоит проверять граничные значения).
    source = []
    sorted = []
    assert sorting_algorithm(source) == sorted, (f'Ожидаемый результат: {sorted} для {sorting_algorithm.__name__}({sorting_algorithm(source)})')
    print(f'Тест для {sorting_algorithm.__name__} пройден')


test_sort(bubble_sort)
test_sort(timsort_sort)
test_sort(selection_sort)
test_sort(insertion_sort)
test_sort(merge_sort)
test_sort(heap_sort)  
test_sort(quick_sort)
test_sort(sus_sort)