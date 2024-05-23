import os
import subprocess
import sys

# Define paths and filenames
ino_file = "/home/jarvis/JARVIS/JARVIS.ino"  # Corrected path to the .ino file
arduino_cli = "/home/jarvis/bin/arduino-cli"  # Correct path to arduino-cli
fqbn = "arduino:avr:uno"
port = "/dev/ttyS0"  # Adjust according to your setup, typically /dev/ttyUSB0 or /dev/ttyACM0

def compile_sketch(ino_file):
    # Assuming the compiled hex file is in the same directory as the .ino file
    compiled_hex = os.path.splitext(ino_file)[0] + '.ino.hex'
    compile_command = [
        arduino_cli, "compile", "--fqbn", fqbn, "--output-dir", os.path.dirname(ino_file), ino_file
    ]
    result = subprocess.run(compile_command, capture_output=True, text=True)
    if result.returncode != 0:
        print("Compilation failed:")
        print(result.stderr)
        sys.exit(1)
    print("Compilation successful")
    print(result.stdout)  # Print the output of the compilation process
    return os.path.join(os.path.dirname(ino_file), compiled_hex)  # Return the full path to the .hex file

def upload_sketch(port, fqbn, compiled_hex):
    if not all([arduino_cli, port, fqbn, compiled_hex]):
        print("One or more required variables are None")
        sys.exit(1)
    upload_command = [
        arduino_cli, "upload", "-p", port, "--fqbn", fqbn, "--input-file", compiled_hex  # Use --input-file option
    ]
    result = subprocess.run(upload_command, capture_output=True, text=True)
    if result.returncode != 0:
        print("Upload failed:")
        print(result.stderr)
        sys.exit(1)
    print("Upload successful")

if __name__ == "__main__":
    compiled_hex = compile_sketch(ino_file)
    upload_sketch(port, fqbn, compiled_hex)