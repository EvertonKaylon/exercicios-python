import pyglet

music = pyglet.resource.media('Teste.mp3', streaming=False)
music.play()

pyglet.app.run()