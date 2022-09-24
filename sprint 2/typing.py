from typing import Union


# Аргумент x может принимать целое число или строку
def hundreds(х: Union[int, str]) -> str:
    return str(х * 100)

print(hundreds(100))
print(hundreds('сто')) 