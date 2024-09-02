import socket
import pickle
from pynput import mouse

# Configuration for server
UDP_IP = "192.168.1.2"  # Replace with the actual client IP address
UDP_PORT = 5005         # Port to send data on

# Setup UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Function to send data
def send_data(data):
    # Serialize the data using pickle and send it via UDP
    sock.sendto(pickle.dumps(data), (UDP_IP, UDP_PORT))

# Mouse event listeners
def on_move(x, y):
    # Send the mouse move event
    send_data(('move', x, y))

def on_click(x, y, button, pressed):
    # Send the mouse click event with button information
    send_data(('click', x, y, button.name, pressed))

# Start the mouse listener
with mouse.Listener(on_move=on_move, on_click=on_click) as listener:
    listener.join()
