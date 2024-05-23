import subprocess
import os

def compile_and_upload_arduino(file_path):
    # Compile the .ino file into a .hex file
    compile_command = [
        'arduino-cli',
        'compile',
        '--fqbn', 'arduino:avr:uno',  # Adjust according to your Arduino model
        file_path
    ]
    subprocess.run(compile_command, check=True)

    # The .hex file will be in the same directory as the .ino file
    hex_file_path = os.path.splitext(file_path)[0] + '.hex'

    # Upload the .hex file to the Arduino
    upload_command = [
        'avrdude',
        '-p', 'atmega328p',  # Adjust according to your Arduino model
        '-c', 'arduino',
        '-P', '/dev/ttyACM0',  # Adjust according to your setup
        '-b', '115200',  # Adjust according to your Arduino model
        '-U', f'flash:w:{hex_file_path}:i'
    ]
    subprocess.run(upload_command, check=True)

# Call the function with the path to your .ino file
compile_and_upload_arduino('JARVIS.ino')