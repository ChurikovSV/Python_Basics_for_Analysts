# На складе лежат разные фрукты в разном количестве.
# # Нужно написать функцию total_fruits, которая на вход принимает любое количество названий фруктов и их количество, а возвращает общее количество фруктов на складе.
# #
# # можно решить через *kwargs

#print(total_fruits(apples=10, bananas=5, oranges=8))

def total_fruits(**kwargs):
    total = 0
    for fruit, quantity in kwargs.items():
        total += quantity * 1
    return total