radio.set_group(1)
basic.show_icon(IconNames.HEART)
radio.set_transmit_power(7)

def on_forever():
    if GHBit.rocker(GHBit.enRocker.UP):
        radio.send_number(1)
    elif GHBit.rocker(GHBit.enRocker.DOWN):
        radio.send_number(2)
    elif GHBit.rocker(GHBit.enRocker.LEFT):
        radio.send_number(3)
    elif GHBit.rocker(GHBit.enRocker.RIGHT):
        radio.send_number(4)
    elif GHBit.rocker(GHBit.enRocker.PRESS):
        radio.send_number(5)
    elif input.button_is_pressed(Button.A):
        radio.send_number(10)
    elif GHBit.button(GHBit.enButton.B1, GHBit.enButtonState.PRESS):
        radio.send_number(6)
    elif GHBit.button(GHBit.enButton.B2, GHBit.enButtonState.PRESS):
        radio.send_number(7)
    elif GHBit.button(GHBit.enButton.B3, GHBit.enButtonState.PRESS):
        radio.send_number(8)
    elif GHBit.button(GHBit.enButton.B4, GHBit.enButtonState.PRESS):
        radio.send_number(9)
    else:
        radio.send_number(0)
basic.forever(on_forever)
