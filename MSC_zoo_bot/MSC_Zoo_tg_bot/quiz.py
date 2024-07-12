from aiogram import Bot, Dispatcher, types, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
import asyncio
import logging
from aiogram.types import ReplyKeyboardRemove, FSInputFile
import quiz_backend
import texts

router = Router()


class Quiz(StatesGroup):
    first = State()
    second = State()
    third = State()
    fourth = State()
    fifth = State()
    sixth = State()
    seventh = State()
    eight = State()
    ninth = State()
    finish = State()


@router.message(Command(commands=['start', 'help']))
async def start_func(message: types.Message):
    await message.answer_photo(photo=FSInputFile('src/logo.webp'))
    await message.answer(
        text='''
Вас приветствует бот Московского зоопарка!

/start - Запустить бота
/quiz - Викторина "Какое у вас тотемное животное"
/about - О нас
/contacts - Контактная информация
''')


@router.message(Command(commands=['about']))
async def quiz_func(message: types.Message):
    await message.answer_photo(photo=FSInputFile('src/entry.jpg'))
    await message.answer(
        text=texts.about, reply_markup=quiz_backend.about_inline_kb)


@router.message(Command(commands=['contacts']))
async def quiz_func(message: types.Message):
    await message.answer(text=texts.contacts)


@router.message(Command(commands=['quiz']))
async def quiz_func(message: types.Message, state: FSMContext):
    await message.answer(text=texts.quiz, reply_markup=quiz_backend.start_btn)
    await state.set_state(Quiz.first)


@router.message(Quiz.first)  # show first question
async def qiz_start_func(message: types.Message, state: FSMContext):
    await message.answer_photo(photo=FSInputFile('src/appearance.webp'))
    await message.answer(
        text=quiz_backend.questions['appearance'],
        reply_markup=quiz_backend.get_answers('appearance', back_btn=False))
    await state.set_state(Quiz.second)


@router.message(Quiz.second)  # after reply second question is shown
async def qiz_start_func(message: types.Message, state: FSMContext):
    await message.answer_photo(photo=FSInputFile('src/food.webp'))
    await message.answer(
        text=quiz_backend.questions['pref_food'],
        reply_markup=quiz_backend.get_answers('pref_food'))
    await state.update_data(appearance=message.text)
    await state.set_state(Quiz.third)


@router.message(Quiz.third)
async def qiz_start_func(message: types.Message, state: FSMContext):
    if message.text == 'Вернуться назад':  # if it is a reply to previous (2) question
        await message.answer_photo(photo=FSInputFile('src/appearance.webp'))
        await message.answer(
            text=quiz_backend.questions['appearance'],
            reply_markup=quiz_backend.get_answers('appearance', back_btn=False))  # show first(n-2) question
        await state.set_state(Quiz.second)  # and set previous(n-1) state
    else:
        await message.answer_photo(photo=FSInputFile('src/activities.webp'))
        await message.answer(
            text=quiz_backend.questions['activities'],
            reply_markup=quiz_backend.get_answers('activities'))  # else go to the next question
        await state.update_data(pref_food=message.text)
        await state.set_state(Quiz.fourth)  # next state(n+1)


@router.message(Quiz.fourth)
async def qiz_start_func(message: types.Message, state: FSMContext):
    if message.text == 'Вернуться назад':
        await message.answer_photo(photo=FSInputFile('src/food.webp'))
        await message.answer(
            text=quiz_backend.questions['pref_food'], reply_markup=quiz_backend.get_answers('pref_food'))
        await state.set_state(Quiz.third)
    else:
        await message.answer_photo(photo=FSInputFile('src/personality.webp'))
        await message.answer(
            text=quiz_backend.questions['personality'],
            reply_markup=quiz_backend.get_answers('personality'))
        await state.update_data(activities=message.text)
        await state.set_state(Quiz.fifth)


@router.message(Quiz.fifth)
async def qiz_start_func(message: types.Message, state: FSMContext):
    if message.text == 'Вернуться назад':
        await message.answer_photo(photo=FSInputFile('src/activities.webp'))
        await state.set_state(Quiz.fourth)
        await message.answer(
            text=quiz_backend.questions['activities'], reply_markup=quiz_backend.get_answers('activities'))
    else:
        await message.answer(
            text=quiz_backend.questions['attention'], reply_markup=quiz_backend.get_answers('attention'))
        await state.update_data(personality=message.text)
        await state.set_state(Quiz.sixth)


