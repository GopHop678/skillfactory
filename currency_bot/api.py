import requests
import json


def get_value(string):
    try:
        first_curr = string[0:3]
        second_curr = string[3:6]
        amount = float(string[7:])
        r = requests.get(f'https://open.er-api.com/v6/latest/{first_curr}')
        texts = json.loads(r.content)
        mult = (texts[f'rates'][f'{second_curr}'])
        return round(mult * amount, 2)
    except:
        return 'Что-то пошло не так...'


def values():
    r = requests.get(f'https://open.er-api.com/v6/latest/aed')
    texts = json.loads(r.content)
    values_dict = texts[f'rates']
    return ', '.join(list(values_dict.keys()))


if __name__ == '__main__':
    print(values())
    print(get_value('gbpusd 100'.upper()))
