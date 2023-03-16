import time
from pyfirmata import Arduino, util, STRING_DATA
board = Arduino('COM4')


def msg(text):
    if text:
        board.send_sysex(STRING_DATA, util.str_to_two_byte_iter(text))


m = ""
for s in "Hello!":
    time.sleep(1)
    msg(m)
    m += s

board.send_sysex(STRING_DATA, util.str_to_two_byte_iter('Selam!'))

