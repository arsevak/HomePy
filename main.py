#D2 - button, D3 - Servo, D4 - Blue Light, D8 - Buzzer, D6 - Touch, I2C - LCD, A0 - Temp Sensor

from homepy.arduino import *
import threading
from time import sleep

notif = []
actionInput = 0
desTempGlobal = 0
lockThreads = threading.Lock()

def doorBell():
    while True:
        
        if digital_read(2) == True:
            buzzer_note(8,20,500)
            if "Answer the door" not in notif:
                with lockThreads:
                    notif.append("Answer the door")
                        
    return


def tempControl():
    
    while True:
        if temp_celsius(0) > (desTempGlobal + 0.5):
            lcd_clear()
            lcd_rgb(0,150,0)
            lcd_print(round(temp_celsius(0),2))
            digital_write(4,1) #Blue Light ON
            
        elif temp_celsius(0) < (desTempGlobal - 0.5):
            lcd_rgb(255,0,0) #Red LCD Background
            lcd_clear()
            lcd_print("Heaters ON-"+str(round(temp_celsius(0),2)))
            digital_write(4,0) #Blue Light OFF
        else:
            
            digital_write(4,0) #Blue Light OFF
            lcd_clear()
            lcd_rgb(0,150,0)
            lcd_print(round(temp_celsius(0),2))
            
        sleep(0.5)
    return



def IRsensor():
    
    while True:
        if digital_read(6) == True: #Touch Sensor for now
            buzzer_note(8,20,30000)
            if "Proximity Danger" not in notif:
                with lockThreads:
                    notif.append("Proximity Danger")
        
    return




def mainMenu():
    
    
    print("\n\n\nWelcome to the Smart Home Control Window")
    print("-----Main Menu-----")
    print("1. Change the Desired Temperature\n2. Show notifications")
    
    return




def setDesTemp():
    
    global desTempGlobal  #Declaring global as to change the value of this globally declared variable
    desTempGlobal = float(input("Enter your Desired Temperature in Celsius - "))
    print("\nSettings applied!\nYou will be redirected to the Main Menu in 3 seconds....")
    sleep(3)
    return
    


#Creating Processes
doorFunc = threading.Thread(target=doorBell)
IRFunc = threading.Thread(target=IRsensor)
desTempGlobal = float(input("\nEnter your Desired Temperature in Celsius - "))
tempFunc = threading.Thread(target=tempControl)


#Starting Processes
doorFunc.start()
IRFunc.start()


tempFunc.start()



#HomeScreen
while True:
    
    mainMenu()
    actionInput = input("\nChoose from the above options - ")

    if actionInput == '':
        continue

    actionInput = int(actionInput)
    
    if actionInput == 1:
        setDesTemp()

    elif actionInput == 2:
        if len(notif) == 0:
            print("\n\n0 notifications\nYou will be redirected to the Main Menu")
            
        else:
            for num,item in enumerate(notif,1):
                print(num,item)

            notifInput = input("\nChoose from the above notifications to respond or press 3 to remove all- ")

            if notifInput == '':
                continue

            notifInput = int(notifInput)

            if 1 <= notifInput <= 2:
                if notif[notifInput-1] == "Answer the door":
                    servo_move(3,180) #Opens the door
                    with lockthreads:
                        notif.remove("Answer the door")
                    sleep(5)  #Waits for 5 seconds
                    servo_move(3,0) #Closes the door

                elif notif[notifInput-1] == "Proximity Danger":
                    with lockthreads:
                        notif.remove("Proximity Danger")
                    buzzer_stop(8)
                
            elif notifInput == 3: #Clears the notifications list
                with lockthreads:
                    notif.clear()
                buzzer.stop(8)
                
    elif actionInput == 9:    #Program kill value
        print("Program Terminated")
        break

    
        
