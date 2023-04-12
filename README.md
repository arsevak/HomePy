# HomePy
A prototype of a smart home system written in python that demonstrates smart monitoring over residences such as controlling house temperature, answering doors and safeguarding important places/things using Raspberry Pi and Arduino board + sensors.

## Requirements

This prototype is run on a terminal/command prompt, and utilizes Raspberry Pi and the following components of the Arduino Board:

1. Button
2. Buzzer
3. Servo motor
4. Blue Light
5. I2C - LCD
6. Temperature Sensor
7. Touch Sensor

## How it works

This prototype uses threads to actively receive multiple inputs from the sensors and provides the following ways of monitoring a house:

### Answer doors

The program considers Button as a door bell, and once pressed, the program will make a sound through the Buzzer (emulating a door bell) and register a notification. To see all notifications, select "Show notifications" from the main menu shown in the terminal, and you will see the registered notification called "Answer the door".

Upon selection, the program will make the servo motor, which is a placeholder for a door, to rotate its motor 180 degrees, emulating the opening of a door.

### House Temperature Control

The program uses temperature sensor to receive temperature input from the environment. I2C - LCD and Blue light components are used to emulate ON and OFF states of Heaters respectively.

The main menu on the terminal asks user to enter the desired temperature in Celsius. 

Once set, this input is used by the program to maintain the temperature of the house. When the temperature of the room falls down from the desired temperature, the program turns the LCD to blue color emulating OFF state of the heater. When the temperature of the room rises above the desired temperature, the program turns the LCD to red color emulating ON state of the heater. When the temperature is equal to the desired one, the LCD is turned off.

### Proximity sensor

In this example, touch sensor is used instead of proximity sensor (IR sensor) due to its unavailability. The touch sensor is used in this example to emulate an important object that the user wants to safeguard from others. IR sensor is the best component to be used in this case to maintain a safe distance between an area/object and others. When touch sensor is pressed, a notification is registered and the user can read the notifications on the terminal as "Proximity Danger".

## Recommendations

This program is just a prototype, hence it can be used in various ways to inspire an actual smart home system.

For example, the main menu shown in the terminal by this program can be shown directly to the user's smartphone app using cloud servers. This way, the house stays protected with minimum data usage.

As mentioned earlier, IR sensor is an excellent way to keep people away from some spaces/things. For example, it can also be used to keep toddlers away from going to some dangerous places in house OR it can also be used to safeguard a safety box from theft.
