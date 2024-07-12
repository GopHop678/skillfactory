from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import KeyboardBuilder
import texts

questions = {
    'appearance': 'Какой окрас животного вы бы предпочли?',
    'pref_food': 'Какая ваша любимая еда?',
    'activities': 'Каков ваш образ жизни?',
    'personality': 'Какой характер у вашего животного?',
    'attention': 'Сколько внимания требует ваше животное?',
    'training': 'Поддается ли оно дрессировке?',
    'caring': 'Насколько оно неприхотиливо?',
    'size': 'Какого размера животное вы хотели бы?',
    'environment': 'Какую среду обитания вы выберите?'
}

answers = {
    'appearance': ['Яркий', 'Нейтральный', 'Темный'],
    'pref_food': ['Морепродукты', 'Мясо', 'Фрукты', 'Овощи', 'Орехи'],
    'activities': ['Активный', 'По настроению', 'Ленивый'],
    'personality': ['Игривый', 'Дружелюбный', 'Нелюдимый'],
    'attention': ['Все время', 'Много времени', 'Немного времени', 'Мало времени'],
    'training': ['Да', 'Возможно', 'Нет'],
    'caring': ['Неприхотливый', 'Минимум требований', 'Требовательный'],
    'size': ['Крупного', 'Среднего', 'Совсем небольшого'],
    'environment': ['На суше', 'В воде', 'В воздухе']
}

start_btn = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Начнём!')]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

about_inline_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Наш Телеграмм-канал', url='t.me/Moscowzoo_official')],
    [InlineKeyboardButton(text='Мы ВКонтакте', url='https://vk.com/moscow_zoo')],
    [InlineKeyboardButton(text='Наш сайт', url='https://moscowzoo.ru/')],
    [InlineKeyboardButton(text='Наш YouTube-канал', url='https://www.youtube.com/@Moscowzooofficial')]
])

result_inline_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='О программе опеки', url='https://moscowzoo.ru/about/guardianship')],
    [InlineKeyboardButton(text='Пройти викторину сначала', callback_data='restart')]
])


def get_answers(no_question, back_btn=True):
    builder = KeyboardBuilder(button_type=KeyboardButton)
    for answer in answers[no_question]:
        builder.add(KeyboardButton(text=answer))
    if back_btn:
        builder.add(KeyboardButton(text='Вернуться назад'))
    builder.adjust(2, 3, repeat=True)
    return builder.as_markup(input_field_placeholder='Выберите ответ из предложенных', resize_keyboard=True)


