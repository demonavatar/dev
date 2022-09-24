from audioop import reverse


def count_sheep(n):
    if n >= 0 and isinstance(n, int):
        sheepcounter = ''
        for i in range(1,n+1):
            sheepcounter += f'{i} sheep...'
        return sheepcounter
    else:
        raise Exception("You can't input negative integer")

def get_grade(s1, s2, s3):
    avg_grade = sum([s1, s2, s3]) / 3
    if 90 <= avg_grade <= 100: 
        return 'A'
    elif 80 <= avg_grade <= 90:
        return 'B'
    elif 70 <= avg_grade <= 80:
        return 'C'
    elif 60 <= avg_grade <= 70:
        return 'D'
    else:
        return 'F'    

def get_grade1(s1, s2, s3):
    return {6:'D', 7:'C', 8:'B', 9:'A'}.get((s1 + s2 + s3) // 30, 'F')

def string_to_array(s):
    return s.split(' ')

def fake_bin(x):
    new_string = []
    for num in list(x):
        if int(num) < 5:
            new_string.append(0)
        else:
            new_string.append(1)
    return ''.join([str(item) for item in new_string])

def zero_fuel(distance_to_pump, mpg, fuel_left):
    if distance_to_pump/mpg <= fuel_left:
        return True
    else:
        return False

def count_by(x, n):
    multiply_list = []
    while n > 0:
        multiply_list.append(x*n)
        n = n-1
    return list(reversed(multiply_list))

def find_smallest_int(arr):
    return min(arr)

def double_char(s):
    return ''.join(c * 2 for c in s)

def count_positives_sum_negatives(arr):
    if arr:
        counter = 0
        sum_negative = 0
        for item in arr:
            if item > 0:
                counter += 1
            else:
                sum_negative += item
        return [counter, sum_negative]
    return []

def count_positives_sum_negatives1(arr):
    pos = sum(1 for x in arr if x > 0)
    neg = sum(x for x in arr if x < 0)
    return [pos, neg] if len(arr) else []

def century(year):
    # Finish this :)
    return

print(count_positives_sum_negatives([0,0]))