import csv

from dataclasses import dataclass


@dataclass
class Buyer:
    name: str
    device_type: str
    browser: str
    sex: str
    age: str
    bill: str
    region: str

    # Пользователь Allen Miss. Elisabeth Walton женского пола, 29 лет совершила покупку на 885 у.е. с мобильного браузера Chrome. Регион, из которого совершалась покупка: St Louis: MO.
    def get_report(self):
        return (f"Пользователь {self.name} {self.get_gender_string()}, {self.age} {self.get_age_string()} "
                f"совершил{self.get_action_ending()} покупку на сумму {self.bill} у.е. c {self.get_device_string()}. "
                f"Регион, из которого совершалась покупка: {self.region}")

    def get_gender_string(self):
        return "женского пола" if self.sex == "female" else "мужского пола"

    def get_age_string(self):
        if float(self.age) < 1:
            return 'года'
        rem = int(self.age) % 10

        if rem == 0 or (5 <= rem <= 9):
            return 'лет'
        if rem == 1:
            return 'год'
        if 2 <= rem <= 4:
            return 'года'
        return '-'

    def get_action_ending(self):
        return "а" if self.sex == "female" else ""

    def get_device_string(self):
        match self.device_type:
            case 'mobile':
                return f"мобильного браузера {self.browser}"
            case 'desktop':
                return f"ПК в браузере {self.browser}"
            case 'tablet':
                return f"планшета в браузере {self.browser}"
            case 'laptop':
                return f"ноутбука в браузере {self.browser}"
        return '-'


with open('buyers.csv', newline='') as csv_input, open('out.txt', 'w', newline='', encoding='utf-8') as txt_output:
    reader = csv.reader(csv_input, delimiter=',')
    header = next(reader)
    for row in reader:
        buyer = Buyer(**dict(zip(header, row)))
        txt_output.write(f"{buyer.get_report()}\n")