def get_result(polled_results):
    animals = {
        'dog': {
            'keys': {'appearance': 'Нейтральный, Темный', 'pref_food': 'Мясо, Морепродукты',
                     'activities': 'Активный',
                     'personality': 'Игривый, Дружелюбный', 'attention': 'Все время, Много времени',
                     'training': 'Да, Возможно',
                     'caring': 'Неприхотливый', 'size': 'Крупного, Среднего', 'environment': 'На суше'},
            'img': 'src/dog.webp',
            'score': 0,
            'text': 'Собака'},

        'cat': {
            'keys': {'appearance': 'Нейтральный, Темный', 'pref_food': 'Мясо, Морепродукты',
                     'activities': 'По настроению, Ленивый',
                     'personality': 'Игривый, Нелюдимый', 'attention': 'Немного времени, Мало времени',
                     'training': 'Нет',
                     'caring': 'Неприхотливый, Минимум требований', 'size': 'Среднего', 'environment': 'На суше'},
            'img': 'src/cat.webp',
            'score': 0,
            'text': 'Кот'},

        'wolf': {
            'keys': {'appearance': 'Нейтральный', 'pref_food': 'Мясо, Морепродукты',
                     'activities': 'Активный',
                     'personality': 'Нелюдимый, Игривый, Дружелюбный', 'attention': 'Все время, Много времени',
                     'training': 'Да, Возможно',
                     'caring': 'Неприхотливый', 'size': 'Крупного', 'environment': 'На суше'},
            'img': 'src/wolf.webp',
            'score': 0,
            'text': 'Волк'},

        'raven': {
            'keys': {'appearance': 'Темный', 'pref_food': 'Орехи, Мясо, Фрукты', 'activities': 'Активный',
                     'personality': 'Игривый', 'attention': 'Много времени', 'training': 'Да, Возможно',
                     'caring': 'Требовательный', 'size': 'Среднего, Совсем небольшого', 'environment': 'В воздухе'},
            'img': 'src/raven.webp',
            'score': 0,
            'text': 'Ворон'},

        'ferret': {
            'keys': {'appearance': 'Яркий, Нейтральный', 'pref_food': 'Мясо, Морепродукты', 'activities': 'Активный',
                     'personality': 'Игривый', 'attention': 'Все время, Много времени', 'training': 'Возможно',
                     'caring': 'Минимум требований', 'size': 'Совсем небольшого', 'environment': 'На суше'},
            'img': 'src/ferret.webp',
            'score': 0,
            'text': 'Хорёк'},

        'guppy': {
            'keys': {'appearance': 'Яркий', 'pref_food': '', 'activities': '',
                     'personality': 'Нелюдимый', 'attention': 'Немного времени',
                     'training': 'Нет',
                     'caring': 'Неприхотливый', 'size': 'Совсем небольшого', 'environment': 'В воде'},
            'img': 'src/guppy.webp',
            'score': 0,
            'text': 'Рыбка Гуппи'},

        'discus': {
            'keys': {'appearance': 'Яркий', 'pref_food': 'Морепродукты', 'activities': '',
                     'personality': '', 'attention': 'Немного времени', 'training': 'Нет',
                     'caring': 'Минимум требований', 'size': 'Среднего', 'environment': 'В воде'},
            'img': 'src/discus.webp',
            'score': 0,
            'text': 'Дискус'},

        'parrot': {
            'keys': {'appearance': 'Яркий', 'pref_food': 'Орехи, Фрукты', 'activities': 'Активный',
                     'personality': 'Игривый', 'attention': 'Много времени', 'training': 'Возможно',
                     'caring': 'Требовательный', 'size': 'Среднего', 'environment': 'В воздухе'},
            'img': 'src/parrot.webp',
            'score': 0,
            'text': 'Попугай'},

        'hamster': {
            'keys': {'appearance': 'Нейтральный', 'pref_food': 'Орехи, Фрукты', 'activities': 'По настроению',
                     'personality': 'Дружелюбный', 'attention': 'Немного времени', 'training': 'Нет',
                     'caring': 'Неприхотливый', 'size': 'Совсем небольшого', 'environment': 'На суше'},
            'img': 'src/hamster.webp',
            'score': 0,
            'text': 'Хомячок'},

        'turtle': {
            'keys': {'appearance': 'Нейтральный, Яркий', 'pref_food': 'Морепродукты, Мясо', 'activities': 'Ленивый',
                     'personality': 'Нелюдимый', 'attention': 'Немного времени', 'training': 'Нет',
                     'caring': 'Требовательный', 'size': 'Совсем небольшого', 'environment': 'В воде'},
            'img': 'src/turtle.webp',
            'score': 0,
            'text': 'Водная черепашка'},

        'tortoise': {
            'keys': {'appearance': 'Нейтральный, Яркий', 'pref_food': 'Овощи, Фрукты', 'activities': 'Ленивый',
                     'personality': 'Нелюдимый', 'attention': 'Немного времени', 'training': 'Нет',
                     'caring': 'Минимум требований', 'size': 'Совсем небольшого', 'environment': 'На суше'},
            'img': 'src/tortoise.webp',
            'score': 0,
            'text': 'Черепаха'},

        'snake': {
            'keys': {'appearance': 'Яркий, Нейтральный', 'pref_food': 'Мясо', 'activities': 'Ленивый',
                     'personality': 'Нелюдимый', 'attention': 'Немного времени', 'training': 'Нет',
                     'caring': 'Минимум требований', 'size': 'Среднего, Совсем небольшого', 'environment': 'На суше'},
            'img': 'src/snake.webp',
            'score': 0,
            'text': 'Змея'},

        'moth': {
            'keys': {'appearance': 'Яркий', 'pref_food': '', 'activities': 'По настроению',
                     'personality': 'Дружелюбный', 'attention': 'Мало времени', 'training': 'Нет',
                     'caring': 'Минимум требований', 'size': 'Совсем небольшого', 'environment': 'В воздухе'},
            'img': 'src/moth.webp',
            'score': 0,
            'text': 'Мотылек'}
    }

    for answer in polled_results:
        for animal in animals:
            if polled_results[answer] in animals[animal]['keys'][answer]:
                animals[animal]['score'] += 1

    lst = list(animals.keys())
    sorted_lst = list(sorted(lst, key=lambda x: animals[x]['score'], reverse=True))
    return animals[sorted_lst[0]]['text'], animals[sorted_lst[0]]['img']


def get_res_msg(animal):
    result_msg = f'''
Поздравляем, тест пройден!
Ваше тотемное животное - {animal}.

В нашем зоопарке вы можете оформить опеку над животными, подробности на нашем сайте по ссылке ниже
'''
    return result_msg
