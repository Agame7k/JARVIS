import os
import subprocess
import sys

# Define paths and filenames
ino_file = "/home/jarvis/JARVIS/JARVIS.ino"  # Corrected path to the .ino file
arduino_cli = "/home/jarvis/bin/arduino-cli"  # Correct path to arduino-cli
fqbn = "arduino:avr:uno"
port = "/dev/ttyUSB0"  # Adjust according to your setup, typically /dev/ttyUSB0 or /dev/ttyACM0

def compile_sketch(ino_file):
    compile_command = [
        arduino_cli, "compile", "--fqbn", fqbn, ino_file
    ]
    result = subprocess.run(compile_command, capture_output=True, text=True)
    if result.returncode != 0:
        print("Compilation failed:")
        print(result.stderr)
        sys.exit(1)
    print("Compilation successful")
    print(result.stdout)  # Print the output of the compilation process

def upload_sketch(ino_file):
    # Get the directory of the .ino file
    ino_dir = os.path.dirname(ino_file)
    # Find the .hex file in the build directory
    hex_file = os.path.join(ino_dir, "build", fqbn.replace(":", "/"), os.path.splitext(os.path.basename(ino_file))[0] + ".ino.hex")

    print(f"Expected hex file location: {hex_file}")  # Print the expected hex file location

    if not os.path.exists(hex_file):
        print(f"Hex file not found: {hex_file}")
        sys.exit(1)

    upload_command = [
        "avrdude", "-v", "-patmega328p", "-carduino", f"-P{port}", "-b115200", "-D", f"-Uflash:w:{hex_file}:i"
    ]
    result = subprocess.run(upload_command, capture_output=True, text=True)
    if result.returncode != 0:
        print("Upload failed:")
        print(result.stderr)
        sys.exit(1)
    print("Upload successful")

if __name__ == "__main__":
    compile_sketch(ino_file)
    upload_sketch(ino_file)
