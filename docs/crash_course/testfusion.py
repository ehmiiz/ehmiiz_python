import fusionengine as fusion

window = fusion.window("Example:", 1, 600, 600)
image = fusion.image(window, fusion.DEBUGIMAGE, 0, 0, 600, 600)

@window.loop
def loop():
    image.draw()