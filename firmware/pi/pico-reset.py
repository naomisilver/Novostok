from gpiozero import LED
from time import sleep

sleep(10)

reset = LED(22)

reset.off()
sleep(0.2)
reset.on()