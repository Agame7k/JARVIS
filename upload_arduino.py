import subprocess

def upload_arduino(file_path):
    command = [
        'avrdude',
        '-p', 'atmega328p',  # Adjust according to your Arduino model
        '-c', 'arduino',
        '-P', '/dev/ttyACM0',  # Adjust according to your setup
        '-b', '115200',  # Adjust according to your Arduino model
        '-U', f'flash:w:{file_path}:i'
    ]

    subprocess.run(command, check=True)

# Call the function with the path to your .ino file
upload_arduino('JARVIS.ino')