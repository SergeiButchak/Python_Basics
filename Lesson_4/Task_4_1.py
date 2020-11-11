from sys import argv

try:
    hours_worked, pay_per_hour, reward = argv[1:]
    payment = int(hours_worked) * int(pay_per_hour) + int(reward)
    print(f"Заработная плата = {payment}")
except Exception as exc:
    print(exc)
