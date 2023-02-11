gender = {
    'm' : 'Дорогой',
    'f' : 'Дорогая'
}
data_bank = [
    ['Zhdaniuk', 'Ivan', 'm', '400000'],
    ['Kootan', 'Pups', 'm', '10'],
    ['Zhdaniuk', 'Sveta', 'f', '333']
]

for sur_name, name, gend, balanc in data_bank:
    print(f'{gender[gend]} {sur_name} {name} балaнс вашего счета сотавляет {balanc} $.')

