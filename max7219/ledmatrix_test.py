from max7219 import LedMatrix8x8
from pyb import Pin, SPI
spi = SPI(1, SPI.MASTER)
load = Pin('X1')
display = LedMatrix8x8(spi,load)

display.clear()
display.show()

teststr = 'HELLO WORLD'
for c in teststr:
	display.print(c)
	display.show()
	pyb.delay(500)
