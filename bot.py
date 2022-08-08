from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher



from config import TOKEN
import keyboards as nav
import ssh_module
import list_arrays as arl
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
#Режим работы бота
###@myidbot    /getgroupid@myidbot
sent_tlg = "INSERT YOUR VALUE HERE"


## message.from_user.id
## chat_id=
#pwdown = "!Пароль находится в двойных кавычках!\nПароль ВиФи содержит одна из строк ниже"
pwdown = "Пароль ВиФи содержит одна из строк ниже"
pwup = "Пароль ВиФи содержит одна из строк выше"
##



bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.callback_query_handler(text="mainmenu")
async def request_tt_1(message: types.message):
    await bot.send_message(sent_tlg, text="Выберите один из роутеров", reply_markup=nav.mainMenu)



####
@dp.callback_query_handler(text=arl.opc_arr_1[1])
async def request_tt_1(message: types.message):
    host = arl.opc_arr_1[2]
    await bot.send_message(sent_tlg, reply_markup=nav.mainMenu, text="Подключение к  "+arl.opc_arr_1[0] + "\n" + pwdown + "\n" + ssh_module.mikrotik_request(host) + pwup)
@dp.callback_query_handler(text=arl.opc_arr_2[1])
async def request_tt_1(message: types.message):
    host = arl.opc_arr_2[2]
    await bot.send_message(sent_tlg, reply_markup=nav.mainMenu, text="Подключение к  "+arl.opc_arr_2[0] + "\n" + pwdown + "\n" + ssh_module.mikrotik_request(host) + pwup)
@dp.callback_query_handler(text=arl.opc_arr_3[1])
async def request_tt_1(message: types.message):
    host = arl.opc_arr_3[2]
    await bot.send_message(sent_tlg, reply_markup=nav.mainMenu, text="Подключение к  "+arl.opc_arr_3[0] + "\n" + pwdown + "\n" + ssh_module.mikrotik_request(host) + pwup)
@dp.callback_query_handler(text=arl.opc_arr_4[1])
async def request_tt_1(message: types.message):
    host = arl.opc_arr_4[2]
    await bot.send_message(sent_tlg, reply_markup=nav.mainMenu, text="Подключение к  "+arl.opc_arr_4[0] + "\n" + pwdown + "\n" + ssh_module.mikrotik_request(host) + pwup)

####



@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    #await message.reply("Привет!\nНапиши мне что-нибудь!")
    await bot.send_message(sent_tlg, text="Данный бот подскажет пароль от ВиФи\nНужно ткнуть на кнопку и ждать результат", reply_markup=nav.mainMenu)


@dp.message_handler(commands=['wifi'])
async def process_start_command(message: types.Message):
    #await message.reply("Привет!\nНапиши мне что-нибудь!")
    await bot.send_message(sent_tlg, text="Данный бот подскажет пароль от ВиФи\nНужно ткнуть на кнопку и ждать результат", reply_markup=nav.mainMenu)


# бот будет постоянно спрашивать у сервера Телеграмма «Мне кто-нибудь написал?»,
# bot.polling(none_stop=True, interval=1)
if __name__ == '__main__':
    executor.start_polling(dp)
