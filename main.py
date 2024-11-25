import flet as ft
from pytubefix import YouTube
from pytubefix.cli import on_progress

def download_mp3(page, url):
   yt=YouTube(url)
   x=yt.streams.filter(only_audio=True)
   name=yt.title
#yt.streams.filter(only_audio=True)


#yt.download()
#yt = YouTube('http://youtube.com/watch?v=9bZkp7q19f0')
#yt.streams.filter(only_audio=True)
   streams = yt.streams.get_by_itag(139)
   streams.download(filename=name+".mp3")

def main(page: ft.Page):
    page.bgcolor = ft.colors.WHITE

    # حقل النص لإدخال رابط الفيديو
    text_field = ft.TextField(
        label="أدخل رابط YouTube هنا", 
        border_color=ft.colors.BLACK,
        color=ft.colors.BLACK,
        label_style=ft.TextStyle(color=ft.colors.BLACK)
    )

    # زر التنزيل
    button = ft.ElevatedButton(
        "تحميل الصوت بصيغة MP3",
        on_click=lambda e: download_mp3(page, text_field.value),
        bgcolor=ft.colors.RED,
        color=ft.colors.WHITE
    )

    

    # إضافة المكونات إلى الصفحة
    page.add(
        ft.Column(
            controls=[text_field, button],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )

ft.app(target=main)
