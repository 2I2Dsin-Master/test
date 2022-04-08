def on_button_pressed_a():
    led.plot(0, 0)
    led.unplot(1, 1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    led.plot(1, 1)
    led.unplot(0, 0)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_forever():
    pass
basic.forever(on_forever)
