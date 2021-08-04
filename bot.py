import types
import keyboard
import config
from libs import*

class find(StatesGroup):
    que1 = State()
    que2 = State()


# bot init
storage = MemoryStorage()
bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot, storage=storage)

# start
@dp.message_handler(commands=['start', 'help'])
async def start(message: types.Message):
    await bot.send_message(message.chat.id, f"Привет, *{message.from_user.first_name},* я бот для поиска фильмов на кинопоиске, чтобы узреть мой функционал пропиши '/'", reply_markup=keyboard.start, parse_mode='Markdown')


# search
@dp.message_handler(content_types=['text'], state=None)
async def search(message:types.Message):
    if message.text == 'Поиск фильмов':
        await message.answer("Введите название фильма")

        # changing state
        await find.que1.set()

    elif message.text == 'Новости':
        await message.answer("Приятного чтения☺️")
        await find.que2.set()

    else:
        await message.answer('Я тебя не понял, пожалуйста используй команды 🙏')


# function that parse site and search cinema
@dp.message_handler(state=find.que1)
async def query(message:types.Message, state: FSMContext):
    answer=message.text
    link = config.url + answer

    # getting response from site
    response = requests.get(link)

    # parsing this page
    soup = BeautifulSoup(response.text, "html.parser")

    # searching by class
    films = soup.find_all("p", class_="name")

    # status that bot is typing
    await bot.send_chat_action(message.chat.id, 'typing')

    # if found 0 films
    if len(films) == 0:
        await message.answer('По вашему запросу ничего не найдено 😢')

    # putting a limit of results
    limit = 0
    for film in films:
        limit += 1
        film = film.a.get('href')

        # creating a space for a button
        markup = types.InlineKeyboardMarkup()

        # setting name of the button
        l = types.InlineKeyboardButton("Ссылка для просмотра", url='https://www.ggkinopoisk.ru/' + film)

        # adding our created button
        markup.add(l)

        await bot.send_message(message.chat.id, 'https://www.kinopoisk.ru/' + film, reply_markup=markup)
        if limit == 10:
            break
    # finishing state
    await state.finish()

# media button


@dp.message_handler(state=find.que2)
async def news(message: types.Message, state=FSMContext):
    print('Im here!')
    # getting response from site
    link = 'https://www.kinopoisk.ru/media/news/'
    response = requests.get(link)
    p
    # parsing this page
    soup = BeautifulSoup(response.text, "html.parser")

    # searching by class
    n = soup.find_all("div", class_="post-feature-card__inner")
    n = n.a.get('href')
    print(n)
    await message.answer(config.main + n)
    await state.finish()

if __name__ == "__main__":
    executor.start_polling(dp,skip_updates=True)