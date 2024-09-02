import socket
import pickle
import pyautogui

# Configuration for client
UDP_IP = "0.0.0.0"  # Listen on all network interfaces
UDP_PORT = 5005  # Port to listen on

# Setup UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

def simulate_mouse_event(data):
    event_type = data[0]
    
    if event_type == 'move':
        x, y = data[1], data[2]
        pyautogui.moveTo(x, y)
    elif event_type == 'click':
        x, y, button, pressed = data[1], data[2], data[3], data[4]
        if pressed:
            pyautogui.click(x, y, button=button)

# Main loop to receive data
while True:
    data, addr = sock.recvfrom(1024)  # Buffer size is 1024 bytes
    try:
        event_data = pickle.loads(data)
        simulate_mouse_event(event_data)
    except Exception as e:
        print(f"Error processing data: {e}")
