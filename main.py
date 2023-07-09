import vlc

url = 'http://radio.mvd.ru:8000/mv128.mp3'

instance = vlc.Instance('--fullscreen')
player = instance.media_player_new()
media = instance.media_new(url)
player.set_media(media)
player.play()

while True:
    pass