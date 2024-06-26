import subprocess
import os

def compile_and_upload_arduino(file_path):
    # Compile the .ino file into a .hex file
    compile_command = [
        'arduino-cli',
        'compile',
        '--fqbn', 'arduino:avr:uno',  # Correct for Arduino Uno R3
        file_path
    ]
    subprocess.run(compile_command, check=True)

    # The .hex file will be in the same directory as the .ino file
    hex_file_path = os.path.splitext(file_path)[0] + '.hex'

    # Upload the .hex file to the Arduino
    upload_command = [
        'avrdude',
        '-p', 'atmega328p',  # Correct for Arduino Uno R3
        '-c', 'arduino',
        '-P', '/dev/ttyAMA0',  # Adjust to your setup
        '-b', '115200',  # Correct for Arduino Uno R3
        '-U', f'flash:w:{hex_file_path}:i'
    ]
    subprocess.run(upload_command, check=True)

# Call the function with the path to your .ino file
compile_and_upload_arduino('JARVIS.ino')