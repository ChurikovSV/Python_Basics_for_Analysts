# Найдите выручку компании в зависимости от месяца Для этого напишите функцию calc_income_by_month(), которая на вход принимает список с датами и список с выручкой, а на выходе словарь, где ключи - это месяцы, а значения - это выручка. Используйте аннотирование типов.

dates = ['2021-10-01', '2021-11-05', '2021-12-10']
incomes = [100, 200, 300]

def calc_income_by_month(dates: list, incomes: list) -> dict:
    res = {}
    for d, m in zip(dates, incomes):
        if d[5:7] in res.keys():
            res[d[5:7]] = res[d[5:7]] + m
        else:
            res[d[5:7]] = m
    return res

print(sum_in_month(dates, incomes))