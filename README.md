# WIFI-Controlled-Robocar
This project focuses on creating an intelligent two-wheel robotic system that can be controlled remotely and utilizes ultrasonic sensors for navigation and obstacle detection.

## Features

- **Remote Control:** Control the UltrabotX wirelessly using Blynk app.
- **Ultrasonic Sensing:** Utilize ultrasonic sensors to measure distances and navigate around obstacles/stops if the distance is less than 40cm and reverses.
- **Motor Control:** Drive the robot with precise motor control for forward, backward, left, and right movements.
- **Real-time Feedback:** Receive real-time distance feedback from the ultrasonic sensors for effective navigation.

## Requirements

- Raspberry Pi Pico 
- Two-wheeled robotic chassis with motor driver
- Ultrasonic sensors (HC-SR04 or similar)
- WiFi connectivity for remote control
- Thonny IDE

## Summary

- The robot car is built with an ultrasonic sensor to measure distance. If there is an obstacle, it stops and goes in reverse. An IR sensor is used to automatically turn off indicator lights and a buzzer when turning. The buzzer is activated when reversing.
- All of these features are integrated into the Raspberry Pi Pico. 
- These data are controlled and monitored through Blynk IOT cloud platform.
