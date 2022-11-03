radio.setGroup(1)
basic.showIcon(IconNames.Heart)
radio.setTransmitPower(7)
basic.forever(function () {
    if (GHBit.Rocker(GHBit.enRocker.Up)) {
        radio.sendNumber(1)
    } else if (GHBit.Rocker(GHBit.enRocker.Down)) {
        radio.sendNumber(2)
    } else if (GHBit.Rocker(GHBit.enRocker.Left)) {
        radio.sendNumber(3)
    } else if (GHBit.Rocker(GHBit.enRocker.Right)) {
        radio.sendNumber(4)
    } else if (GHBit.Rocker(GHBit.enRocker.Press)) {
        radio.sendNumber(5)
    } else if (input.buttonIsPressed(Button.A)) {
        radio.sendNumber(10)
    } else {
        radio.sendNumber(0)
    }
})
