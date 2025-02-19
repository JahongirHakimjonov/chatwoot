from urllib.parse import urlparse, unquote
import base64

url = "https://panda.felixits.uz/media/hls_videos/cinema/MQ%3D%3D/4e2cfb40-18f3-44c2-a151-628f542af076/master_playlist.m3u8"

# URL ni tahlil qilish
parsed_url = urlparse(url)

# Path ni ajratib olish va kerakli qismini olish
path_parts = parsed_url.path.split("/cinema/")  # "/cinema/" bo'yicha bo'lamiz
if len(path_parts) > 1:
    needed_part = path_parts[1].split("/")[0]  # "/cinema/" dan keyingi birinchi qism
    needed_part = unquote(needed_part)  # URL ni o'qish uchun kodni o'chirib qo'yamiz
    needed_part = base64.b64decode(needed_part).decode("utf-8")  # base64 dan o'qish
    print(needed_part)
else:
    print("Kerakli ma'lumot topilmadi")
