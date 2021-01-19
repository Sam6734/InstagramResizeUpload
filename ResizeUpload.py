from PIL import Image, ImageOps
import os,time, glob
from instabot import Bot

# put your filepath here
filepath = r"C:\instagramupload\pythonupload.jpg"
#image caption
caption = 'Math majors need to understand'
#image hashtags
hashtags = '#Python #programming #programmerhumor #memes'
#your instagram username
instausername = 'instausername'
#your instagram password
instapassword = 'instapassword'

def resizeimg(func):
    def wrapper():
        originalimg = Image.open((filepath))
        size = (1080, 1350)
        fit_and_resized_image = ImageOps.fit(originalimg, size, Image.ANTIALIAS)
        fit_and_resized_image.save(os.path.join(os.path.split(filepath)[0], 'instagramimage.jpg'))
        func()
        for f in glob.glob(os.path.join(os.path.split(filepath)[0], "instagramimage*.*")):
            os.remove(f)
    return wrapper

@resizeimg
def upload():
    bot = Bot()
    bot.login(username=instausername, password=instapassword)
    bot.upload_photo(os.path.join(os.path.split(filepath)[0], 'instagramimage.jpg'), caption=caption + '\r\n' + hashtags )

upload()








