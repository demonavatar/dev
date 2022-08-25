# case 9.2.1

from typing import Sequence


def lower_join(seq: Sequence[str]) -> str:
    """Принимает на вход последовательность и создаёт из неё
    строку в нижнем регистре."""
    return ''.join(seq).lower()

# case 9.2.2

from typing import List, Union


def series_sum(incoming: List[Union[str, float]]) -> str:
    """Принимает на вход список из строк и чисел с плавающей точкой, приводит его элементы к строкам и конкатенирует их.
    """
    result = ''
    for i in incoming:
        result += str(i)
    return result

# case 9.2.3

from typing import Callable


def add(number: float, callback: Callable[[float], float]) -> float:
    """Производит арифметические действия с числами.
    Принимает число и функцию, выполняющую арифметическое действие.
    """    
    return callback(number)


def adder20(number: float) -> float:
    """Добавляет к аргументу 20."""
    return number + 20


def multiplier2(number: float) -> float:
    """Умножает аргумент на 2."""
    return number * 2