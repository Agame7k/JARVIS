import serial

def send_command(command):
    # Open serial port (adjust device path and baud rate according to your setup)
    ser = serial.Serial('/dev/ttyACM0', 9600)

    # Wait for the serial connection to be established
    ser.flushInput()

    # Send command
    ser.write(command.encode())

    # Close serial port
    ser.close()

# Test the function
send_command('Your command here')