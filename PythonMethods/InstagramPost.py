from instabot import Bot;

bot = Bot();
#bot.login(username = input("Digite su username: "), password = input("Digite su contraseña: "))
#bot.upload_photo(photo="NewCanvas1.jpg", caption="Prueba de upload desde bot")
bot.download_photo(media_id="https://www.instagram.com/p/CFf9DgfH_M1/?utm_source=ig_web_copy_link",filename="Download",folder="IMG")
bot.download_photo(media_id="instagram://media?id=2404909247916667701",filename="Download2",folder="IMG")
