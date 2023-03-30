from serial import Serial
import time

'''set the serial to connect  to the arduino (you should change the port)'''
ser = Serial(
    port='COM7',
    baudrate=115200,
    timeout=None)


def add_data(data):
    """a function  to add the data to the text file"""
    date = time.time()
    date_header = str(data) + ',' + str(date) + '\n'
    print(data)
    file_data = open('example.txt', 'a')
    file_data.write(date_header)
    file_data.close()


while True:
    ''' infinite loop'''
    rotation = float(ser.readline().decode('utf-8'))
    '''read and decode the data'''
    add_data(rotation)
    '''add the data to the  txt file'''
    if rotation > 60:
        print("led is on")
    else:
        print("led is off")
