input.onButtonPressed(Button.A, function on_button_pressed_a() {
    led.plot(0, 0)
    led.unplot(1, 1)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    led.plot(1, 1)
    led.unplot(0, 0)
})
basic.forever(function on_forever() {
    
})
