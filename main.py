def on_button_pressed_a():
    music.play(music.string_playable("F G F E G E F G ", 120),
        music.PlaybackMode.LOOPING_IN_BACKGROUND)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    music.stop_all_sounds()
input.on_button_pressed(Button.B, on_button_pressed_b)


def on_button_pressed_a2():
    pass
input.on_button_pressed(Button.A, on_button_pressed_a2)

