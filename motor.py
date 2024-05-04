import network
import socket
from machine import Pin
import time

motor_left_forward = Pin(16, Pin.OUT)
motor_left_backward = Pin(17, Pin.OUT)
motor_right_forward = Pin(18, Pin.OUT)
motor_right_backward = Pin(19, Pin.OUT)
ultrasonic_trigger = Pin(22, Pin.OUT)
ultrasonic_echo = Pin(21, Pin.IN)

# Connect to WiFi
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect("Your_WiFi_Name", "Your_WiFi_Password")

# Wait for WiFi connection
timeout = 10
while timeout > 0:
    if wifi.isconnected():
        break
    timeout -= 1
    print('Waiting for WiFi connection...')
    time.sleep(1)

if not wifi.isconnected():
    raise RuntimeError('WiFi connection failed')
else:
    print('WiFi Connected')
    local_ip = wifi.ifconfig()[0]
    print('Local IP:', local_ip)

local_port = 1234     #UDP_port
buffer_size = 1024

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.bind((local_ip, local_port))
print('Listening on Port - ' + str(local_port))

while True:
    data, addr = udp_socket.recvfrom(buffer_size)
    message = str(data.decode()).strip()
    print("Incoming Data:", message, ", From Address:", addr)

    ultrasonic_trigger.low()
    time.sleep_us(2)
    ultrasonic_trigger.high()
    time.sleep_us(5)
    ultrasonic_trigger.low()

    while ultrasonic_echo.value() == 0:
        signal_off = time.ticks_us()
    while ultrasonic_echo.value() == 1:
        signal_on = time.ticks_us()
    time_passed = signal_on - signal_off
    distance = (time_passed * 0.0343) / 2
    print("Total distance:", distance, "cm")
    print("Sensor")
    time.sleep(1)

    if distance < 40:
        motor_left_forward.high()
        motor_left_backward.low()
        motor_right_forward.high()
        motor_right_backward.low()

    if message == "front":
        motor_left_forward.high()
        motor_left_backward.low()
        motor_right_forward.high()
        motor_right_backward.low()

    if message == "back":
        motor_left_forward.low()
        motor_left_backward.high()
        motor_right_forward.low()
        motor_right_backward.high()

    if message == "left":
        motor_left_forward.high()
        motor_left_backward.low()
        motor_right_forward.low()
        motor_right_backward.low()

    if message == "right":
        motor_left_forward.low()
        motor_left_backward.low()
        motor_right_forward.high()
        motor_right_backward.low()



 