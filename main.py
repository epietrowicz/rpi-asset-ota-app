import serial
import os
import time
import subprocess
import signal

# Get serial settings from environment variables
SERIAL_PORT = "/dev/tty.usbmodem2101"
BAUD_RATE = 115200
SCRIPT_FILENAME = "app.py"

running_process = None  # Track the currently running process

def save_script(data):
    """Save received data as a Python script."""
    with open(SCRIPT_FILENAME, "w") as f:
        f.write(data)

def execute_script():
    """Terminate the existing script and execute the new one."""
    global running_process

    # Terminate existing process if it's running
    if running_process:
        print("Stopping previous script...")
        running_process.send_signal(signal.SIGTERM)  # Graceful shutdown
        running_process.wait()  # Ensure it stops before starting a new one

    print(f"Executing {SCRIPT_FILENAME}...")

    # Start the new script as a subprocess
    running_process = subprocess.Popen(["python3", SCRIPT_FILENAME])

def wait_for_serial():
    """Wait until the serial device becomes available before proceeding."""
    retry_delay = 2  # Initial delay in seconds
    while not os.path.exists(SERIAL_PORT):
        print(f"Waiting for {SERIAL_PORT} to become available...")
        time.sleep(retry_delay)
        retry_delay = min(retry_delay * 2, 60)  # Exponential backoff (max 60s)

def listen_serial():
    """Continuously listen for incoming Python scripts over serial and execute them."""
    print(f"Listening on {SERIAL_PORT} at {BAUD_RATE} baud...")

    retry_delay = 2  # Initial retry delay

    while True:
        try:
            with serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=10) as ser:
                print("Serial connection established.")
                
                retry_delay = 2  # Reset delay on successful connection
                capturing = False
                script_data = []
                
                # Read lines continuously until an exception occurs
                while True:
                    line = ser.readline().decode("utf-8")

                    if "--- Begin app.py" in line:
                        capturing = True
                        script_data = []
                    elif "--- End of file ---" in line:
                        capturing = False
                        script_content = "\n".join(script_data)
                        print("Received script!")
                        save_script(script_content)
                        execute_script()
                    elif capturing:
                        script_data.append(line)
                        
        except (serial.SerialException, FileNotFoundError) as e:
            print(f"Serial error: {e}")
            print(f"Retrying in {retry_delay} seconds...")
            time.sleep(retry_delay)
            retry_delay = min(retry_delay * 2, 60)  # Exponential backoff (max 60s)
            
if __name__ == "__main__":
    listen_serial()
