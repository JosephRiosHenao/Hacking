from instabot import Bot;

bot = Bot();
bot.login(username = input("Digite su username: "), password = input("Digite su contraseña: "))
bot.upload_photo("CloudIcon.png", caption="Prueba de upload desde bot")
