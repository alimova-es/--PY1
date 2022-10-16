money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить

# TODO Оформить решение
while True:
    money_capital += (salary - spend)
    if money_capital <= 0:
        break
    month += 1
    spend *= 1.05

print(month)
