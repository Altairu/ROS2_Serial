import serial

data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,]
ser = serial.Serial("/dev/ttyACM0", baudrate=9600)

while True:
    ser.write(bytes(data))  
    received_data = ser.read(16)
    
    for a in range(16):
        data[a] = received_data[a]

    print(data)

