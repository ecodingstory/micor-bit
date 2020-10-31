from microbit import *

display.off()

while True:
    if pin6.read_digital():
        pin1.write_digital(1)
    else:
        pin1.write_digital(0)
    if pin7.read_digital():
        pin2.write_digital(1)
    else:
        pin2.write_digital(0)
