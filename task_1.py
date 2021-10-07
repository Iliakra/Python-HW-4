""" Красильников Илья
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника. В расчете
необходимо использовать формулу: (выработка в часах * ставка в час) + премия. Для выполнения расчета для конкретных
значений необходимо запускать скрипт с параметрами.
"""

from sys import argv


script_name, production_hours, hour_rate, prize = argv


def salary_calculate(script_name, production_hours, hour_rate, prize):
    result = float(production_hours) * float(hour_rate) + float(prize)
    print(f"Заработная плата, рассчитанная в {script_name} равна {result} руб.")


salary_calculate(script_name, production_hours, hour_rate, prize)