@router.message(Quiz.sixth)
async def qiz_start_func(message: types.Message, state: FSMContext):
    if message.text == 'Вернуться назад':
        await state.set_state(Quiz.fifth)
        await message.answer_photo(photo=FSInputFile('src/personality.webp'))
        await message.answer(
            text=quiz_backend.questions['personality'], reply_markup=quiz_backend.get_answers('personality'))
    else:
        await message.answer_photo(photo=FSInputFile('src/training.webp'))
        await message.answer(
            text=quiz_backend.questions['training'], reply_markup=quiz_backend.get_answers('training'))
        await state.update_data(attention=message.text)
        await state.set_state(Quiz.seventh)


@router.message(Quiz.seventh)
async def qiz_start_func(message: types.Message, state: FSMContext):
    if message.text == 'Вернуться назад':
        await state.set_state(Quiz.sixth)
        await message.answer(
            text=quiz_backend.questions['attention'], reply_markup=quiz_backend.get_answers('attention'))
    else:
        await message.answer_photo(photo=FSInputFile('src/caring.webp'))
        await message.answer(
            text=quiz_backend.questions['caring'], reply_markup=quiz_backend.get_answers('caring'))
        await state.update_data(training=message.text)
        await state.set_state(Quiz.eight)


@router.message(Quiz.eight)
async def qiz_start_func(message: types.Message, state: FSMContext):
    if message.text == 'Вернуться назад':
        await message.answer_photo(photo=FSInputFile('src/training.webp'))
        await state.set_state(Quiz.seventh)
        await message.answer(
            text=quiz_backend.questions['training'], reply_markup=quiz_backend.get_answers('training'))
    else:
        await message.answer_photo(photo=FSInputFile('src/size.webp'))
        await message.answer(
            text=quiz_backend.questions['size'], reply_markup=quiz_backend.get_answers('size'))
        await state.update_data(caring=message.text)
        await state.set_state(Quiz.ninth)


@router.message(Quiz.ninth)
async def qiz_start_func(message: types.Message, state: FSMContext):
    if message.text == 'Вернуться назад':
        await message.answer_photo(photo=FSInputFile('src/caring.webp'))
        await state.set_state(Quiz.eight)
        await message.answer(
            text=quiz_backend.questions['caring'], reply_markup=quiz_backend.get_answers('caring'))
    else:
        await message.answer_photo(photo=FSInputFile('src/environment.webp'))
        await message.answer(
            text=quiz_backend.questions['environment'], reply_markup=quiz_backend.get_answers('environment'))
        await state.update_data(size=message.text)
        await state.set_state(Quiz.finish)


@router.message(Quiz.finish)
async def qiz_start_func(message: types.Message, state: FSMContext):
    if message.text == 'Вернуться назад':
        await message.answer_photo(photo=FSInputFile('src/size.webp'))
        await state.set_state(Quiz.ninth)
        await message.answer(text=quiz_backend.questions['size'], reply_markup=quiz_backend.get_answers('size'))
    else:
        await state.update_data(environment=message.text)
        answers = dict(*(await asyncio.gather(state.get_data())))
        text, pic = quiz_backend.get_result(answers)
        text = quiz_backend.get_res_msg(text)
        await message.answer_photo(photo=FSInputFile(pic))
        await message.answer(text=text, reply_markup=quiz_backend.result_inline_kb)
        await state.clear()


@router.callback_query()
async def quiz_again(callback: types.CallbackQuery, state: FSMContext):
    text = callback.data
    if text == 'restart':
        await callback.message.answer_photo(photo=FSInputFile('src/appearance.webp'))
        await callback.message.answer(
            text=quiz_backend.questions['appearance'],
            reply_markup=quiz_backend.get_answers('appearance', back_btn=False))
        await state.set_state(Quiz.second)


async def main():
    logging.basicConfig(level=logging.DEBUG)
    TOKEN = texts.token

    # session = AiohttpSession(proxy='http://proxy.server:3128')
    # bot = Bot(token=TOKEN, session=session)

    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
