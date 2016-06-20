####################### Import Libraries #################### 
#!/usr/bin/python
# -*- coding: utf-8 -*-
import datetime,time
import RPi.GPIO as GPIO 
import serial
import os
GPIO.setwarnings(False)
#############################################################

####################### Variables Declarations ##############
button1 = 0
button2 = 0
button3 = 0
button4 = 0
button5 = 0
button6 = 0
button7 = 0
button8 = 0
clear_flag = 0
reset_button = 0
OK_button = 0
Buzzer = 0
button1_counter = 0

LCD_Backlight = 5
Flag_LCD_Backlight = 0
#############################################################

####################### LongPress ###########################
GPIO.setmode(GPIO.BCM)
global Number_Count
Number_Count = 0
Longpress_GPIO = 13
GPIO.setup(Longpress_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#global Flag_Main_Menu
Flag_Main_Menu = 0
global Flag_Second 
Flag_Second = 1
global Second_Diff
Second_Diff = 0
global Second_Prev
Second_Prev = 0
global Minute_Prev
Minute_Prev = 0
global Second_Next
Second_Next = 0
global Minute_Next
Minute_Next = 0
global Minute_Change
Minute_Change = 0
global Flag_RESET
Flag_RESET = 0

Total_Minute_Calculation = [60,120,180,240,300,360,420,480,540,600]
#############################################################

###################### OK Button Back Up Flag ###############
#global OK_Button_Data_Backup_Flag
OK_Button_Data_Backup_Flag = 1
#global PUMPING_RIGHT_END_OK_Flag			#For PUMPING RIGHT End and LEFT End Flags
PUMPING_RIGHT_END_OK_Flag = 0
#global PUMPING_LEFT_END_OK_Flag
PUMPING_LEFT_END_OK_Flag = 0
#############################################################

################ MENU DISPLAY Submenu Flags #################
#-------------- Flags for NURSING submenu -----------
NURSING_Submenu_Flag = 0
NURSING_LEFT_Submenu_Flag = 0
NURSING_LEFT_Submenu_Flag = 0
NURSING_RIGHT_Submenu_Flag = 0
NURSING_RIGHT_Submenu_Flag = 0
Back_Nursing_Left_Flag = 0
Back_Nursing_Right_Flag = 0
#-------------- Flags for FEED submenu --------------
FEED_Submenu_Flag = 0
SOLID_Submenu_NEXT_Flag = 0
FORMULA_Submenu_NEXT_Flag = 0
BREAST_MILK_Submenu_NEXT_Flag = 0
BACK_FEED_Option_Flag = 0
BACK_SOLID_Option_Flag_For_Next = 0
BACK_FORMULA_Option_Flag_For_Next = 0
BACK_BREAST_MILK_Option_Flag_For_Next = 0
#--------------- Flages For PUMPING submenu ---------
PUMPING_Submenu_Flag = 0
PUMPING_LEFT_Submenu_Flag = 0
PUMPING_LEFT_START_Submenu_Flag = 0
PUMPING_LEFT_END_Submenu_Flag = 0
PUMPING_RIGHT_Submenu_Flag = 0
PUMPING_RIGHT_START_Submenu_Flag = 0
PUMPING_RIGHT_END_Submenu_Flag = 0
 ##-------------- LEFT ---------------------
Back_Pumping_Left_Flag = 0
Back_Pumping_Left_Start_Flag = 0
Back_Pumping_Left_Start_OZ_Flag = 0
Back_Pumping_Left_End_Flag = 0
Back_Pumping_Left_End_OZ_Flag = 0
 ##--------------RIGHT----------------------
Back_Pumping_Right_Flag = 0
Back_Pumping_Right_Start_Flag = 0
Back_Pumping_Right_Start_OZ_Flag = 0
Back_Pumping_Right_End_Flag = 0
Back_Pumping_Right_End_OZ_Flag = 0
#--------------- Flages For DIAPER submenu ---------
DIAPER_Submenu_Flag = 0
#--------------- Flages For BATH submenu -----------
BATH_Submenu_Flag = 0
#--------------- Flages For SLEEP submenu ----------
SLEEP_Submenu_Flag = 0
#--------------- Flages For MEDICINE submenu -------
MEDICINE_Submenu_Flag = 0
#############################################################

###################### SLEEP MODE Flags #####################
Flag_0to54 = 0
Flag_0to54_Match = 1
Flag_55 = 0
Flag_55_Match = 1
Flag_56 = 0
Flag_56_Match = 1
Flag_57 = 0
Flag_57_Match = 1
Flag_58 = 0
Flag_58_Match = 1
Flag_59 = 0
Flag_59_Match = 1

#global minute_1
minute_1 = 0
#global minute_2
minute_2 = 0
#############################################################

#################### PCF8574 GPIO Exander ###################
#!/usr/bin/env python2.7
from smbus import SMBus
import time

# i2c address of PCF8574
PCF8574=0x38

# open the bus (0 -- original Pi, 1 -- Rev 2 Pi)
bus=SMBus(1)

# make certain the pins are set high so they can be used as inputs
bus.write_byte(PCF8574, 0xff)
#############################################################

########################## GLCD 128x64 ######################
class LCD_GPIO(object):
	global Flag_Second 
	global Flag_Main_Menu
	global reset_button

	GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)

	# GPIO 13 set up as an input, pulled down, connected to 3V3 on button press
	GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(20, GPIO.OUT)
        GPIO.output(20, GPIO.LOW)
	
	GPIO.setup(LCD_Backlight,GPIO.OUT)
        GPIO.output(LCD_Backlight,True)
	
	def reset(channel1):
		global Flag_Second
		global clear_flag
		if(Flag_Second):
#			global Flag_Second
                        Flag_Second = 0

#	                now = datetime.datetime.now()
#        	        global Second_Prev
#                	Second_Prev = int(now.second)
#                	global Minute_Prev
#                	Minute_Prev = int(now.minute)
#                	print ("Second_Prev = "+str(Second_Prev))
#                	print ("Minute_Prev = "+str(Minute_Prev))

#               	now = datetime.datetime.now()
#               	global Second_Next
#               	Second_Next = int(now.second)
#               	global Minute_Next
#               	Minute_Next = int(now.minute)
#		print ("Second_Prev = "+str(Second_Prev))
#               	print ("Second_Next = "+str(Second_Next))
#               	print ("Minute_Next = "+str(Minute_Next))

#                global Minute_Change
#                Minute_Change = Minute_Next - Minute_Prev
		global Flag_RESET
                Flag_RESET = 1
#                if(Minute_Change):
#                	global Second_Diff
#                        Second_Diff = (Second_Next + (Total_Minute_Calculation[Minute_Change-1] - Second_Prev))
#                else:
#                        global Second_Diff
#                        Second_Diff = (Second_Next - Second_Prev)
#                print ("Second Difference = "+str(Second_Diff))
#                if(Second_Diff >= 3):
#                        print ("Long Press > 3 seconds")
#			global Flag_Second
#			Flag_Second = 1
#			global Flag_Main_Menu
#			Flag_Main_Menu = 1
#                elif(Second_Diff < 3):
#                        print ("---------------------------Short Press--------------------")
#			global Flag_Second
#                        Flag_Second = 0

		global Number_Count
		Number_Count+=1
		print " ----- In RESET BUTTON Defination ----- "
                global reset_button
                reset_button = 1
#                global clear_flag
                clear_flag = 1
                clear_for_reset_button()
		
        def OK(channel1):
                print " ----- In OK BUTTON Defination ----- "
                now = datetime.datetime.now()
		date = datetime.datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
                global Second
                Second = int(now.second)
                global Minute
                Minute = int(now.minute)
                global Hour
                Hour = int(now.hour)
                global OK_button
                OK_button = 1
#                global clear_flag
                clear_flag = 1
                clear_for_OK_button()

	
#	print "Make sure you have a button connected so that when pressed"
#	print "it will connect GPIO port 23 (pin 16) to GND (pin 6)\n"
#	print "You will also need a second button connected so that when pressed"
#	print "it will connect GPIO port 24 (pin 18) to 3V3 (pin 1)\n"
#	print "You will also need a third button connected so that when pressed"
#	print "it will connect GPIO port 17 (pin 11) to GND (pin 14)"
	#raw_input("Press Enter when ready\n>")

	# when a falling edge is detected on port 17, regardless of whatever 
	# else is happening in the program, the function my_callback will be run
	#GPIO.add_event_detect(17, GPIO.FALLING, callback=my_callback, bouncetime=300)

#	GPIO.add_event_detect(6, GPIO.FALLING, callback=my_callback, bouncetime=300)
	

	# when a falling edge is detected on port 23, regardless of whatever 
	# else is happening in the program, the function my_callback2 will be run
	#GPIO.add_event_detect(23, GPIO.FALLING, callback=my_callback2, bouncetime=300)

	GPIO.add_event_detect(27, GPIO.FALLING, callback=OK, bouncetime=300)		
	GPIO.add_event_detect(13, GPIO.BOTH, callback=reset, bouncetime=300)
	
#class LCD_GPIO(object):
    # Timing constants
	E_PULSE = 0.000000140  # Addess setup time 140ns
    	E_DELAY = 0.000000200  # Data setup time 200ns

        def __init__(self, RST,RS,RW,E,CS1,CS2, D0, D1, D2, D3, D4, D5, D6, D7):

    	    #GPIO number Assignment
		self.CS1=CS1
        	self.CS2=CS2
	        self.RST=RST
        	self.E = E
	        self.RS = RS
        	self.RW = RW

        	self.D0 = D0
	        self.D1 = D1
	        self.D2 = D2
        	self.D3 = D3
	        self.D4 = D4
        	self.D5 = D5
	        self.D6 = D6
	        self.D7 = D7

        	GPIO.setmode(GPIO.BCM)        # Use BCM GPIO numbers

	        GPIO.setup(self.E, GPIO.OUT)  # E
        	GPIO.setup(self.RW, GPIO.OUT) # RW
	        GPIO.setup(self.RS, GPIO.OUT) # RS

        	GPIO.setup(self.D0, GPIO.OUT) # DB0
	        GPIO.setup(self.D1, GPIO.OUT) # DB1
        	GPIO.setup(self.D2, GPIO.OUT) # DB2
	        GPIO.setup(self.D3, GPIO.OUT) # DB3
        	GPIO.setup(self.D4, GPIO.OUT) # DB4
	        GPIO.setup(self.D5, GPIO.OUT) # DB5
        	GPIO.setup(self.D6, GPIO.OUT) # DB6
	        GPIO.setup(self.D7, GPIO.OUT) # DB7

        	GPIO.setup(self.CS1, GPIO.OUT) # CS1
	        GPIO.setup(self.CS2, GPIO.OUT) # CS2

        	GPIO.output(self.RS, 0)
	        GPIO.output(self.RW, 0)
        	GPIO.output(self.E, 0)
	        GPIO.output(self.CS1, 0)
	        GPIO.output(self.CS2, 0)
        	GPIO.setup(self.RST, GPIO.OUT) # RST

	        GPIO.output(self.RST, 0)
        	time.sleep(0.01)
	        GPIO.output(self.RST, 1)

        	time.sleep(0.03)

	def useDisp1(self):
        	# use Controller 1 (Display's LEFT part)
        	GPIO.output(self.CS1, 1)
        	GPIO.output(self.CS2, 0)

	def useDisp2(self):
        	# use Controller 2 (Display's LEFT part)
	        GPIO.output(self.CS1, 0)
        	GPIO.output(self.CS2, 1)

	def lcd_byte(self,value, mode):

        	GPIO.output(self.RW,0)
	        GPIO.output(self.RS,mode)
        	GPIO.output(self.D0, (value) & 0x01)
	        GPIO.output(self.D1, (value) & 0x02)
        	GPIO.output(self.D2, (value) & 0x04)
	        GPIO.output(self.D3, (value) & 0x08)
	        GPIO.output(self.D4, (value) & 0x10)
	        GPIO.output(self.D5, (value) & 0x20)
        	GPIO.output(self.D6, (value) & 0x40)
	        GPIO.output(self.D7, (value) & 0x80)

        	# Toggle E
	        time.sleep(self.E_DELAY)
        	GPIO.output(self.E, True)
	        time.sleep(self.E_PULSE)
	        GPIO.output(self.E, False)
        	time.sleep(self.E_DELAY)

        	# Waiting write operation complete by listening BUSY singal

	        GPIO.setup(self.D7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

        	GPIO.output(self.RW,1)
	        GPIO.output(self.RS,0)

        	time.sleep(self.E_DELAY)
	        GPIO.output(self.E, True)
        	time.sleep(self.E_PULSE)
	        GPIO.output(self.E, False)
        	time.sleep(self.E_DELAY)

	        #Wait until BUSY(D7) is off
        	while GPIO.input(self.D7):
			pass

        	GPIO.setup(self.D7, GPIO.OUT) # set D7 back to Output
#############################################################

#################### Clear For Buttons ######################
def clear_for_button1():
                global button4
                button4 = 0
                global button3
                button3 = 0
                global button2
                button2 = 0
                global button5
                button5 = 0
                global button6
                button6 = 0
                global button7
                button7 = 0
                global button8
                button8 = 0
		global reset_button
                reset_button = 0
                global OK_button
                OK_button = 0

def clear_for_button2():
                global button4
                button4 = 0
                global button3
                button3 = 0
                global button5
                button5 = 0
                global button1
                button1 = 0
                global button6
                button6 = 0
                global button7
                button7 = 0
                global button8
                button8 = 0
		global reset_button
                reset_button = 0
                global OK_button
                OK_button = 0
		global button1_counter
		button1_counter = 0

def clear_for_button3():
                global button4
                button4 = 0
                global button5
                button5 = 0
                global button2
                button2 = 0
                global button1
                button1 = 0
                global button6
                button6 = 0
                global button7
                button7 = 0
                global button8
                button8 = 0
		global reset_button
                reset_button = 0
                global OK_button
                OK_button = 0
		global button1_counter
		button1_counter = 0

def clear_for_button4():
                global button5
                button5 = 0
                global button3
                button3 = 0
                global button2
                button2 = 0
                global button1
                button1 = 0
                global button6
                button6 = 0
                global button7
                button7 = 0
                global button8
                button8 = 0
		global reset_button
                reset_button = 0                
		global OK_button
                OK_button = 0
		global button1_counter
		button1_counter = 0

def clear_for_button5():
                global button4
                button4 = 0
                global button3
                button3 = 0
                global button2
                button2 = 0
                global button1
                button1 = 0
		global button6 
		button6 = 0
		global button7
		button7 = 0
		global button8
		button8 = 0
		global reset_button
                reset_button = 0
                global OK_button
                OK_button = 0
		global button1_counter
		button1_counter = 0

def clear_for_button6():
                global button4
                button4 = 0
                global button3
                button3 = 0
                global button2
                button2 = 0
                global button1
                button1 = 0
                global button5
                button5 = 0
                global button7
                button7 = 0
                global button8
                button8 = 0
		global reset_button
                reset_button = 0
                global OK_button
                OK_button = 0
		global button1_counter
		button1_counter = 0

def clear_for_button6():
                global button4
                button4 = 0
                global button3
                button3 = 0
                global button2
                button2 = 0
                global button1
                button1 = 0
                global button5
                button5 = 0
                global button7
                button7 = 0
                global button8
                button8 = 0
		global reset_button
                reset_button = 0
                global OK_button
                OK_button = 0
		global button1_counter
		button1_counter = 0

def clear_for_button7():
                global button4
                button4 = 0
                global button3
                button3 = 0
                global button2
                button2 = 0
                global button1
                button1 = 0
                global button5
                button5 = 0
                global button6
                button6 = 0
                global button8
                button8 = 0
		global reset_button
                reset_button = 0
                global OK_button
                OK_button = 0
		global button1_counter
		button1_counter = 0

def clear_for_button8():
                global button4
                button4 = 0
                global button3
                button3 = 0
                global button2
                button2 = 0
                global button1
                button1 = 0
                global button5
                button5 = 0
                global button7
                button7 = 0
                global button6
                button6 = 0
		global reset_button
                reset_button = 0
                global OK_button
                OK_button = 0
		global button1_counter
		button1_counter = 0

def clear_for_reset_button():	
#-------------- Flags for NURSING submenu -----------
	        global NURSING_LEFT_Submenu_Flag
        	global NURSING_LEFT_Submenu_Flag
        	global NURSING_RIGHT_Submenu_Flag
        	global NURSING_RIGHT_Submenu_Flag
		global Back_Nursing_Left_Flag
	        global Back_Nursing_Right_Flag
#-------------- Flags for FEED submenu --------------
       	 	global FEED_Submenu_Flag
        	global SOLID_Submenu_NEXT_Flag
        	global FORMULA_Submenu_NEXT_Flag
        	global BREAST_MILK_Submenu_NEXT_Flag
        	global BACK_FEED_Option_Flag
        	global BACK_SOLID_Option_Flag_For_Next
        	global BACK_FORMULA_Option_Flag_For_Next
        	global BACK_BREAST_MILK_Option_Flag_For_Next
#--------------- Flages For PUMPING submenu ---------
        	global PUMPING_Submenu_Flag
        	global PUMPING_LEFT_Submenu_Flag
        	global PUMPING_LEFT_START_Submenu_Flag
        	global PUMPING_LEFT_END_Submenu_Flag
        	global PUMPING_RIGHT_Submenu_Flag
        	global PUMPING_RIGHT_START_Submenu_Flag
        	global PUMPING_RIGHT_END_Submenu_Flag
 ##-------------- LEFT ---------------------
        	global Back_Pumping_Left_Flag
        	global Back_Pumping_Left_Start_Flag
        	global Back_Pumping_Left_Start_OZ_Flag
        	global Back_Pumping_Left_End_Flag
        	global Back_Pumping_Left_End_OZ_Flag
 ##--------------RIGHT----------------------
        	global Back_Pumping_Right_Flag
        	global Back_Pumping_Right_Start_Flag
        	global Back_Pumping_Right_Start_OZ_Flag
        	global Back_Pumping_Right_End_Flag
        	global Back_Pumping_Right_End_OZ_Flag
#--------------- Flages For DIAPER submenu ---------
	        global DIAPER_Submenu_Flag
#--------------- Flages For BATH submenu -----------
        	global BATH_Submenu_Flag
#--------------- Flages For SLEEP submenu ----------
        	global SLEEP_Submenu_Flag
#--------------- Flages For MEDICINE submenu -------
        	global MEDICINE_Submenu_Flag

                global button4
                button4 = 0
                global button3
                button3 = 0
                global button2
                button2 = 0
                global button1
                button1 = 0
                global button5
                button5 = 0
                global button7
                button7 = 0
                global button6
                button6 = 0
		global button8
                button8 = 0
		global button1_counter
		button1_counter = 1
                global OK_button
                OK_button = 0

                if(BACK_FEED_Option_Flag != 1 and BACK_SOLID_Option_Flag_For_Next != 1 and BACK_FORMULA_Option_Flag_For_Next != 1):
#			global FEED_Submenu_Flag
                	FEED_Submenu_Flag = 0
#			global SOLID_Submenu_NEXT_Flag
        	        SOLID_Submenu_NEXT_Flag = 0
#			global FORMULA_Submenu_NEXT_Flag
	                FORMULA_Submenu_NEXT_Flag = 0
		if(Back_Pumping_Left_Start_Flag != 1 and Back_Pumping_Left_Start_OZ_Flag != 1 and Back_Pumping_Left_End_Flag != 1 and Back_Pumping_Left_End_OZ_Flag != 1):
# 	                print ' ----- In Clear For RESET Pumping ----- '
			#global PUMPING_Submenu_Flag 
			#PUMPING_Submenu_Flag = 0
#			global PUMPING_LEFT_START_Submenu_Flag
                	PUMPING_LEFT_START_Submenu_Flag = 0
#			global PUMPING_LEFT_END_Submenu_Flag
        	        PUMPING_LEFT_END_Submenu_Flag = 0
#			global PUMPING_RIGHT_START_Submenu_Flag
	                PUMPING_RIGHT_START_Submenu_Flag = 0
#        	        global PUMPING_RIGHT_END_Submenu_Flag
                	PUMPING_RIGHT_END_Submenu_Flag = 0
		if(Back_Pumping_Right_Start_Flag != 1 and Back_Pumping_Right_Start_OZ_Flag != 1 and Back_Pumping_Right_End_Flag != 1 and Back_Pumping_Right_End_OZ_Flag != 1):
#                        print 'in reset pumping'
                        #global PUMPING_Submenu_Flag
                        #PUMPING_Submenu_Flag = 0
#                        global PUMPING_LEFT_START_Submenu_Flag
                        PUMPING_LEFT_START_Submenu_Flag = 0
#                        global PUMPING_LEFT_END_Submenu_Flag
                        PUMPING_LEFT_END_Submenu_Flag = 0
#                        global PUMPING_RIGHT_START_Submenu_Flag
                        PUMPING_RIGHT_START_Submenu_Flag = 0
#                        global PUMPING_RIGHT_END_Submenu_Flag
                        PUMPING_RIGHT_END_Submenu_Flag = 0
 
def clear_for_OK_button():
                global button4
                button4 = 0
                global button3
                button3 = 0
                global button2
                button2 = 0
                global button1
                button1 = 0
                global button5
                button5 = 0
                global button7
                button7 = 0
                global button6
                button6 = 0
                global button8
                button8 = 0
                global reset_button
                reset_button = 0
#############################################################

################## LCD12864 ALL DISPLAY MENU ################
class LCD12864(object):
    def __init__(self, driver):
        self.driver = driver
        self.lcd_init()

    def setPage(self, value):
        # set y=value * 8
        self.driver.lcd_byte(0xB8|(value&0x07),0)

    def setAddress(self, value):
        # set x=value
        self.driver.lcd_byte(0x40|(value&0x3F),0)

    def lcd_cls(self):
        # clear screen by write 0x00 to all display memory
        self.driver.useDisp1()

        for y in range(8):
          self.setPage(y)
          self.setAddress(0)
          for i in range(64):
             self.driver.lcd_byte(0x00,1)

        self.driver.useDisp2()

        for y in range(8):
          self.setPage(y)
          self.setAddress(0)
          for i in range(64):
             self.driver.lcd_byte(0x00,1)

    def lcd_init(self):
        self.driver.useDisp1()
        self.driver.lcd_byte(0x3F,0)
        self.driver.useDisp1()
        self.driver.lcd_byte(0x3F,0)

        self.driver.useDisp2()
        self.driver.lcd_byte(0x3F,0)
        self.driver.useDisp2()
        self.driver.lcd_byte(0x3F,0)
  
    def main_menu(self):
	self.driver.useDisp1()

	#------------- NURSING ----------------
	Display_N_3(0,0,7,self)
	Display_U_3(0,9,15,self)
	Display_R_3(0,16,22,self)
	Display_S_3(0,23,29,self)
	Display_I_3(0,30,36,self)
	Display_N_3(0,38,45,self)
	Display_G_3(0,47,55,self)

	#------------- FEED ----------------
	Display_F_3(2,1,7,self)
        Display_E_3(2,8,14,self)
        Display_E_3(2,15,21,self)
        Display_D_3(2,22,28,self)

	#------------- DIAPER --------
	Display_D_3(4,0,6,self)
	Display_I_3(4,7,13,self)
	Display_A_3(4,15,21,self)
	Display_P_3(4,22,28,self)
	Display_E_3(4,30,36,self)
	Display_R_3(4,37,43,self)

	#------------ SLEEP ----------
	Display_S_3(6,0,6,self)
	Display_L_3(6,7,13,self)
        Display_E_3(6,14,20,self)
        Display_E_3(6,21,27,self)
        Display_P_3(6,28,34,self)
	#Display_1_1(0,0,6,self)
        #Display_2_1(2,0,6,self)
        #Display_3_1(4,0,6,self)
        #Display_4_1(6,0,6,self)

	self.driver.useDisp2()
        #Display_5_1(0,54,60,self)
        #Display_6_1(2,54,60,self)
        #Display_7_1(4,54,60,self)
        #Display_8_1(6,54,60,self)
	#---------- PUMPING ------------

	Display_P_3(0,5,11,self)
        Display_U_3(0,13,19,self)
        Display_M_3(0,20,27,self)
        Display_P_3(0,29,35,self)
        Display_I_3(0,37,43,self)
        Display_N_3(0,45,52,self)
	Display_G_3(0,54,62,self)

	#---------- BATH ---------------
	Display_B_3(2,34,40,self)
        Display_A_3(2,41,47,self)
        Display_T_3(2,48,54,self)
        Display_H_3(2,56,62,self)

	#---------- MEDICINE ------------

        Display_M_3(4,1,8,self)
        Display_E_3(4,10,16,self)
        Display_D_3(4,17,23,self)
        Display_I_3(4,24,30,self)
        Display_C_3(4,32,38,self)
        Display_I_3(4,39,45,self)
        Display_N_3(4,47,54,self)
	Display_E_3(4,56,62,self)

    def DIAPER_SUB_MENU(self):
	self.driver.useDisp1()

	Display_P_3(0,0,6,self)
        Display_E_3(0,8,14,self)
        Display_E_3(0,15,21,self)

	Display_P_3(2,0,6,self)
        Display_O_3(2,8,14,self)
        Display_O_3(2,15,21,self)

	Display_P_3(4,0,6,self)
        Display_E_3(4,8,14,self)
        Display_E_3(4,15,21,self)
        Display_P_3(4,24,30,self)
        Display_O_3(4,32,38,self)
        Display_O_3(4,39,45,self)

	Display_D_3(6,0,6,self)
	Display_R_3(6,8,14,self)
	Display_Y_3(6,15,21,self)

    def BATH_SUB_MENU(self):
	self.driver.useDisp1()
	Display_B_3(0,0,6,self)
        Display_U_3(0,7,13,self)
        Display_B_3(0,14,20,self)
        Display_B_3(0,21,27,self)
        Display_L_3(0,28,34,self)
        Display_E_3(0,35,41,self)

	Display_B_3(0,50,56,self)
        Display_A_3(0,57,63,self)

	self.driver.useDisp2()
	Display_T_3(0,0,6,self)
        Display_H_3(0,8,14,self)

	self.driver.useDisp1()
	Display_S_3(2,0,6,self)
        Display_H_3(2,7,13,self)
        Display_O_3(2,14,20,self)
        Display_W_3(2,21,29,self)
        Display_E_3(2,30,36,self)
        Display_R_3(2,37,43,self)

	Display_S_3(4,0,6,self)
        Display_P_3(4,7,13,self)
        Display_O_3(4,15,21,self)
        Display_N_3(4,22,29,self)
        Display_G_3(4,31,38,self)
        Display_E_3(4,40,46,self)

	Display_B_3(4,50,56,self)
        Display_A_3(4,57,63,self)
        self.driver.useDisp2()
        Display_T_3(4,0,6,self)
        Display_H_3(4,8,14,self)


	self.driver.useDisp1()
	Display_W_3(6,0,8,self)
        Display_A_3(6,9,15,self)
        Display_S_3(6,16,22,self)
        Display_H_3(6,23,29,self)
        Display_E_3(6,30,36,self)
        Display_D_3(6,37,43,self)

	Display_H_3(6,50,56,self)
        Display_A_3(6,57,63,self)

	self.driver.useDisp2()
	Display_I_3(6,0,6,self)
        Display_R_3(6,8,14,self)

    def FEED_SUB_MENU(self):
	self.driver.useDisp1()
        Display_F_3(0,0,6,self)
        Display_O_3(0,7,13,self)
        Display_R_3(0,14,20,self)
        Display_M_3(0,21,28,self)
        Display_U_3(0,30,36,self)
        Display_L_3(0,37,43,self)
	Display_A_3(0,44,50,self)

	Display_B_3(2,0,6,self)
        Display_R_3(2,7,13,self)
        Display_E_3(2,14,20,self)
        Display_A_3(2,21,27,self)
        Display_S_3(2,28,34,self)
        Display_T_3(2,35,41,self)

	Display_M_3(2,48,55,self)
	Display_I_3(2,57,63,self)
	self.driver.useDisp2()
        Display_L_3(2,1,7,self)
        Display_K_3(2,8,15,self)
	
	self.driver.useDisp1()
	Display_S_3(4,0,6,self)
        Display_O_3(4,7,13,self)
        Display_L_3(4,14,20,self)
        Display_I_3(4,21,27,self)
        Display_D_3(4,29,35,self)
	Display_S_3(4,36,42,self)

    def SOLIDS_SUB_MENU(self):
	self.driver.useDisp1()
	#----------- CEREAL -----------
	Display_C_3(0,0,6,self)
        Display_E_3(0,7,13,self)
        Display_R_3(0,14,20,self)
        Display_E_3(0,21,27,self)
        Display_A_3(0,28,34,self)
        Display_L_3(0,35,41,self)

	#---------- VEGGIES -----------
	Display_V_3(2,0,7,self)
        Display_E_3(2,8,14,self)
        Display_G_3(2,15,23,self)
        Display_G_3(2,24,32,self)
        Display_I_3(2,33,39,self)
        Display_E_3(2,41,47,self)
	Display_S_3(2,48,54,self)

	#---------- FRUIT ------------
	Display_F_3(4,0,6,self)
        Display_R_3(4,7,13,self)
        Display_U_3(4,14,20,self)
        Display_I_3(4,21,27,self)
        Display_T_3(4,29,35,self)

	#---------- JUICE -----------
        Display_J_3(6,0,6,self)
        Display_U_3(6,7,13,self)
        Display_I_3(6,14,20,self)
        Display_C_3(6,22,28,self)
        Display_E_3(6,29,35,self)
	
	
	self.driver.useDisp2()
	#----------- MEAT ------------
	Display_M_3(0,33,40,self)
        Display_E_3(0,42,48,self)
        Display_A_3(0,49,55,self)
        Display_T_3(0,56,62,self)

	#----------- BREAD -----------
	Display_B_3(2,28,34,self)
	Display_R_3(2,35,41,self)
        Display_E_3(2,42,48,self)
        Display_A_3(2,49,55,self)
        Display_D_3(2,56,62,self)

	#----------- YOGURT -----------
        Display_Y_3(4,18,25,self)
	Display_O_3(4,26,32,self)
        Display_G_3(4,33,41,self)
        Display_U_3(4,42,48,self)
        Display_R_3(4,49,55,self)
        Display_T_3(4,56,62,self)
	
	#----------- NEXT -----------
	Display_N_3(6,31,38,self)
        Display_E_3(6,40,46,self)
        Display_X_3(6,47,54,self)
        Display_T_3(6,56,62,self)
    
    def SOLIDS_SUB_MENU_NEXT(self):
	self.driver.useDisp1()
	#----------- DAIRY -----------
        Display_D_3(0,0,6,self)
        Display_A_3(0,7,13,self)
        Display_I_3(0,14,20,self)
        Display_R_3(0,22,28,self)
        Display_Y_3(0,29,36,self)

	#----------- FISH -----------
        Display_F_3(2,0,6,self)
        Display_I_3(2,7,13,self)
        Display_S_3(2,15,21,self)
        Display_H_3(2,22,28,self)

	#----------- PASTA -----------
        Display_P_3(4,0,7,self)
        Display_A_3(4,8,14,self)
        Display_S_3(4,15,21,self)
        Display_T_3(4,22,28,self)
        Display_A_3(4,30,36,self)

	#---------- FINGER FOODS -----------
        Display_F_3(6,0,6,self)
        Display_I_3(6,7,14,self)
        Display_N_3(6,16,23,self)
        Display_G_3(6,25,33,self)
        Display_E_3(6,34,40,self)
        Display_R_3(6,41,47,self)

	Display_F_3(6,57,63,self)
	self.driver.useDisp2()
	Display_O_3(6,0,6,self)
        Display_O_3(6,7,13,self)
        Display_D_3(6,14,20,self)
	Display_S_3(6,21,27,self)

    def FORMULA_SUB_MENU(self):
	self.driver.useDisp1()
	#--------------------- 1 OZ --------------
        Display_1_1(0,0,6,self)
	Display_O_3(0,9,15,self)
        Display_Z_3(0,16,24,self)

	#--------------------- 2 OZ --------------
        Display_2_1(2,0,6,self)
        Display_O_3(2,9,15,self)
        Display_Z_3(2,16,24,self)

	#--------------------- 3 OZ --------------
        Display_3_1(4,0,6,self)
        Display_O_3(4,9,15,self)
        Display_Z_3(4,16,24,self)

	#--------------------- 4 OZ --------------
        Display_4_1(6,0,6,self)
        Display_O_3(6,9,15,self)
        Display_Z_3(6,16,24,self)

	self.driver.useDisp2()
        #--------------------- 5 OZ --------------
        Display_5_1(0,38,44,self)
        Display_O_3(0,47,53,self)
        Display_Z_3(0,54,62,self)

	#--------------------- 6 OZ --------------
        Display_6_1(2,38,44,self)
        Display_O_3(2,47,53,self)
        Display_Z_3(2,54,62,self) 

        #--------------------- 7 OZ --------------
        Display_7_1(4,38,44,self)
        Display_O_3(4,47,53,self)
        Display_Z_3(4,54,62,self)

	#----------- NEXT -----------
        Display_N_3(6,31,38,self)
        Display_E_3(6,40,46,self)
        Display_X_3(6,47,54,self)
        Display_T_3(6,56,62,self)

    def FORMULA_SUB_MENU_NEXT(self):
	self.driver.useDisp1()
        #--------------------- 8 OZ --------------
        Display_8_1(0,0,6,self)
        Display_O_3(0,9,15,self)
        Display_Z_3(0,16,24,self)

        #--------------------- 9 OZ --------------
        Display_9_1(2,0,6,self)
        Display_O_3(2,9,15,self)
        Display_Z_3(2,16,24,self)

    def BREAST_MILK_SUB_MENU(self):
	self.driver.useDisp1()
        #--------------------- 1 OZ --------------
        Display_1_1(0,0,6,self)
        Display_O_3(0,9,15,self)
        Display_Z_3(0,16,24,self)

        #--------------------- 2 OZ --------------
        Display_2_1(2,0,6,self)
        Display_O_3(2,9,15,self)
        Display_Z_3(2,16,24,self)

        #--------------------- 3 OZ --------------
        Display_3_1(4,0,6,self)
        Display_O_3(4,9,15,self)
        Display_Z_3(4,16,24,self)

        #--------------------- 4 OZ --------------
        Display_4_1(6,0,6,self)
        Display_O_3(6,9,15,self)
        Display_Z_3(6,16,24,self)

        self.driver.useDisp2()
        #--------------------- 5 OZ --------------
        Display_5_1(0,38,44,self)
        Display_O_3(0,47,53,self)
        Display_Z_3(0,54,62,self)
	
	#--------------------- 6 OZ --------------
        Display_6_1(2,38,44,self)
        Display_O_3(2,47,53,self)
        Display_Z_3(2,54,62,self)

        #--------------------- 7 OZ --------------
        Display_7_1(4,38,44,self)
        Display_O_3(4,47,53,self)
        Display_Z_3(4,54,62,self)

        #----------- NEXT -----------
        Display_N_3(6,31,38,self)
        Display_E_3(6,40,46,self)
        Display_X_3(6,47,54,self)
        Display_T_3(6,56,62,self)
	
    def BREAST_MILK_SUB_MENU_NEXT(self):
        self.driver.useDisp1()
        #--------------------- 8 OZ --------------
        Display_8_1(0,0,6,self)
        Display_O_3(0,9,15,self)
        Display_Z_3(0,16,24,self)

        #--------------------- 9 OZ --------------
        Display_9_1(2,0,6,self)
        Display_O_3(2,9,15,self)
        Display_Z_3(2,16,24,self)
    
    def PUMPING_SUB_MENU(self):
	self.driver.useDisp1()
	#--------------- LEFT ------------------
        Display_L_3(0,1,7,self)
        Display_E_3(0,8,14,self)
        Display_F_3(0,15,21,self)
        Display_T_3(0,22,28,self)
	#-------------- RIGHT ------------------
        Display_R_3(2,1,7,self)
        Display_I_3(2,8,15,self)
        Display_G_3(2,17,24,self)
        Display_H_3(2,26,32,self)
        Display_T_3(2,33,39,self)
    
    def PUMPING_LEFT_SUB_MENU(self):
	#--------------- START ------------------
        self.driver.useDisp1()
        Display_S_3(0,1,7,self)
        Display_T_3(0,8,14,self)
        Display_A_3(0,15,21,self)
        Display_R_3(0,22,28,self)
        Display_T_3(0,29,35,self)
	#--------------- END ------------------
        self.driver.useDisp1()
        Display_E_3(2,1,7,self)
        Display_N_3(2,8,15,self)
        Display_D_3(2,17,23,self)

    def PUMPING_LEFT_START_SUB_MENU(self):
	self.driver.useDisp1()
        #--------------------- 1 OZ --------------
        Display_1_1(0,0,6,self)
        Display_O_3(0,9,15,self)
        Display_Z_3(0,16,24,self)

        #--------------------- 2 OZ --------------
        Display_2_1(2,0,6,self)
        Display_O_3(2,9,15,self)
        Display_Z_3(2,16,24,self)

        #--------------------- 3 OZ --------------
        Display_3_1(4,0,6,self)
        Display_O_3(4,9,15,self)
        Display_Z_3(4,16,24,self)

        #--------------------- 4 OZ --------------
        Display_4_1(6,0,6,self)
        Display_O_3(6,9,15,self)
        Display_Z_3(6,16,24,self)

        self.driver.useDisp2()
        #--------------------- 5 OZ --------------
        Display_5_1(0,38,44,self)
        Display_O_3(0,47,53,self)
        Display_Z_3(0,54,62,self)

    def PUMPING_LEFT_END_SUB_MENU(self):
        self.driver.useDisp1()
        #--------------------- 6 OZ --------------
        Display_6_1(0,0,6,self)
        Display_O_3(0,9,15,self)
        Display_Z_3(0,16,24,self)

        #--------------------- 7 OZ --------------
        Display_7_1(2,0,6,self)
        Display_O_3(2,9,15,self)
        Display_Z_3(2,16,24,self)

        #--------------------- 8 OZ --------------
        Display_8_1(4,0,6,self)
        Display_O_3(4,9,15,self)
        Display_Z_3(4,16,24,self)

        #--------------------- 9 OZ --------------
        Display_9_1(6,0,6,self)
        Display_O_3(6,9,15,self)
        Display_Z_3(6,16,24,self)

    def PUMPING_RIGHT_SUB_MENU(self):
        #--------------- START ------------------
        self.driver.useDisp1()
        Display_S_3(0,1,7,self)
        Display_T_3(0,8,14,self)
        Display_A_3(0,15,21,self)
        Display_R_3(0,22,28,self)
        Display_T_3(0,29,35,self)
        #--------------- END ------------------
        self.driver.useDisp1()
        Display_E_3(2,1,7,self)
        Display_N_3(2,8,15,self)
        Display_D_3(2,17,23,self)

    def PUMPING_RIGHT_START_SUB_MENU(self):
        self.driver.useDisp1()
        #--------------------- 1 OZ --------------
        Display_1_1(0,0,6,self)
        Display_O_3(0,9,15,self)
        Display_Z_3(0,16,24,self)

        #--------------------- 2 OZ --------------
        Display_2_1(2,0,6,self)
        Display_O_3(2,9,15,self)
        Display_Z_3(2,16,24,self)

        #--------------------- 3 OZ --------------
        Display_3_1(4,0,6,self)
        Display_O_3(4,9,15,self)
        Display_Z_3(4,16,24,self)

        #--------------------- 4 OZ --------------
        Display_4_1(6,0,6,self)
        Display_O_3(6,9,15,self)
        Display_Z_3(6,16,24,self)

        self.driver.useDisp2()
        #--------------------- 5 OZ --------------
        Display_5_1(0,38,44,self)
        Display_O_3(0,47,53,self)
        Display_Z_3(0,54,62,self)

    def PUMPING_RIGHT_END_SUB_MENU(self):
        self.driver.useDisp1()
        #--------------------- 6 OZ --------------
        Display_6_1(0,0,6,self)
        Display_O_3(0,9,15,self)
        Display_Z_3(0,16,24,self)

        #--------------------- 7 OZ --------------
        Display_7_1(2,0,6,self)
        Display_O_3(2,9,15,self)
        Display_Z_3(2,16,24,self)

        #--------------------- 8 OZ --------------
        Display_8_1(4,0,6,self)
        Display_O_3(4,9,15,self)
        Display_Z_3(4,16,24,self)

        #--------------------- 9 OZ --------------
        Display_9_1(6,0,6,self)
        Display_O_3(6,9,15,self)
        Display_Z_3(6,16,24,self)

    def SLEEP_SUB_MENU(self):
        #--------------- START ------------------
        self.driver.useDisp1()
        Display_S_3(0,1,7,self)
        Display_T_3(0,8,14,self)
        Display_A_3(0,15,21,self)
        Display_R_3(0,22,28,self)
        Display_T_3(0,29,35,self)
        #--------------- END ------------------
        self.driver.useDisp1()
        Display_E_3(2,1,7,self)
        Display_N_3(2,8,15,self)
        Display_D_3(2,17,23,self)

    def NURSING_SUB_MENU(self):
        self.driver.useDisp1()
        #--------------- LEFT ------------------
        Display_L_3(0,1,7,self)
        Display_E_3(0,8,14,self)
        Display_F_3(0,15,21,self)
        Display_T_3(0,22,28,self)
        #-------------- RIGHT ------------------
        Display_R_3(2,1,7,self)
        Display_I_3(2,8,15,self)
        Display_G_3(2,17,24,self)
        Display_H_3(2,26,32,self)
        Display_T_3(2,33,39,self)
    
    def NURSING1_SUB_MENU(self):
        #--------------- START ------------------
        self.driver.useDisp1()
        Display_S_3(0,1,7,self)
        Display_T_3(0,8,14,self)
        Display_A_3(0,15,21,self)
        Display_R_3(0,22,28,self)
        Display_T_3(0,29,35,self)
        #--------------- END ------------------
        self.driver.useDisp1()
        Display_E_3(2,1,7,self)
        Display_N_3(2,8,15,self)
        Display_D_3(2,17,23,self)

    def NURSING_LEFT_SUB_MENU(self):
        #--------------- START ------------------
        self.driver.useDisp1()
        Display_S_3(0,1,7,self)
        Display_T_3(0,8,14,self)
        Display_A_3(0,15,21,self)
        Display_R_3(0,22,28,self)
        Display_T_3(0,29,35,self)
        #--------------- END ------------------
        self.driver.useDisp1()
        Display_E_3(2,1,7,self)
        Display_N_3(2,8,15,self)
        Display_D_3(2,17,23,self)
    
    def NURSING_RIGHT_SUB_MENU(self):
        #--------------- START ------------------
        self.driver.useDisp1()
        Display_S_3(0,1,7,self)
        Display_T_3(0,8,14,self)
        Display_A_3(0,15,21,self)
        Display_R_3(0,22,28,self)
        Display_T_3(0,29,35,self)
        #--------------- END ------------------
        self.driver.useDisp1()
        Display_E_3(2,1,7,self)
        Display_N_3(2,8,15,self)
        Display_D_3(2,17,23,self)

    def menu_1(self):
	self.driver.useDisp1()
        Display_1_1(0,0,6,self)
	Display_1_1(0,6,12,self)
	Display_1_1(2,0,6,self)
        Display_2_1(2,6,12,self)
	Display_1_1(4,0,6,self)
        Display_3_1(4,6,12,self)
	Display_1_1(6,0,6,self)
        Display_4_1(6,6,12,self)

        self.driver.useDisp2()
	Display_1_1(0,48,54,self)
        Display_5_1(0,54,60,self)
	
    def menu_11(self):
        self.driver.useDisp1()
        Display_1_1(0,0,6,self)
        Display_1_1(0,6,12,self)
        Display_1_1(0,12,18,self)

	Display_1_1(2,0,6,self)
        Display_1_1(2,6,12,self)
        Display_2_1(2,12,18,self)

        Display_1_1(4,0,6,self)
	Display_1_1(4,6,12,self)
        Display_3_1(4,12,18,self)         

    def Font_3(self):
	self.driver.useDisp1()
        Display_I_3(0,0,6,self)	
	Display_C_3(0,8,14,self)
	Display_J_3(0,15,21,self)
	Display_L_3(0,22,28,self)
	Display_P_3(0,29,35,self)
	Display_O_3(0,37,43,self)
	Display_U_3(0,44,50,self)
	Display_S_3(0,51,57,self)

	Display_R_3(2,0,6,self)
	Display_K_3(2,7,13,self)
	Display_V_3(2,14,20,self)
	Display_M_3(2,22,29,self)
	Display_W_3(2,31,38,self)
        Display_N_3(2,40,47,self)
	Display_Z_3(2,49,57,self)
	Display_X_3(4,0,8,self)
        Display_G_3(4,9,16,self)
	Display_Q_3(4,18,26,self)

    def Alphabet_for_Font3(self):
        self.driver.useDisp1()
	Display_A_3(0,0,6,self)
	Display_B_3(0,7,13,self)
	Display_C_3(0,14,20,self)
	Display_D_3(0,21,27,self)
	Display_E_3(0,28,34,self)
	Display_F_3(0,35,41,self)
	Display_G_3(0,42,50,self)
	Display_H_3(0,51,57,self)

        Display_I_3(2,0,6,self)
        Display_J_3(2,8,14,self)
        Display_K_3(2,15,21,self)	
        Display_L_3(2,22,28,self)
        Display_M_3(2,29,36,self)
	Display_N_3(2,38,45,self)
        Display_O_3(2,47,53,self)
	Display_P_3(2,54,60,self)

	Display_Q_3(4,0,8,self)
	Display_R_3(4,9,15,self)
	Display_S_3(4,16,22,self)
	Display_T_3(4,23,29,self)
	Display_U_3(4,31,37,self)
	Display_V_3(4,38,45,self)
	Display_W_3(4,46,54,self)
	
	Display_X_3(6,0,8,self)
        Display_Y_3(6,9,16,self)
        Display_Z_3(6,17,24,self)

    def NURSING(self):
        self.driver.useDisp1()
#--------------- NURSING ------------------
        Display_N_3(0,1,9,self)
        Display_U_3(0,10,16,self)
        Display_R_3(0,17,23,self)
        Display_S_3(0,24,30,self)
        Display_I_3(0,31,37,self)
        Display_N_3(0,39,47,self)
        Display_G_3(0,48,55,self)

    def LEFT_RIGHT(self):
        self.driver.useDisp1()
#--------------- LEFT ------------------
        Display_L_3(0,1,7,self)
        Display_E_3(0,8,14,self)
        Display_F_3(0,15,21,self)
        Display_T_3(0,22,28,self)
#--------------- RIGHT ------------------
        Display_R_3(2,1,7,self)
        Display_I_3(2,8,15,self)
        Display_G_3(2,17,24,self)
        Display_H_3(2,26,32,self)
        Display_T_3(2,33,39,self)

    def START_END(self):
#--------------- START ------------------
 	self.driver.useDisp1()
        Display_S_3(0,1,7,self)
        Display_T_3(0,8,14,self)
        Display_A_3(0,15,21,self)
        Display_R_3(0,22,28,self)
	Display_T_3(0,29,35,self)
#--------------- END ------------------
 	self.driver.useDisp2()
        Display_E_3(6,34,40,self)
        Display_N_3(6,41,49,self)
        Display_D_3(6,50,56,self)
    
    def NUMBERS(self):
    	self.driver.useDisp1()
        Display_0_1(0,0,6,self)
        Display_1_1(0,8,14,self)
	Display_2_1(0,15,21,self)
	Display_3_1(0,22,28,self)
	Display_4_1(0,29,35,self)
	Display_5_1(0,37,43,self)
	Display_6_1(0,44,50,self)
	Display_7_1(0,51,57,self)
	Display_8_1(2,0,6,self)
	Display_9_1(2,8,14,self)


    def FEED_BATH(self):
	self.driver.useDisp1()	
	
#--------------- FEED ------------------
	Display_F_3(0,1,7,self)
	Display_E_3(0,8,14,self)
	Display_E_3(0,15,21,self)
	Display_D_3(0,22,28,self)

	Display_F_3(2,1,7,self)
	Display_E_3(2,8,14,self)
        Display_E_3(2,15,21,self)
        Display_D_3(2,22,28,self)

	Display_F_3(4,1,7,self)
	Display_E_3(4,8,14,self)
        Display_E_3(4,15,21,self)
        Display_D_3(4,22,28,self)

	Display_F_3(6,1,7,self)
	Display_E_3(6,8,14,self)
        Display_E_3(6,15,21,self)
        Display_D_3(6,22,28,self)

#---------------- BATH -------------------
	self.driver.useDisp2()
	Display_B_3(0,34,40,self)
        Display_A_3(0,41,47,self)
        Display_T_3(0,48,54,self)
        Display_H_3(0,56,62,self)

	Display_B_3(2,34,40,self)
        Display_A_3(2,41,47,self)
        Display_T_3(2,48,54,self)
        Display_H_3(2,56,62,self)

	Display_B_3(4,34,40,self)
        Display_A_3(4,41,47,self)
        Display_T_3(4,48,54,self)
        Display_H_3(4,56,62,self)

	Display_B_3(6,34,40,self)
        Display_A_3(6,41,47,self)
        Display_T_3(6,48,54,self)
        Display_H_3(6,56,62,self)
#############################################################

###################### Character Libraries ##################
#---------------- For Displaying H on GLCD ---------------
def Display_H_3(Page_No, Start_Range, End_Range ,self):
        self.setPage(Page_No)
        for i in range(Start_Range,(End_Range)):
                self.setAddress(i)
                self.driver.lcd_byte(0X20,1)

        self.setPage(Page_No)        
	self.setAddress(Start_Range)
        self.driver.lcd_byte(0xFE,1)

        self.setPage(Page_No)
        self.setAddress(Start_Range+5)
        self.driver.lcd_byte(0xFE,1)

	self.setPage(Page_No+1)
        self.setAddress(Start_Range)
        self.driver.lcd_byte(0x03,1)

	self.setPage(Page_No+1)
        self.setAddress(Start_Range+5)
        self.driver.lcd_byte(0x03,1)

#--------------For Displying L_3 on GLCD-------------------
def Display_L_3(Page_No, Start_Range, End_Range ,self):

        self.setPage(Page_No+1)
        for i in range(Start_Range,End_Range):
                self.setAddress(i)
                self.driver.lcd_byte(0X02,1)

        self.setPage(Page_No)
        self.setAddress(Start_Range)
        self.driver.lcd_byte(0xFE,1)

        self.setPage(Page_No+1)
        self.setAddress(Start_Range)
        self.driver.lcd_byte(0x03,1)
       
#--------------- For Displaying C_3 on GLCD ----------------
def Display_C_3(Page_No, Start_Range, End_Range ,self):

        self.setPage(Page_No)
        for i in range(Start_Range,End_Range):
                self.setAddress(i)
                self.driver.lcd_byte(0X02,1)

        self.setPage(Page_No+1)
        for i in range(Start_Range,End_Range):
                self.setAddress(i)
                self.driver.lcd_byte(0X02,1)

        self.setPage(Page_No)
        self.setAddress(Start_Range)
        self.driver.lcd_byte(0xFE,1)

        self.setPage(Page_No+1)
        self.setAddress(Start_Range)
        self.driver.lcd_byte(0x03,1)

#--------------- For Displaying O_3 on GLCD ----------------
def Display_O_3(Page_No, Start_Range, End_Range ,self):

        self.setPage(Page_No)
        for i in range(Start_Range,End_Range):
                self.setAddress(i)
                self.driver.lcd_byte(0X02,1)

	self.setPage(Page_No+1)
        for i in range(Start_Range,End_Range):
                self.setAddress(i)
                self.driver.lcd_byte(0X02,1)

        self.setPage(Page_No)
        self.setAddress(Start_Range)
        self.driver.lcd_byte(0xFE,1)

        self.setPage(Page_No)
        self.setAddress(Start_Range + 5)
        self.driver.lcd_byte(0xFE,1)

	self.setPage(Page_No+1)
        self.setAddress(Start_Range)
        self.driver.lcd_byte(0x03,1)

        self.setPage(Page_No+1)
        self.setAddress(Start_Range + 5)
        self.driver.lcd_byte(0x03,1)
	
#--------------- For Displaying E_3 on GLCD ----------------
def Display_E_3(Page_No, Start_Range, End_Range ,self):

        self.setPage(Page_No)
        for i in range(Start_Range,(End_Range)):
                self.setAddress(i)
                self.driver.lcd_byte(0X22,1)

        self.setPage(Page_No)
        self.setAddress(Start_Range)
        self.driver.lcd_byte(0xFE,1)

	self.setPage(Page_No+1)
        for i in range(Start_Range,(End_Range)):
                self.setAddress(i)
                self.driver.lcd_byte(0X02,1)

        self.setPage(Page_No+1)
        self.setAddress(Start_Range)
        self.driver.lcd_byte(0x03,1)
      
#--------------- For Displaying F_3 on GLCD ----------------
def Display_F_3(Page_No, Start_Range, End_Range ,self):

        self.setPage(Page_No)
        for i in range(Start_Range,End_Range):
                self.setAddress(i)
                self.driver.lcd_byte(0X22,1)

        self.setPage(Page_No)
        self.setAddress(Start_Range)
        self.driver.lcd_byte(0xFE,1)

	self.setPage(Page_No+1)
        self.setAddress(Start_Range)
        self.driver.lcd_byte(0x03,1)

#---------------- For Displaying U_3 On GLCD ----------------
def Display_U_3(Page_No, Start_Range, End_Range ,self):
        self.setPage(Page_No+1)
        for i in range(Start_Range,End_Range):
                self.setAddress(i)
                self.driver.lcd_byte(0X02,1)

        self.setPage(Page_No)
        self.setAddress(Start_Range)
        self.driver.lcd_byte(0xFE,1)

        self.setPage(Page_No)
        self.setAddress(Start_Range+5)
        self.driver.lcd_byte(0xFE,1)

        self.setPage( (Page_No + 1) )
        self.setAddress(Start_Range)
        self.driver.lcd_byte(0x03,1)

        self.setPage( (Page_No + 1) )
        self.setAddress(Start_Range+5)
        self.driver.lcd_byte(0x03,1)

#----------------- For Displaying S_3 on GLCD ----------------
def Display_S_3(Page_No, Start_Range, End_Range ,self):
        self.setPage(Page_No)
        for i in range(Start_Range,End_Range):
                self.setAddress(i)
                self.driver.lcd_byte(0X22,1)

        self.setPage(Page_No+1)
        for i in range(Start_Range,End_Range):
                self.setAddress(i)
                self.driver.lcd_byte(0X02,1)

        self.setPage(Page_No)
        self.setAddress(Start_Range)
        self.driver.lcd_byte(0x3E,1)

	self.setPage(Page_No)
        self.setAddress(Start_Range+5)
        self.driver.lcd_byte(0xE2,1)

        self.setPage(Page_No+1)
        self.setAddress(Start_Range+5)
        self.driver.lcd_byte(0x03,1)

#---------------- For Displaying I_3 on GLCD ----------------
def Display_I_3(Page_No, Start_Range, End_Range ,self):
        self.setPage(Page_No)
        for i in range(Start_Range,(End_Range+1)):
                self.setAddress(i)
                self.driver.lcd_byte(0X02,1)
	
	self.setPage(Page_No+1)
        for i in range(Start_Range,(End_Range+1)):
                self.setAddress(i)
                self.driver.lcd_byte(0X02,1)


        self.setPage(Page_No)
        self.setAddress(Start_Range+3)
        self.driver.lcd_byte(0xFE,1)

        self.setPage(Page_No+1)
        self.setAddress(Start_Range+3)
        self.driver.lcd_byte(0x03,1)

#----------------- For Displaying T_3 on GLCD ----------------
def Display_T_3(Page_No, Start_Range, End_Range ,self):
        self.setPage(Page_No)
        for i in range(Start_Range,(End_Range+1)):
                self.setAddress(i)
                self.driver.lcd_byte(0X02,1)

        self.setPage(Page_No)
        self.setAddress(Start_Range+3)
        self.driver.lcd_byte(0xFE,1)

	self.setPage(Page_No + 1 )
        self.setAddress(Start_Range+3)
        self.driver.lcd_byte(0x03,1)

#----------------- For Displaying P_3 on GLCD ----------------
def Display_P_3(Page_No, Start_Range, End_Range ,self):
        self.setPage(Page_No)
        for i in range(Start_Range,(End_Range)):
                self.setAddress(i)
                self.driver.lcd_byte(0X22,1)

        self.setPage(Page_No)
        self.setAddress(Start_Range)
        self.driver.lcd_byte(0xFE,1)

        self.setPage(Page_No)
        self.setAddress(Start_Range+6)
        self.driver.lcd_byte(0x3E,1)

        self.setPage(Page_No+1)
        self.setAddress(Start_Range)
        self.driver.lcd_byte(0x03,1)

#---------------- For Displaying A_3 On GLCD --------------
def Display_A_3(Page_No, Start_Range, End_Range ,self):
        self.setPage(Page_No)
        for i in range(Start_Range,End_Range):
                self.setAddress(i)
                self.driver.lcd_byte(0X22,1)

        self.setPage(Page_No)
        self.setAddress(Start_Range)
        self.driver.lcd_byte(0xFC,1)

        self.setPage(Page_No)
        self.setAddress(Start_Range+5)
        self.driver.lcd_byte(0xFC,1)

	self.setPage(Page_No+1)
        self.setAddress(Start_Range)
        self.driver.lcd_byte(0x03,1)

        self.setPage(Page_No+1)
        self.setAddress(Start_Range+5)
        self.driver.lcd_byte(0x03,1)

#-------------------- Displaying R_3 on GLCD -----------------
def Display_R_3(Page_No, Start_Range, End_Range ,self):

        self.setPage(Page_No)
        for i in range(Start_Range,(End_Range)):
                self.setAddress(i)
                self.driver.lcd_byte(0X22,1)

        self.setPage(Page_No)
        self.setAddress(Start_Range)
        self.driver.lcd_byte(0xFE,1)

        self.setPage(Page_No)
        self.setAddress(Start_Range+5)
        self.driver.lcd_byte(0x3E,1)

        self.setPage(Page_No + 1)
        self.setAddress(Start_Range)
        self.driver.lcd_byte(0x03,1)

	self.setPage(Page_No)
        self.setAddress(Start_Range+1)
        self.driver.lcd_byte(0x62,1)
        self.setAddress(Start_Range+2)
        self.driver.lcd_byte(0xA2,1)
	
	self.setPage(Page_No + 1)
        self.setAddress(Start_Range+3)
        self.driver.lcd_byte(0x01,1)
        self.setAddress(Start_Range+4)
        self.driver.lcd_byte(0x02,1)
        self.setAddress(Start_Range+5)
        self.driver.lcd_byte(0x02,1)

#------------- Displaying Z_3 on GLCD ------------------
def Display_Z_3(Page_No, Start_Range, End_Range ,self):

        self.setPage(Page_No)
        for i in range(Start_Range,End_Range):
                self.setAddress(i)
                self.driver.lcd_byte(0X02,1)

        self.setPage(Page_No+1)
        for i in range(Start_Range,End_Range):
                self.setAddress(i)
                self.driver.lcd_byte(0X02,1)
	
	self.setPage(Page_No)
        self.setAddress(Start_Range+7)
        self.driver.lcd_byte(0x06,1)

        self.setPage(Page_No)
        self.setAddress(Start_Range+6)
        self.driver.lcd_byte(0x06,1)

        self.setPage(Page_No)
        self.setAddress(Start_Range+5)
        self.driver.lcd_byte(0x0A,1)

        self.setPage(Page_No)
        self.setAddress(Start_Range+4)
        self.driver.lcd_byte(0x12,1)

        self.setPage(Page_No)
        self.setAddress(Start_Range+3)
        self.driver.lcd_byte(0x22,1)

        self.setPage(Page_No)
        self.setAddress(Start_Range+2)
	self.driver.lcd_byte(0x42,1)

        self.setPage(Page_No)
        self.setAddress(Start_Range+1)
        self.driver.lcd_byte(0x82,1)
	
	self.setPage(Page_No+1)
        self.setAddress(Start_Range)
        self.driver.lcd_byte(0x03,1)

	self.setPage(Page_No+1)
        self.setAddress(Start_Range+1)
        self.driver.lcd_byte(0x03,1)

#------------- Displaying J_3 on GLCD ------------------
def Display_J_3(Page_No, Start_Range, End_Range ,self):
        self.setPage(Page_No+1)
        for i in range(Start_Range,(End_Range-2)):
                self.setAddress(i)
                self.driver.lcd_byte(0X02,1)

        self.setPage(Page_No)
        for i in range((Start_Range+1),(End_Range)):
                self.setAddress(i)
                self.driver.lcd_byte(0X02,1)

        self.setPage(Page_No)
        self.setAddress(Start_Range+3)
        self.driver.lcd_byte(0xFE,1)

	self.setPage(Page_No)
        self.setAddress(Start_Range)
        self.driver.lcd_byte(0x80,1)

        self.setPage(Page_No+1)
        self.setAddress(Start_Range+3)
        self.driver.lcd_byte(0x03,1)

        self.setPage(Page_No+1)
        self.setAddress(Start_Range)
        self.driver.lcd_byte(0x03,1)

#------------- Displaying K_3 on GLCD ------------------
def Display_K_3(Page_No, Start_Range, End_Range ,self):

        self.setPage(Page_No)
        self.setAddress(Start_Range)
        self.driver.lcd_byte(0xFE,1)

        self.setPage(Page_No + 1)
        self.setAddress(Start_Range)
        self.driver.lcd_byte(0x03,1)

	self.setPage(Page_No)
        self.setAddress(Start_Range+5)
        self.driver.lcd_byte(0x02,1)
        self.setAddress(Start_Range+4)
        self.driver.lcd_byte(0x04,1)
        self.setAddress(Start_Range+3)
        self.driver.lcd_byte(0x88,1)
        self.setAddress(Start_Range+2)
        self.driver.lcd_byte(0x50,1)
        self.setAddress(Start_Range+1)
        self.driver.lcd_byte(0x20,1)

        self.setPage(Page_No+1)
        self.setAddress(Start_Range+4)
        self.driver.lcd_byte(0x01,1)
        self.setAddress(Start_Range+5)
        self.driver.lcd_byte(0x02,1)

#------------------- For Displaying Q_3 On GLCD -------------------
def Display_Q_3(Page_No, Start_Range, End_Range ,self):

        self.setPage(Page_No)
        for i in range(Start_Range,(End_Range-2)):
                self.setAddress(i)
                self.driver.lcd_byte(0X02,1)

        self.setPage(Page_No+1)
        for i in range(Start_Range,End_Range-2):
                self.setAddress(i)
                self.driver.lcd_byte(0X02,1)

        self.setPage(Page_No)
        self.setAddress(Start_Range)
        self.driver.lcd_byte(0xFE,1)

        self.setPage(Page_No+1)
        self.setAddress(Start_Range)
        self.driver.lcd_byte(0x03,1)

        self.setPage(Page_No)
        self.setAddress(Start_Range + 5)
        self.driver.lcd_byte(0xFE,1)

        self.setPage(Page_No+1)
        self.setAddress(Start_Range + 5)
        self.driver.lcd_byte(0x03,1)

	self.setPage(Page_No)
        self.setAddress(Start_Range+2)
        self.driver.lcd_byte(0x42,1)
	self.setAddress(Start_Range+3)
        self.driver.lcd_byte(0x82,1)
	
	self.setPage(Page_No+1)
        self.setAddress(Start_Range+4)
        self.driver.lcd_byte(0x03,1)
        self.setAddress(Start_Range+6)
        self.driver.lcd_byte(0x01,1)
	self.setAddress(Start_Range+7)
        self.driver.lcd_byte(0x01,1)


#-------------- Displaying V_3 on GLCD ----------------
def Display_V_3(Page_No, Start_Range, End_Range ,self):

        self.setPage(Page_No)
        self.setAddress(Start_Range+0)
        self.driver.lcd_byte(0x7E,1)
        self.setAddress(Start_Range+1)
        self.driver.lcd_byte(0x80,1)
	
	self.setPage(Page_No + 1)
        self.setAddress(Start_Range+2)
        self.driver.lcd_byte(0x01,1)
        self.setAddress(Start_Range+3)
        self.driver.lcd_byte(0x02,1)
        self.setAddress(Start_Range+4)
        self.driver.lcd_byte(0x01,1)
	
	self.setPage(Page_No)
        self.setAddress(Start_Range+5)
        self.driver.lcd_byte(0x80,1)
	self.setAddress(Start_Range+6)
        self.driver.lcd_byte(0x7E,1)

#------------- For Displaying Y_3 on GLCD ----------------
def Display_Y_3(Page_No, Start_Range, End_Range ,self):

        self.setPage(Page_No)
        self.setAddress(Start_Range)
        self.driver.lcd_byte(0x02,1)

        self.setPage(Page_No)
        self.setAddress(Start_Range + 1)
        self.driver.lcd_byte(0x04,1)

        self.setPage(Page_No)
        self.setAddress(Start_Range + 2)
        self.driver.lcd_byte(0x08,1)

        self.setPage(Page_No)
        self.setAddress(Start_Range + 3)
        self.driver.lcd_byte(0xF0,1)

	self.setPage(Page_No+1)
        self.setAddress(Start_Range + 3)
        self.driver.lcd_byte(0x03,1)

        self.setPage(Page_No)
        self.setAddress(Start_Range + 4)
        self.driver.lcd_byte(0x08,1)

        self.setPage(Page_No)
        self.setAddress(Start_Range + 5)
        self.driver.lcd_byte(0x04,1)

	self.setPage(Page_No)
        self.setAddress(Start_Range + 6)
        self.driver.lcd_byte(0x02,1)

#---------------- For Displaying B_3 On GLCD --------------
def Display_B_3(Page_No, Start_Range, End_Range ,self):
        self.setPage(Page_No)
        for i in range(Start_Range,(End_Range)):
                self.setAddress(i)
                self.driver.lcd_byte(0X22,1)

	self.setPage(Page_No+1)
        for i in range(Start_Range,(End_Range)):
                self.setAddress(i)
                self.driver.lcd_byte(0X02,1)

        self.setPage(Page_No)
        self.setAddress(Start_Range)
        self.driver.lcd_byte(0xFE,1)

        self.setPage(Page_No)
        self.setAddress(Start_Range+5)
        self.driver.lcd_byte(0xDC,1)

	self.setPage(Page_No+1)
        self.setAddress(Start_Range)
        self.driver.lcd_byte(0x03,1)

        self.setPage(Page_No+1)
        self.setAddress(Start_Range+5)
        self.driver.lcd_byte(0x01,1)

#---------------- For Displaying D_3 On GLCD --------------
def Display_D_3(Page_No, Start_Range, End_Range ,self):
        self.setPage(Page_No)
        for i in range(Start_Range,(End_Range)):
                self.setAddress(i)
                self.driver.lcd_byte(0X02,1)

	self.setPage(Page_No+1)
        for i in range(Start_Range,(End_Range)):
                self.setAddress(i)
                self.driver.lcd_byte(0X02,1)

        self.setPage(Page_No)
        self.setAddress(Start_Range)
        self.driver.lcd_byte(0xFE,1)

	self.setPage(Page_No+1)
        self.setAddress(Start_Range)
        self.driver.lcd_byte(0x03,1)

        self.setPage(Page_No)
        self.setAddress(Start_Range+5)
        self.driver.lcd_byte(0xFC,1)

	self.setPage(Page_No+1)
        self.setAddress(Start_Range+5)
        self.driver.lcd_byte(0x01,1)

#---------------- For Displaying M_3 on GLCD ---------------
def Display_M_3(Page_No, Start_Range, End_Range ,self):

        self.setPage(Page_No)
        self.setAddress(Start_Range)
        self.driver.lcd_byte(0xFE,1)

        self.setPage(Page_No)
        self.setAddress(Start_Range+7)
        self.driver.lcd_byte(0xFE,1)

        self.setPage( (Page_No + 1) )
        self.setAddress(Start_Range)
        self.driver.lcd_byte(0x03,1)

        self.setPage( (Page_No + 1) )
        self.setAddress(Start_Range+7)
        self.driver.lcd_byte(0x03,1)

        self.setPage(Page_No)
        self.setAddress(Start_Range+1)
        self.driver.lcd_byte(0x04,1)
        self.setAddress(Start_Range+2)
        self.driver.lcd_byte(0x08,1)
        self.setAddress(Start_Range+3)
        self.driver.lcd_byte(0x10,1)

        self.setAddress(Start_Range+6)
        self.driver.lcd_byte(0x04,1)
        self.setAddress(Start_Range+5)
	self.driver.lcd_byte(0x08,1)
        self.setAddress(Start_Range+4)
        self.driver.lcd_byte(0x10,1)

#--------------- For Displaying G_3 on GLCD ----------------
def Display_G_3(Page_No, Start_Range, End_Range ,self):

        self.setPage(Page_No)
        for i in range(Start_Range,End_Range):
                self.setAddress(i)
                self.driver.lcd_byte(0X02,1)

        self.setPage(Page_No+1)
        for i in range(Start_Range,(End_Range)):
                self.setAddress(i)
                self.driver.lcd_byte(0X02,1)

        self.setPage(Page_No+1)
        self.setAddress(Start_Range+7)
        self.driver.lcd_byte(0x03,1)
        self.setAddress(Start_Range)
        self.driver.lcd_byte(0x03,1)

        self.setPage(Page_No)
        for i in range((Start_Range+4),(End_Range)):
                self.setAddress(i)
                self.driver.lcd_byte(0X22,1)

        self.setPage(Page_No)
        self.setAddress(Start_Range+7)
        self.driver.lcd_byte(0xE0,1)

        self.setPage(Page_No)
        self.setAddress(Start_Range)
        self.driver.lcd_byte(0xFE,1)

#---------------- For Displaying W_3 on GLCD ---------------
def Display_W_3(Page_No, Start_Range, End_Range ,self):

        self.setPage(Page_No)
        self.setAddress(Start_Range)
        self.driver.lcd_byte(0xFE,1)

        self.setPage(Page_No)
        self.setAddress(Start_Range+7)
        self.driver.lcd_byte(0xFE,1)

        self.setPage( (Page_No + 1) )
        self.setAddress(Start_Range)
        self.driver.lcd_byte(0x03,1)

        self.setPage( (Page_No + 1) )
        self.setAddress(Start_Range+7)
        self.driver.lcd_byte(0x03,1)

        self.setPage(Page_No+1)
        self.setAddress(Start_Range+1)
	self.driver.lcd_byte(0x01,1)

	self.setAddress(Start_Range+6)
        self.driver.lcd_byte(0x01,1)

        self.setPage(Page_No)
        self.setAddress(Start_Range+2)
        self.driver.lcd_byte(0x80,1)
        self.setAddress(Start_Range+3)
        self.driver.lcd_byte(0x40,1)
        self.setAddress(Start_Range+4)
        self.driver.lcd_byte(0x40,1)
        self.setAddress(Start_Range+5)
        self.driver.lcd_byte(0x80,1)

#---------------- For Displaying N_3 on GLCD ---------------
def Display_N_3(Page_No, Start_Range, End_Range ,self):

        self.setPage(Page_No)
        self.setAddress(Start_Range)
        self.driver.lcd_byte(0xFE,1)

        self.setPage(Page_No)
        self.setAddress(Start_Range+7)
        self.driver.lcd_byte(0xFE,1)

        self.setPage( (Page_No + 1) )
        self.setAddress(Start_Range)
        self.driver.lcd_byte(0x03,1)

        self.setPage( (Page_No + 1) )
        self.setAddress(Start_Range+7)
        self.driver.lcd_byte(0x03,1)

        self.setPage(Page_No)
        self.setAddress(Start_Range+1)
        self.driver.lcd_byte(0x04,1)
        self.setAddress(Start_Range+2)
        self.driver.lcd_byte(0x08,1)
        self.setAddress(Start_Range+3)
        self.driver.lcd_byte(0x10,1)
        self.setAddress(Start_Range+4)
        self.driver.lcd_byte(0x40,1)
	self.setAddress(Start_Range+5)
        self.driver.lcd_byte(0x80,1)

        self.setPage(Page_No+1)
        self.setAddress(Start_Range+6)
        self.driver.lcd_byte(0x01,1)


#------------- Displaying X_3 on GLCD ------------------
def Display_X_3(Page_No, Start_Range, End_Range ,self):

        self.setPage(Page_No)
        self.setAddress(Start_Range+7)
        self.driver.lcd_byte(0x06,1)

        self.setAddress(Start_Range)
        self.driver.lcd_byte(0x06,1)

        self.setPage(Page_No+1)
        self.setAddress(Start_Range)
        self.driver.lcd_byte(0x03,1)

        self.setAddress(Start_Range+7)
        self.driver.lcd_byte(0x03,1)

        self.setPage(Page_No)
        self.setAddress(Start_Range+1)
        self.driver.lcd_byte(0x88,1)
        self.setAddress(Start_Range+2)
        self.driver.lcd_byte(0x50,1)
        self.setAddress(Start_Range+3)
        self.driver.lcd_byte(0x20,1)
        self.setAddress(Start_Range+4)
        self.driver.lcd_byte(0x20,1)
	self.setAddress(Start_Range+5)
        self.driver.lcd_byte(0x50,1)
        self.setAddress(Start_Range+6)
        self.driver.lcd_byte(0x88,1)
#############################################################

################# '0'-'9' Number Libraries ##################
#---------------- Display 0_1 (Zero) On GLCD ---------------
def Display_0_1(Page_No, Start_Range, End_Range ,self):

        self.setPage(Page_No)
        for i in range(Start_Range,End_Range):
                self.setAddress(i)
                self.driver.lcd_byte(0X02,1)

	self.setPage(Page_No+1)
        for i in range(Start_Range,End_Range):
                self.setAddress(i)
                self.driver.lcd_byte(0X02,1)

        self.setPage(Page_No)
        self.setAddress(Start_Range)
        self.driver.lcd_byte(0xFC,1)

        self.setPage(Page_No)
        self.setAddress(Start_Range + 6)
        self.driver.lcd_byte(0xFC,1)

	self.setPage(Page_No+1)
        self.setAddress(Start_Range)
        self.driver.lcd_byte(0x01,1)

        self.setPage(Page_No+1)
        self.setAddress(Start_Range + 6)
        self.driver.lcd_byte(0x01,1)

#---------------- Display 8_1 On GLCD ---------------
def Display_8_1(Page_No, Start_Range, End_Range ,self):

        self.setPage(Page_No)
        for i in range(Start_Range,End_Range):
                self.setAddress(i)
                self.driver.lcd_byte(0X22,1)
	
	self.setPage(Page_No+1)
        for i in range(Start_Range,End_Range):
                self.setAddress(i)
                self.driver.lcd_byte(0X02,1)

        self.setPage(Page_No)
        self.setAddress(Start_Range)
        self.driver.lcd_byte(0xDC,1)

        self.setPage(Page_No)
        self.setAddress(Start_Range + 6)
        self.driver.lcd_byte(0xDC,1)
	
	self.setPage(Page_No+1)
        self.setAddress(Start_Range)
        self.driver.lcd_byte(0x01,1)

        self.setPage(Page_No+1)
        self.setAddress(Start_Range + 6)
        self.driver.lcd_byte(0x01,1)
		
#---------------- Display 1_1 On GLCD ---------------
def Display_1_1(Page_No, Start_Range, End_Range ,self):
        
        self.setPage(Page_No+1)
        for i in range(Start_Range,(End_Range-1)):
                self.setAddress(i)
                self.driver.lcd_byte(0X02,1)

        self.setPage(Page_No)
        self.setAddress(Start_Range+2)
        self.driver.lcd_byte(0xFE,1)

        self.setPage(Page_No)
        self.setAddress(Start_Range+1)
        self.driver.lcd_byte(0x04,1)

	self.setPage(Page_No)
        self.setAddress(Start_Range)
        self.driver.lcd_byte(0x04,1)

	self.setPage(Page_No+1)
        self.setAddress(Start_Range)
        self.driver.lcd_byte(0x02,1)

	self.setPage(Page_No+1)
        self.setAddress(Start_Range+2)
        self.driver.lcd_byte(0x03,1)
       
#---------------- Display 4_1 On GLCD ---------------
def Display_4_1(Page_No, Start_Range, End_Range ,self):

        self.setPage(Page_No)
        self.setAddress(Start_Range+4)
        self.driver.lcd_byte(0xFE,1)
	
	self.setPage(Page_No+1)
        self.setAddress(Start_Range+4)
        self.driver.lcd_byte(0x03,1)

        self.setPage(Page_No)
        self.setAddress(Start_Range+3)
        self.driver.lcd_byte(0x24,1)

        self.setPage(Page_No)
        self.setAddress(Start_Range+2)
        self.driver.lcd_byte(0x28,1)

	self.setPage(Page_No)
        self.setAddress(Start_Range+1)
        self.driver.lcd_byte(0x30,1)

	self.setPage(Page_No)
        self.setAddress(Start_Range+0)
        self.driver.lcd_byte(0x20,1)

	self.setPage(Page_No)
        self.setAddress(Start_Range+5)
        self.driver.lcd_byte(0x20,1)

	self.setPage(Page_No)
        self.setAddress(Start_Range+6)
        self.driver.lcd_byte(0x20,1)

#----------------- For Displaying 5_1 on GLCD ----------------
def Display_5_1(Page_No, Start_Range, End_Range ,self):
        self.setPage(Page_No)
        for i in range(Start_Range,(End_Range)):
                self.setAddress(i)
                self.driver.lcd_byte(0X22,1)

	self.setPage(Page_No+1)
        for i in range(Start_Range+1,(End_Range-1)):
                self.setAddress(i)
                self.driver.lcd_byte(0X02,1)

        self.setPage(Page_No)
        self.setAddress(Start_Range)
        self.driver.lcd_byte(0xBE,1)

        self.setPage(Page_No)
        self.setAddress(Start_Range+5)
        self.driver.lcd_byte(0xC2,1)
	
	self.setPage(Page_No)
        self.setAddress(Start_Range+4)
        self.driver.lcd_byte(0x22,1)

	self.setPage(Page_No+1)
        self.setAddress(Start_Range+3)
        self.driver.lcd_byte(0x02,1)

	self.setPage(Page_No+1)
        self.setAddress(Start_Range+1)
        self.driver.lcd_byte(0x01,1)
	
	self.setPage(Page_No+1)
        self.setAddress(Start_Range+4)
        self.driver.lcd_byte(0x01,1)

#----------------- For Displaying 6_1 on GLCD ----------------
def Display_6_1(Page_No, Start_Range, End_Range ,self):
        self.setPage(Page_No)
        for i in range(Start_Range,(End_Range)):
                self.setAddress(i)
                self.driver.lcd_byte(0X22,1)

	self.setPage(Page_No+1)
        for i in range(Start_Range,(End_Range)):
                self.setAddress(i)
                self.driver.lcd_byte(0X02,1)

        self.setPage(Page_No)
        self.setAddress(Start_Range)
        self.driver.lcd_byte(0xFE,1)

        self.setPage(Page_No)
        self.setAddress(Start_Range+5)
        self.driver.lcd_byte(0xE2,1)

	self.setPage(Page_No+1)
        self.setAddress(Start_Range)
        self.driver.lcd_byte(0x03,1)

        self.setPage(Page_No+1)
        self.setAddress(Start_Range+5)
        self.driver.lcd_byte(0x03,1)

#----------------- For Displaying 7_1 on GLCD ----------------
def Display_7_1(Page_No, Start_Range, End_Range ,self):
        self.setPage(Page_No)
        for i in range(Start_Range,(End_Range)):
                self.setAddress(i)
                self.driver.lcd_byte(0X02,1)

	self.setAddress(Start_Range+5)
        self.driver.lcd_byte(0x06,1)

	self.setAddress(Start_Range+4)
        self.driver.lcd_byte(0x0A,1)
	
	self.setAddress(Start_Range+3)
        self.driver.lcd_byte(0x12,1)

	self.setAddress(Start_Range+2)
        self.driver.lcd_byte(0xE2,1)

	self.setPage(Page_No+1)
	self.setAddress(Start_Range+2)
        self.driver.lcd_byte(0x03,1)

#----------------- For Displaying 9_1 on GLCD ----------------
def Display_9_1(Page_No, Start_Range, End_Range ,self):
        self.setPage(Page_No)
        for i in range(Start_Range,(End_Range)):
                self.setAddress(i)
                self.driver.lcd_byte(0X22,1)

	self.setPage(Page_No+1)
        for i in range(Start_Range,(End_Range)):
                self.setAddress(i)
                self.driver.lcd_byte(0X02,1)


        self.setPage(Page_No)
        self.setAddress(Start_Range)
        self.driver.lcd_byte(0x3E,1)

        self.setPage(Page_No)
        self.setAddress(Start_Range+5)
        self.driver.lcd_byte(0xFE,1)

	self.setPage(Page_No+1)
        self.setAddress(Start_Range+5)
        self.driver.lcd_byte(0x03,1)

        
#----------------- For Displaying 2_1 on GLCD ----------------
def Display_2_1(Page_No, Start_Range, End_Range ,self):
        self.setPage(Page_No)
        for i in range(Start_Range,(End_Range)):
                self.setAddress(i)
                self.driver.lcd_byte(0X22,1)

	self.setPage(Page_No+1)
        for i in range(Start_Range,(End_Range)):
                self.setAddress(i)
                self.driver.lcd_byte(0X02,1)


        self.setPage(Page_No)
        self.setAddress(Start_Range)
        self.driver.lcd_byte(0xE2,1)

        self.setPage(Page_No)
        self.setAddress(Start_Range+5)
        self.driver.lcd_byte(0x3E,1)

	self.setPage(Page_No+1)
        self.setAddress(Start_Range)
        self.driver.lcd_byte(0x03,1)


#----------------- For Displaying 3_1 on GLCD ----------------
def Display_3_1(Page_No, Start_Range, End_Range ,self):
        self.setPage(Page_No)
        for i in range(Start_Range,(End_Range)):
                self.setAddress(i)
                self.driver.lcd_byte(0X22,1)

	self.setPage(Page_No+1)
        for i in range(Start_Range,(End_Range)):
                self.setAddress(i)
                self.driver.lcd_byte(0X02,1)

        self.setPage(Page_No)
        self.setAddress(Start_Range+5)
        self.driver.lcd_byte(0xFE,1)

	self.setPage(Page_No+1)
        self.setAddress(Start_Range+5)
        self.driver.lcd_byte(0x03,1)

#----------------- For Displaying b_1 on GLCD ----------------
def Display_b_1(Page_No, Start_Range, End_Range ,self):
        self.setPage(Page_No)
        for i in range(Start_Range,(End_Range)):
                self.setAddress(i)
                self.driver.lcd_byte(0X90,1)

        self.setPage(Page_No)
        self.setAddress(Start_Range)
        self.driver.lcd_byte(0xFE,1)

        self.setPage(Page_No)
        self.setAddress(Start_Range+5)
        self.driver.lcd_byte(0xF0,1)
#############################################################

################ Non CAPS Characters Libraries ##############
#----------------- For Displaying h_1 on GLCD ----------------
def Display_h_1(Page_No, Start_Range, End_Range ,self):
        self.setPage(Page_No)
        for i in range(Start_Range,(End_Range)):
                self.setAddress(i)
                self.driver.lcd_byte(0X10,1)

        self.setPage(Page_No)
        self.setAddress(Start_Range)
        self.driver.lcd_byte(0xFE,1)

        self.setPage(Page_No)
        self.setAddress(Start_Range+5)
        self.driver.lcd_byte(0xF0,1)

#----------------- For Displaying w_1 on GLCD ----------------
def Display_w_1(Page_No, Start_Range, End_Range ,self):

        self.setPage(Page_No)
        self.setAddress(Start_Range)
        self.driver.lcd_byte(0xF8,1)

	self.setAddress(Start_Range+1)
        self.driver.lcd_byte(0x40,1)

	self.setAddress(Start_Range+2)
        self.driver.lcd_byte(0x20,1)

	self.setAddress(Start_Range+3)
        self.driver.lcd_byte(0x10,1)

	self.setAddress(Start_Range+4)
        self.driver.lcd_byte(0x20,1)

	self.setAddress(Start_Range+5)
        self.driver.lcd_byte(0x40,1)

        self.setPage(Page_No)
        self.setAddress(Start_Range+6)
        self.driver.lcd_byte(0xF8,1)

#--------------For Displying t_1 on GLCD-------------------
def Display_t_1(Page_No, Start_Range, End_Range ,self):

        self.setPage(Page_No)
        for i in range(Start_Range+1,End_Range):
                self.setAddress(i)
                self.driver.lcd_byte(0X90,1)
	
	self.setPage(Page_No)
        self.setAddress(Start_Range)
        self.driver.lcd_byte(0x10,1)

        self.setPage(Page_No)
        self.setAddress(Start_Range + 1)
        self.driver.lcd_byte(0xFE,1)

#--------------For Displying f_1 on GLCD-------------------
def Display_f_1(Page_No, Start_Range, End_Range ,self):

        self.setPage(Page_No)
        for i in range(Start_Range+3,End_Range):
                self.setAddress(i)
                self.driver.lcd_byte(0X12,1)

	for i in range(Start_Range,(End_Range - 3)):
                self.setAddress(i)
                self.driver.lcd_byte(0X10,1)

        self.setPage(Page_No)
        self.setAddress(Start_Range + 2)
        self.driver.lcd_byte(0xFE,1)

#--------------For Displying e_1 on GLCD-------------------
def Display_e_1(Page_No, Start_Range, End_Range ,self):

        self.setPage(Page_No)
        for i in range(Start_Range,(End_Range)):
                self.setAddress(i)
                self.driver.lcd_byte(0XA8,1)

        self.setPage(Page_No)
        self.setAddress(Start_Range)
        self.driver.lcd_byte(0xF8,1)

	self.setAddress(Start_Range+5)
        self.driver.lcd_byte(0x38,1)

#--------------For Displying s_1 on GLCD-------------------
def Display_s_1(Page_No, Start_Range, End_Range ,self):

        self.setPage(Page_No)
        for i in range(Start_Range,(End_Range)):
                self.setAddress(i)
                self.driver.lcd_byte(0XA8,1)

        self.setPage(Page_No)
        self.setAddress(Start_Range)
        self.driver.lcd_byte(0xB8,1)

        self.setAddress(Start_Range+5)
        self.driver.lcd_byte(0xE8,1)

#--------------For Displying z_1 on GLCD-------------------
def Display_z_1(Page_No, Start_Range, End_Range ,self):

        self.setPage(Page_No)
        for i in range(Start_Range,(End_Range)):
                self.setAddress(i)
                self.driver.lcd_byte(0X88,1)

        self.setPage(Page_No)
        self.setAddress(Start_Range+1)
        self.driver.lcd_byte(0xC8,1)

	self.setAddress(Start_Range+2)
        self.driver.lcd_byte(0xA8,1)

	self.setAddress(Start_Range+3)
        self.driver.lcd_byte(0xA8,1)

	self.setAddress(Start_Range+4)
        self.driver.lcd_byte(0x98,1)

#--------------For Displying x_1 on GLCD-------------------
def Display_x_1(Page_No, Start_Range, End_Range ,self):

	self.setPage(Page_No)
        self.setAddress(Start_Range)
        self.driver.lcd_byte(0x88,1)
	
        self.setPage(Page_No)
        self.setAddress(Start_Range+1)
        self.driver.lcd_byte(0x50,1)

        self.setAddress(Start_Range+2)
        self.driver.lcd_byte(0x20,1)

        self.setAddress(Start_Range+3)
        self.driver.lcd_byte(0x20,1)

	self.setAddress(Start_Range+4)
        self.driver.lcd_byte(0x50,1)

        self.setAddress(Start_Range+5)
        self.driver.lcd_byte(0x88,1)

#----------------- For Displaying d_1 on GLCD ----------------
def Display_d_1(Page_No, Start_Range, End_Range ,self):
        self.setPage(Page_No)
        for i in range(Start_Range,(End_Range)):
                self.setAddress(i)
                self.driver.lcd_byte(0X90,1)

        self.setPage(Page_No)
        self.setAddress(Start_Range)
        self.driver.lcd_byte(0xF0,1)
        self.setAddress(Start_Range+5)
        self.driver.lcd_byte(0xFE,1)

#--------------For Displying c_1 on GLCD-------------------
def Display_c_1(Page_No, Start_Range, End_Range ,self):

        self.setPage(Page_No)
        for i in range(Start_Range,(End_Range)):
                self.setAddress(i)
                self.driver.lcd_byte(0X88,1)

        self.setPage(Page_No)
        self.setAddress(Start_Range)
        self.driver.lcd_byte(0xF8,1)

        self.setAddress(Start_Range+5)
        self.driver.lcd_byte(0x88,1)


#--------------For Displying o_1(small o) on GLCD-------------------
def Display_o_1(Page_No, Start_Range, End_Range ,self):

        self.setPage(Page_No)
        for i in range(Start_Range,(End_Range)):
                self.setAddress(i)
                self.driver.lcd_byte(0X88,1)

        self.setPage(Page_No)
        self.setAddress(Start_Range)
        self.driver.lcd_byte(0xF8,1)

        self.setAddress(Start_Range+5)
        self.driver.lcd_byte(0xF8,1)

#--------------For Displying p_1 on GLCD-------------------
def Display_p_1(Page_No, Start_Range, End_Range ,self):

        self.setPage(Page_No)
        for i in range(Start_Range,(End_Range)):
                self.setAddress(i)
                self.driver.lcd_byte(0X14,1)

        self.setPage(Page_No)
        self.setAddress(Start_Range)
        self.driver.lcd_byte(0xFC,1)

        self.setAddress(Start_Range+5)
        self.driver.lcd_byte(0x1C,1)

#--------------For Displying l_1 on GLCD-------------------
def Display_l_1(Page_No, Start_Range, End_Range ,self):

        self.setPage(Page_No)
        self.setAddress(Start_Range)
        self.driver.lcd_byte(0x02,1)

        self.setPage(Page_No)
        self.setAddress(Start_Range + 1)
        self.driver.lcd_byte(0xFE,1)
	
	self.setPage(Page_No)
        self.setAddress(Start_Range + 2)
        self.driver.lcd_byte(0x80,1)

#--------------For Displying k_1 on GLCD-------------------
def Display_k_1(Page_No, Start_Range, End_Range ,self):

        self.setPage(Page_No)
        self.setAddress(Start_Range)
        self.driver.lcd_byte(0xFE,1)

        self.setPage(Page_No)
        self.setAddress(Start_Range + 1)
        self.driver.lcd_byte(0x20,1)

	self.setPage(Page_No)
        self.setAddress(Start_Range + 2)
        self.driver.lcd_byte(0x50,1)

	self.setPage(Page_No)
        self.setAddress(Start_Range + 3)
        self.driver.lcd_byte(0x88,1)

#--------------For Displying v_1 on GLCD-------------------
def Display_v_1(Page_No, Start_Range, End_Range ,self):

        self.setPage(Page_No)
        self.setAddress(Start_Range)
        self.driver.lcd_byte(0x18,1)

        self.setPage(Page_No)
        self.setAddress(Start_Range + 1)
        self.driver.lcd_byte(0x20,1)

        self.setPage(Page_No)
        self.setAddress(Start_Range + 2)
        self.driver.lcd_byte(0x40,1)

        self.setPage(Page_No)
        self.setAddress(Start_Range + 3)
        self.driver.lcd_byte(0x80,1)

	self.setPage(Page_No)
        self.setAddress(Start_Range + 4)
        self.driver.lcd_byte(0x40,1)

	self.setPage(Page_No)
        self.setAddress(Start_Range + 5)
        self.driver.lcd_byte(0x20,1)

	self.setPage(Page_No)
        self.setAddress(Start_Range + 6)
        self.driver.lcd_byte(0x18,1)

#--------------For Displying y_1 on GLCD-------------------
def Display_y_1(Page_No, Start_Range, End_Range ,self):

        self.setPage(Page_No)
        self.setAddress(Start_Range)
        self.driver.lcd_byte(0x04,1)

        self.setPage(Page_No)
        self.setAddress(Start_Range + 1)
        self.driver.lcd_byte(0x08,1)

        self.setPage(Page_No)
        self.setAddress(Start_Range + 2)
        self.driver.lcd_byte(0x10,1)

        self.setPage(Page_No)
        self.setAddress(Start_Range + 3)
        self.driver.lcd_byte(0x20,1)

        self.setPage(Page_No)
        self.setAddress(Start_Range + 4)
        self.driver.lcd_byte(0xFC,1)

#--------------For Displying u_1 on GLCD-------------------
def Display_u_1(Page_No, Start_Range, End_Range ,self):

        self.setPage(Page_No)
        self.setAddress(Start_Range)
        self.driver.lcd_byte(0x18,1)

        self.setPage(Page_No)
        self.setAddress(Start_Range + 1)
        self.driver.lcd_byte(0x20,1)

        self.setPage(Page_No)
        self.setAddress(Start_Range + 2)
        self.driver.lcd_byte(0x40,1)

        self.setPage(Page_No)
        self.setAddress(Start_Range + 3)
        self.driver.lcd_byte(0x80,1)

        self.setPage(Page_No)
        self.setAddress(Start_Range + 4)
        self.driver.lcd_byte(0x80,1)

        self.setPage(Page_No)
        self.setAddress(Start_Range + 5)
	self.driver.lcd_byte(0x40,1)

        self.setPage(Page_No)
        self.setAddress(Start_Range + 6)
        self.driver.lcd_byte(0x20,1)

	self.setPage(Page_No)
        self.setAddress(Start_Range + 7)
        self.driver.lcd_byte(0xF8,1)

#--------------For Displying m_1 on GLCD-------------------
def Display_m_1(Page_No, Start_Range, End_Range ,self):

        self.setPage(Page_No)
        self.setAddress(Start_Range)
        self.driver.lcd_byte(0xEC,1)

        self.setPage(Page_No)
        self.setAddress(Start_Range + 1)
        self.driver.lcd_byte(0x10,1)

        self.setPage(Page_No)
        self.setAddress(Start_Range + 2)
        self.driver.lcd_byte(0x10,1)

        self.setPage(Page_No)
        self.setAddress(Start_Range + 3)
        self.driver.lcd_byte(0xE0,1)

        self.setPage(Page_No)
        self.setAddress(Start_Range + 4)
        self.driver.lcd_byte(0x10,1)

        self.setPage(Page_No)
        self.setAddress(Start_Range + 5)
        self.driver.lcd_byte(0x10,1)

        self.setPage(Page_No)
        self.setAddress(Start_Range + 6)
        self.driver.lcd_byte(0xE0,1)

#--------------For Displying n_1 on GLCD-------------------
def Display_n_1(Page_No, Start_Range, End_Range ,self):

        self.setPage(Page_No)
        self.setAddress(Start_Range + 1)
        self.driver.lcd_byte(0x04,1)

        self.setPage(Page_No)
        self.setAddress(Start_Range + 2)
        self.driver.lcd_byte(0xFC,1)

        self.setPage(Page_No)
        self.setAddress(Start_Range + 3)
        self.driver.lcd_byte(0x10,1)

        self.setPage(Page_No)
        self.setAddress(Start_Range + 4)
        self.driver.lcd_byte(0x10,1)

        self.setPage(Page_No)
        self.setAddress(Start_Range + 5)
        self.driver.lcd_byte(0x10,1)

        self.setPage(Page_No)
        self.setAddress(Start_Range + 6)
        self.driver.lcd_byte(0xE0,1)

#--------------For Displying r_1 on GLCD-------------------
def Display_r_1(Page_No, Start_Range, End_Range ,self):

        self.setPage(Page_No)
        self.setAddress(Start_Range)
        self.driver.lcd_byte(0x04,1)

        self.setPage(Page_No)
        self.setAddress(Start_Range + 1)
        self.driver.lcd_byte(0x08,1)

        self.setPage(Page_No)
        self.setAddress(Start_Range + 2)
        self.driver.lcd_byte(0x50,1)

        self.setPage(Page_No)
        self.setAddress(Start_Range + 3)
        self.driver.lcd_byte(0xA0,1)

        self.setPage(Page_No)
        self.setAddress(Start_Range + 4)
        self.driver.lcd_byte(0x50,1)

        self.setPage(Page_No)
        self.setAddress(Start_Range + 5)
        self.driver.lcd_byte(0x08,1)

        self.setPage(Page_No)
        self.setAddress(Start_Range + 6)
        self.driver.lcd_byte(0x04,1)

#--------------For Displying i_1 on GLCD-------------------
def Display_i_1(Page_No, Start_Range, End_Range ,self):

        self.setPage(Page_No)
        self.setAddress(Start_Range + 1)
        self.driver.lcd_byte(0xF4,1)

#--------------For Displying j_1 on GLCD-------------------
def Display_j_1(Page_No, Start_Range, End_Range ,self):

	self.setPage(Page_No)
	for i in range(Start_Range,(Start_Range+3)):
		 self.setAddress(i)
                 self.driver.lcd_byte(0x80,1)

        self.setPage(Page_No)
	self.setAddress(Start_Range)
        self.driver.lcd_byte(0xC0,1)
	
        self.setAddress(Start_Range + 2)
        self.driver.lcd_byte(0xFA,1)

#----------------- For Displaying g_1 on GLCD ----------------
def Display_g_1(Page_No, Start_Range, End_Range ,self):

	self.setPage(Page_No)
        for i in range(Start_Range,(End_Range)):
                self.setAddress(i)
                self.driver.lcd_byte(0XA8,1)

        self.setPage(Page_No)
        self.setAddress(Start_Range)
        self.driver.lcd_byte(0x10,1)

        self.setAddress(Start_Range+5)
        self.driver.lcd_byte(0xF0,1)

#--------------For Displying a_1 on GLCD-------------------
def Display_a_1(Page_No, Start_Range, End_Range ,self):

        self.setPage(Page_No)
        for i in range(Start_Range,(End_Range-1)):
                self.setAddress(i)
                self.driver.lcd_byte(0X22,1)

        self.setPage(Page_No)
        self.setAddress(Start_Range)
        self.driver.lcd_byte(0x1C,1)

        self.setAddress(Start_Range+4)
        self.driver.lcd_byte(0xFC,1)

	self.setAddress(Start_Range+5)
        self.driver.lcd_byte(0x80,1)

	self.setAddress(Start_Range+6)
        self.driver.lcd_byte(0x80,1)

#--------------For Displying q_1 on GLCD-------------------
def Display_q_1(Page_No, Start_Range, End_Range ,self):

        self.setPage(Page_No)
        for i in range(Start_Range,(End_Range-1)):
                self.setAddress(i)
                self.driver.lcd_byte(0X22,1)

        self.setPage(Page_No)
        self.setAddress(Start_Range)
        self.driver.lcd_byte(0x1C,1)

        self.setAddress(Start_Range+4)
        self.driver.lcd_byte(0xFC,1)

	self.setAddress(Start_Range+5)
        self.driver.lcd_byte(0x40,1)

	self.setAddress(Start_Range+6)
        self.driver.lcd_byte(0x20,1)
#############################################################

################## Unique Serial Device ID ##################
def getserial():
  # Extract serial from cpuinfo file
  cpuserial = "0000000000000000"
  try:
    f = open('/proc/cpuinfo','r')
    for line in f:
      if line[0:6]=='Serial':
        cpuserial = line[10:26]
    f.close()
  except:
    cpuserial = " ----- ERROR IN GETTING UNIQUE DEVICE ID ----- "

  return cpuserial
#############################################################

######################## Infinite Loop ######################
def demo():
#----------- Global Variables Declarations ----------
	global Flag_0to54
        global Flag_55
        global Flag_56
        global Flag_57
        global Flag_58
        global Flag_59
	global Flag_0to54_Match
        global Flag_55_Match
        global Flag_56_Match
        global Flag_57_Match
        global Flag_58_Match
        global Flag_59_Match
	global Flag_LCD_Backlight
	global minute_1
	global minute_2
	global clear_flag
	global OK_Button_Data_Backup_Flag
	global reset_button
#-------------- Flags for NURSING submenu -----------
	global NURSING_Submenu_Flag 
	global NURSING_LEFT_Submenu_Flag
	global NURSING_LEFT_Submenu_Flag 
	global NURSING_RIGHT_Submenu_Flag
	global NURSING_RIGHT_Submenu_Flag 
	global Back_Nursing_Left_Flag
	global Back_Nursing_Right_Flag 
#-------------- Flags for FEED submenu --------------
	global FEED_Submenu_Flag 
	global SOLID_Submenu_NEXT_Flag 
	global FORMULA_Submenu_NEXT_Flag
	global BREAST_MILK_Submenu_NEXT_Flag 
	global BACK_FEED_Option_Flag 
	global BACK_SOLID_Option_Flag_For_Next 
	global BACK_FORMULA_Option_Flag_For_Next 
	global BACK_BREAST_MILK_Option_Flag_For_Next 
#--------------- Flages For PUMPING submenu ---------
	global PUMPING_Submenu_Flag 
	global PUMPING_LEFT_Submenu_Flag 
	global PUMPING_LEFT_START_Submenu_Flag 
	global PUMPING_LEFT_END_Submenu_Flag 
	global PUMPING_RIGHT_Submenu_Flag 
	global PUMPING_RIGHT_START_Submenu_Flag 
	global PUMPING_RIGHT_END_Submenu_Flag
	global PUMPING_LEFT_END_OK_Flag
	global PUMPING_RIGHT_END_OK_Flag  
 ##-------------- LEFT ---------------------
	global Back_Pumping_Left_Flag 
	global Back_Pumping_Left_Start_Flag
	global Back_Pumping_Left_Start_OZ_Flag 
	global Back_Pumping_Left_End_Flag
	global Back_Pumping_Left_End_OZ_Flag
 ##--------------RIGHT----------------------
	global Back_Pumping_Right_Flag 
	global Back_Pumping_Right_Start_Flag 
	global Back_Pumping_Right_Start_OZ_Flag
	global Back_Pumping_Right_End_Flag 
	global Back_Pumping_Right_End_OZ_Flag
#--------------- Flages For DIAPER submenu ---------
	global DIAPER_Submenu_Flag
#--------------- Flages For BATH submenu -----------
	global BATH_Submenu_Flag 
#--------------- Flages For SLEEP submenu ----------
	global SLEEP_Submenu_Flag 
#--------------- Flages For MEDICINE submenu -------
	global MEDICINE_Submenu_Flag
#---------------- Button Variables -----------------
	global button1 
	global button2 
	global button3 
	global button4 
	global button5 
	global button6 
	global button7 
	global button8 
#---------------------------------------------------

        driver = LCD_GPIO(RS=4,RW=7,E=8,D0=9,D1=10,D2=11,D3=19,D4=26,D5=17,D6=18,D7=25,CS1=22,CS2=23,RST=24)
        port=serial.Serial('/dev/ttyAMA0',baudrate=38400,timeout=0.1)
	GPIO.setup(Longpress_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        lcd = LCD12864(driver=driver)
        lcd.lcd_cls()
	lcd.main_menu()
	while True:
		pins = bus.read_byte(PCF8574)
		          
#----------------------------Backlight ON/OFF-------------------------------------
#		GPIO.output(LCD_Backlight,True)
#                time.sleep(0.5)
#                GPIO.output(LCD_Backlight,False)
#                time.sleep(0.5)

#----------------------------Bluetooth Communication------------------------------
#		print "%02x" % pins
                port.write("Hello\r\n") 	# Text To Be Send Over Bluetooth
                time.sleep(0.1)
                rcv=port.read(100)
		time.sleep(0.1)
		print(rcv)

#----------------------------------------LongPress--------------------------------
#                GPIO.setup(Longpress_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
				
#-------------------------------Detect Button Press-------------------------------      
		pins = bus.read_byte(PCF8574)

		now = datetime.datetime.now()
#		global minute_1
		minute_1 = int(now.minute)
		
	        if (pins & 0x08) == 0:
		        print " ----- In Button 1 ----- "
			now = datetime.datetime.now()
#			global minute_1
			minute_1 = int(now.minute)
#			global Flag_0to54_Match
                        Flag_0to54_Match = 1
#                        global Flag_55_Match
                        Flag_55_Match = 1
#                        global Flag_56_Match
                        Flag_56_Match = 1
#                        global Flag_57_Match
                        Flag_57_Match = 1
#                        global Flag_58_Match
                        Flag_58_Match = 1
#                        global Flag_59_Match
                        Flag_59_Match = 1

#			global button1
	                button1 = 1
#        	        global clear_flag
                	clear_flag = 1
	                clear_for_button1()
			lcd.lcd_cls()
			global button1_counter
			button1_counter += 1
#			global Flag_LCD_Backlight
			Flag_LCD_Backlight = 1

	        if (pins & 0x04) == 0:
		        print " ----- In Button 2 ----- "
			now = datetime.datetime.now()
#			global minute_1
			minute_1 = int(now.minute)
#			global Flag_0to54_Match
                        Flag_0to54_Match = 1
#                        global Flag_55_Match
                        Flag_55_Match = 1
#                        global Flag_56_Match
                        Flag_56_Match = 1
#                        global Flag_57_Match
                        Flag_57_Match = 1
#                        global Flag_58_Match
                        Flag_58_Match = 1
#                        global Flag_59_Match
                        Flag_59_Match = 1

#                        global button2
                        button2 = 1
#                        global clear_flag
                        clear_flag = 1
                        clear_for_button2()
#			global Flag_LCD_Backlight
			Flag_LCD_Backlight = 1

	        if (pins & 0x02) == 0:
		        print " ----- In Button 3 ----- "
			now = datetime.datetime.now()
#			global minute_1
			minute_1 = int(now.minute)
#			global Flag_0to54_Match
                        Flag_0to54_Match = 1
#                        global Flag_55_Match
                        Flag_55_Match = 1
#                        global Flag_56_Match
                        Flag_56_Match = 1
#                        global Flag_57_Match
                        Flag_57_Match = 1
#                        global Flag_58_Match
                        Flag_58_Match = 1
#                        global Flag_59_Match
                        Flag_59_Match = 1

#                        global button3
                        button3 = 1
#                        global clear_flag
                        clear_flag = 1
                        clear_for_button3()
#			global Flag_LCD_Backlight
			Flag_LCD_Backlight = 1

	        if (pins & 0x01) == 0:
		        print " ----- In Button 4 ----- "
			now = datetime.datetime.now()
#			global minute_1
			minute_1 = int(now.minute)
#			global Flag_0to54_Match
                        Flag_0to54_Match = 1
#                        global Flag_55_Match
                        Flag_55_Match = 1
#                        global Flag_56_Match
                        Flag_56_Match = 1
#                        global Flag_57_Match
                        Flag_57_Match = 1
#                        global Flag_58_Match
                        Flag_58_Match = 1
#                        global Flag_59_Match
                        Flag_59_Match = 1

#			global button4
                        button4 = 1
#                        global clear_flag
                        clear_flag = 1
                        clear_for_button4()
#			global Flag_LCD_Backlight
			Flag_LCD_Backlight = 1

	        if (pins & 0x10) == 0:
		        print " ----- In Button 5 ----- "
			now = datetime.datetime.now()
#			global minute_1
			minute_1 = int(now.minute)
#			global Flag_0to54_Match
                        Flag_0to54_Match = 1
#                        global Flag_55_Match
                        Flag_55_Match = 1
#                        global Flag_56_Match
                        Flag_56_Match = 1
#                        global Flag_57_Match
                        Flag_57_Match = 1
#                        global Flag_58_Match
                        Flag_58_Match = 1
#                        global Flag_59_Match
                        Flag_59_Match = 1

#			global button5
                        button5 = 1
#                        global clear_flag
                        clear_flag = 1
                        clear_for_button5()
#			global Flag_LCD_Backlight
			Flag_LCD_Backlight = 1

	        if (pins & 0x20) == 0:
		        print " ----- In Button 6 ----- "
			now = datetime.datetime.now()
#			global minute_1
			minute_1 = int(now.minute)
#			global Flag_0to54_Match
                        Flag_0to54_Match = 1
#                        global Flag_55_Match
                        Flag_55_Match = 1
#                        global Flag_56_Match
                        Flag_56_Match = 1
#                        global Flag_57_Match
                        Flag_57_Match = 1
#                        global Flag_58_Match
                        Flag_58_Match = 1
#                        global Flag_59_Match
                        Flag_59_Match = 1

#			global button6
                        button6 = 1
#                        global clear_flag
                        clear_flag = 1
                        clear_for_button6()
#			global Flag_LCD_Backlight
			Flag_LCD_Backlight = 1
	
	        if (pins & 0x40) == 0:
		        print " ----- In Button 7 ----- "
			now = datetime.datetime.now()
#			global minute_1
			minute_1 = int(now.minute)
#			global Flag_0to54_Match
                        Flag_0to54_Match = 1
#                        global Flag_55_Match
                        Flag_55_Match = 1
#                        global Flag_56_Match
                        Flag_56_Match = 1
#                        global Flag_57_Match
                        Flag_57_Match = 1
#                        global Flag_58_Match
                        Flag_58_Match = 1
#                        global Flag_59_Match
                        Flag_59_Match = 1

# 			global button7
                        button7 = 1
#                        global clear_flag
                        clear_flag = 1
                        clear_for_button7()
#			global Flag_LCD_Backlight
			Flag_LCD_Backlight = 1

	        if (pins & 0x80) == 0:
		        print " ----- In Button 8 ----- "
			now = datetime.datetime.now()
#			global minute_1
			minute_1 = int(now.minute)
#			global Flag_0to54_Match
                        Flag_0to54_Match = 1
#                        global Flag_55_Match
                        Flag_55_Match = 1
#                        global Flag_56_Match
                        Flag_56_Match = 1
#                        global Flag_57_Match
                        Flag_57_Match = 1
#                        global Flag_58_Match
                        Flag_58_Match = 1
#                        global Flag_59_Match
                        Flag_59_Match = 1

#			global button8
                        button8 = 1
#                        global clear_flag
                        clear_flag = 1
                        clear_for_button8()
#			global Flag_LCD_Backlight
			Flag_LCD_Backlight = 1

#--------------------------- Button Functions --------------------------------------
		if button1:
			if (clear_flag and DIAPER_Submenu_Flag != 1):
                                lcd.lcd_cls()
#				print(" ----- In Button 1 Defination ----- ")
#                                global clear_flag
                                clear_flag = 0
			if (NURSING_Submenu_Flag == 1):
#				global NURSING_LEFT_Submenu_Flag
                                NURSING_LEFT_Submenu_Flag = 1
#				global NURSING_RIGHT_Submenu_Flag
                                NURSING_RIGHT_Submenu_Flag = 0

		#---------------- FOR NURSING MENU and SUBMENU --------------
			if (NURSING_Submenu_Flag != 1 and PUMPING_Submenu_Flag != 1  and FEED_Submenu_Flag != 1 and DIAPER_Submenu_Flag != 1 and BATH_Submenu_Flag != 1 and SLEEP_Submenu_Flag != 1):
#				lcd.PUMPING_LEFT_START_SUB_MENU()
				lcd.NURSING_SUB_MENU()
#				global button1
				button1 = 0

			elif (NURSING_LEFT_Submenu_Flag == 1 and NURSING_RIGHT_Submenu_Flag != 1 and PUMPING_LEFT_Submenu_Flag != 1 and PUMPING_LEFT_START_Submenu_Flag != 1 and PUMPING_RIGHT_START_Submenu_Flag != 1 and FEED_Submenu_Flag != 1 and DIAPER_Submenu_Flag != 1 and BATH_Submenu_Flag !=1 and SLEEP_Submenu_Flag != 1):
				lcd.NURSING_LEFT_SUB_MENU()
#				global Back_Nursing_Left_Start_Flag
#                                Back_Nuring_Left_Start_Flag = 1
#				global Back_Nursing_Left_Flag
				Back_Nursing_Left_Flag = 1
				
		#---------------- FOR PUMPING MENU and SUBMENU ----------------
			if PUMPING_LEFT_START_Submenu_Flag == 1:
#				print 'i am here in pumping'
				lcd.PUMPING_LEFT_START_SUB_MENU()
#				global Back_Pumping_Left_Start_OZ_Flag
				Back_Pumping_Left_Start_OZ_Flag = 1
			elif PUMPING_RIGHT_START_Submenu_Flag == 1:
                                lcd.PUMPING_RIGHT_START_SUB_MENU()
#				global Back_Pumping_Right_Start_OZ_Flag
                                Back_Pumping_Right_Start_OZ_Flag = 1
			elif (PUMPING_Submenu_Flag == 1):
                                lcd.PUMPING_LEFT_SUB_MENU()
#                                global PUMPING_LEFT_START_Submenu_Flag
                                PUMPING_LEFT_START_Submenu_Flag = 1
#                                global PUMPING_LEFT_END_Submenu_Flag
                                PUMPING_LEFT_END_Submenu_Flag = 1
#                                global Back_Pumping_Left_Start_Flag
                                Back_Pumping_Left_Start_Flag = 1
#                                global button1
                                button1 = 0
		#---------------- FOR FEED MENU and SUBMENU -----------------
			elif (PUMPING_Submenu_Flag == 0) and (FEED_Submenu_Flag == 1) and (NURSING_Submenu_Flag != 1):
#				print 'I am here'
				lcd.FORMULA_SUB_MENU()
#				global FORMULA_Submenu_NEXT_Flag
                                FORMULA_Submenu_NEXT_Flag = 1
#				global BACK_FEED_Option_Flag
                                BACK_FEED_Option_Flag = 1
#				global SOLID_Submenu_NEXT_Flag
                                SOLID_Submenu_NEXT_Flag = 0
#                                global BREAST_MILK_Submenu_NEXT_Flag
                                BREAT_MILK_Submenu_NEXT_Flag = 0

			if(PUMPING_Submenu_Flag != 1 and FEED_Submenu_Flag != 1 and DIAPER_Submenu_Flag != 1 and BATH_Submenu_Flag != 1 and SLEEP_Submenu_Flag != 1):
#				global NURSING_Submenu_Flag 
				NURSING_Submenu_Flag = 1
				
		elif button2:
			if clear_flag:
				lcd.lcd_cls()
#                                global clear_flag
                                clear_flag = 0
#			print(" ----- In Button 2 Defination ----- ")
			if (NURSING_Submenu_Flag == 1):
#                                global NURSING_RIGHT_Submenu_Flag
                                NURSING_RIGHT_Submenu_Flag = 1
#				global NURSING_LEFT_Submenu_Flag
                                NURSING_LEFT_Submenu_Flag = 0

		 #---------------- FOR NURSING MENU and SUBMENU --------------
			if (NURSING_RIGHT_Submenu_Flag == 1 and NURSING_Submenu_Flag == 1):
				lcd.lcd_cls()
#                                global clear_flag
                                clear_flag = 0
                                lcd.NURSING_RIGHT_SUB_MENU()
#                                global Back_Nursing_Right_Flag
                                Back_Nursing_Right_Flag = 1
#				global Back_Nursing_Left_Flag
                                Back_Nursing_Left_Flag = 0
#				global button2
                                button2 = 0

		 #---------------- FOR PUMPING MENU and SUBMENU --------------

			if (PUMPING_LEFT_END_Submenu_Flag == 1 and NURSING_Submenu_Flag != 1):
                                lcd.PUMPING_LEFT_END_SUB_MENU()
#				global Back_Pumping_Left_End_OZ_Flag
                                Back_Pumping_Left_End_OZ_Flag = 1
#				global PUMPING_LEFT_END_OK_Flag 
				PUMPING_LEFT_END_OK_Flag = 1
#				global PUMPING_RIGHT_END_OK_Flag
                                PUMPING_RIGHT_END_OK_Flag = 0

			elif (PUMPING_RIGHT_END_Submenu_Flag == 1 and NURSING_Submenu_Flag != 1):
                                lcd.PUMPING_RIGHT_END_SUB_MENU()
#				global Back_Pumping_Right_End_OZ_Flag
                                Back_Pumping_Right_End_OZ_Flag = 1
#				global PUMPING_RIGHT_END_OK_Flag
                                PUMPING_RIGHT_END_OK_Flag = 1
#				global PUMPING_LEFT_END_OK_Flag
                                PUMPING_LEFT_END_OK_Flag = 0

			elif (PUMPING_Submenu_Flag == 1 and NURSING_Submenu_Flag != 1):
                                lcd.PUMPING_RIGHT_SUB_MENU()
#				global PUMPING_RIGHT_START_Submenu_Flag
                                PUMPING_RIGHT_START_Submenu_Flag = 1
#                                global PUMPING_RIGHT_END_Submenu_Flag
                                PUMPING_RIGHT_END_Submenu_Flag = 1
				#global Back_Pumping_Left_End_OZ_Flag
                                #Back_Pumping_Left_End_OZ_Flag = 1
#				global Back_Pumping_Right_Start_Flag
                                Back_Pumping_Right_Start_Flag = 1
#				global Back_Pumping_Right_End_Flag
                                Back_Pumping_Right_End_Flag = 1
#				global button2
                                button2 = 0
			#-------------------------- FOR FEED MENU and SUBMENU -----------------------------
			elif (FEED_Submenu_Flag != 1 and NURSING_Submenu_Flag != 1 and DIAPER_Submenu_Flag != 1):
		 
				lcd.FEED_SUB_MENU()
#				global button2
		                button2 = 0
			elif (PUMPING_Submenu_Flag != 1 and NURSING_Submenu_Flag != 1 and DIAPER_Submenu_Flag != 1):
				lcd.BREAST_MILK_SUB_MENU()
#				global BREAST_MILK_Submenu_NEXT_Flag
                                BREAST_MILK_Submenu_NEXT_Flag = 1
#				global BACK_FEED_Option_Flag 
				BACK_FEED_Option_Flag = 1
#				global SOLID_Submenu_NEXT_Flag
                                SOLID_Submenu_NEXT_Flag = 0
#                                global FORMULA_Submenu_NEXT_Flag
                                FORMULA_Submenu_NEXT_Flag = 0

			if(PUMPING_Submenu_Flag != 1 and NURSING_Submenu_Flag != 1 and DIAPER_Submenu_Flag != 1 and BATH_Submenu_Flag != 1 and SLEEP_Submenu_Flag != 1):
#				global FEED_Submenu_Flag
				FEED_Submenu_Flag = 1

		elif button3:
			if ( clear_flag and PUMPING_Submenu_Flag != 1 and SLEEP_Submenu_Flag != 1):
				lcd.lcd_cls()
#				global clear_flag
				clear_flag = 0
#				print(" ----- In Button 3 Defination ----- ")
			if (FEED_Submenu_Flag != 1 and PUMPING_Submenu_Flag != 1 and SLEEP_Submenu_Flag != 1 and NURSING_Submenu_Flag != 1):
				lcd.DIAPER_SUB_MENU()
#				print("IN DIAPER SUBMENU FLAG=1@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
#				global DIAPER_Submenu_Flag
	                        DIAPER_Submenu_Flag = 1

			elif(PUMPING_Submenu_Flag != 1 and SLEEP_Submenu_Flag != 1): # (FORMULA_Submenu_NEXT_Flag != 1):
                        	lcd.SOLIDS_SUB_MENU()
#				global SOLID_Submenu_NEXT_Flag 
                                SOLID_Submenu_NEXT_Flag = 1
#				global BACK_FEED_Option_Flag
                                BACK_FEED_Option_Flag = 1
#                                global FORMULA_Submenu_NEXT_Flag
                                FORMULA_Submenu_NEXT_Flag = 0
#                                global BREAST_MILK_Submenu_NEXT_Flag
                                BREAST_MILK_Submenu_NEXT_Flag = 0

				#global BACK_SOLID_Option_Flag_For_Next
                                #BACK_SOLID_Option_Flag_For_Next = 1
		elif button4:
#			print(" ----- In Button 4 Defination ----- ")
			if ( clear_flag and PUMPING_Submenu_Flag != 1 and FEED_Submenu_Flag != 1 and DIAPER_Submenu_Flag != 1):
				lcd.lcd_cls()
#				global clear_flag
				clear_flag = 0
			elif(PUMPING_Submenu_Flag != 1 and FEED_Submenu_Flag != 1 and DIAPER_Submenu_Flag != 1):
				lcd.SLEEP_SUB_MENU()
#				global SLEEP_Submenu_Flag
                                SLEEP_Submenu_Flag = 1
		elif button5:
#			print(" ----- In Button 5 Defination ----- ")
			if (clear_flag and PUMPING_Submenu_Flag != 1 and FEED_Submenu_Flag != 1 and DIAPER_Submenu_Flag != 1 and BATH_Submenu_Flag != 1 and SLEEP_Submenu_Flag != 1):
				lcd.lcd_cls()
#				global clear_flag
				clear_flag = 0
			if (PUMPING_Submenu_Flag != 1  and FEED_Submenu_Flag != 1 and DIAPER_Submenu_Flag != 1 and BATH_Submenu_Flag != 1 and SLEEP_Submenu_Flag != 1):
                                lcd.PUMPING_SUB_MENU()
#                                global button5
                                button5 = 0
			if(FEED_Submenu_Flag != 1 and DIAPER_Submenu_Flag != 1 and BATH_Submenu_Flag != 1 and SLEEP_Submenu_Flag != 1):
#				global PUMPING_Submenu_Flag
        	                PUMPING_Submenu_Flag = 1
		elif button6:
#			print(" ----- In Button 6 Defination ----- ")
			if ( clear_flag and PUMPING_Submenu_Flag != 1  and FEED_Submenu_Flag != 1 and DIAPER_Submenu_Flag != 1 and SLEEP_Submenu_Flag != 1):
				lcd.lcd_cls()
#				global clear_flag
				clear_flag = 0
			elif(PUMPING_Submenu_Flag != 1 and FEED_Submenu_Flag != 1 and DIAPER_Submenu_Flag != 1 and SLEEP_Submenu_Flag != 1):
				lcd.BATH_SUB_MENU()
#				global BATH_Submenu_Flag
                                BATH_Submenu_Flag = 1
		elif button7:
#			print(" ----- In Button 7 Defination ----- ")
			if ( clear_flag and PUMPING_Submenu_Flag != 1  and FEED_Submenu_Flag != 1 and DIAPER_Submenu_Flag != 1 and BATH_Submenu_Flag != 1 and SLEEP_Submenu_Flag != 1):
				lcd.lcd_cls()
#				global clear_flag
				clear_flag = 0
			elif( PUMPING_Submenu_Flag != 1  and FEED_Submenu_Flag != 1 and DIAPER_Submenu_Flag != 1 and BATH_Submenu_Flag != 1 and SLEEP_Submenu_Flag != 1 and NURSING_Submenu_Flag != 1):
				lcd.Alphabet_for_Font3()
#				global MEDICINE_Submenu_Flag
				MEDICINE_Submenu_Flag = 1
		elif button8:
#			print(" ----- In Button 8 Defination ----- ")
			if ( clear_flag and PUMPING_Submenu_Flag != 1 and DIAPER_Submenu_Flag != 1 and BATH_Submenu_Flag != 1 and SLEEP_Submenu_Flag != 1):
				lcd.lcd_cls()
#				global clear_flag
				clear_flag = 0
			if (FEED_Submenu_Flag == 1):
				if (SOLID_Submenu_NEXT_Flag == 1):
                                	lcd.SOLIDS_SUB_MENU_NEXT()
#					global FORMULA_Submenu_NEXT_Flag
	                                FORMULA_Submenu_NEXT_Flag = 0 
#					global BREAST_MILK_Submenu_NEXT_Flag
                                        BREAST_MILK_Submenu_NEXT_Flag = 0
#					global BACK_SOLID_Option_Flag_For_Next
	                                BACK_SOLID_Option_Flag_For_Next = 1
				elif(FORMULA_Submenu_NEXT_Flag == 1):
					lcd.FORMULA_SUB_MENU_NEXT()
#					global SOLID_Submenu_NEXT_Flag
                                        SOLID_Submenu_NEXT_Flag = 0
#					global BREAST_MILK_Submenu_NEXT_Flag
                                        BREAT_MILK_Submenu_NEXT_Flag = 0
#					global BACK_FORMULA_Option_Flag_For_Next 
					BACK_FORMULA_Option_Flag_For_Next = 1
				elif(BREAST_MILK_Submenu_NEXT_Flag == 1):
                                        lcd.BREAST_MILK_SUB_MENU_NEXT()
#                                        global SOLID_Submenu_NEXT_Flag
                                        SOLID_Submenu_NEXT_Flag = 0
#					global FORMULA_Submenu_NEXT_Flag
                                        FORMULA_Submenu_NEXT_Flag = 0
#					global BACK_BREAST_MILK_Option_Flag_For_Next
                                        BACK_BREAST_MILK_Option_Flag_For_Next = 1
                        elif( PUMPING_Submenu_Flag != 1 and DIAPER_Submenu_Flag != 1 and SLEEP_Submenu_Flag != 1 and BATH_Submenu_Flag != 1):
                                lcd.NUMBERS()
		elif reset_button:
			 print(" ----- In RESET BUTTON Defination ----- ")
#			 global OK_Button_Data_Backup_Flag
			 OK_Button_Data_Backup_Flag = 1

			 now = datetime.datetime.now()
#			 global minute_1
			 minute_1 = int(now.minute)
#            	         global Flag_0to54_Match
                         Flag_0to54_Match = 1
#                         global Flag_55_Match
                         Flag_55_Match = 1
#                         global Flag_56_Match
                         Flag_56_Match = 1
#                         global Flag_57_Match
                         Flag_57_Match = 1
#                         global Flag_58_Match
                         Flag_58_Match = 1
#                         global Flag_59_Match
                         Flag_59_Match = 1

			 if(reset_button):
				print (" ----- In RESET BUTTON DEFINATION SUB-FUNCTION ----- ")
			 	if clear_flag:
                                	lcd.lcd_cls()
#                                	global clear_flag
                                	clear_flag = 0
			 	if (BACK_FEED_Option_Flag == 1 and BACK_SOLID_Option_Flag_For_Next != 1  and BACK_FORMULA_Option_Flag_For_Next != 1 and BACK_BREAST_MILK_Option_Flag_For_Next != 1):
			 	 	lcd.FEED_SUB_MENU()			 	
#				 	global BACK_FEED_Option_Flag 
				 	BACK_FEED_Option_Flag = 0
#				 	global reset_button
	                                reset_button = 0
				elif (BACK_SOLID_Option_Flag_For_Next == 1):
					 lcd.SOLIDS_SUB_MENU()
#					 global BACK_SOLID_Option_Flag_For_Next 
					 BACK_SOLID_Option_Flag_For_Next = 0
#					 global reset_button
					 reset_button = 0
				elif (BACK_FORMULA_Option_Flag_For_Next == 1):
					 lcd.FORMULA_SUB_MENU()
#					 print('i am here in formula reset')
#	                                 global BACK_FORMULA_Option_Flag_For_Next
        	                         BACK_FORMULA_Option_Flag_For_Next = 0
#                	                 global reset_button
                        	         reset_button = 0
				elif (BACK_BREAST_MILK_Option_Flag_For_Next == 1):
        	                         lcd.BREAST_MILK_SUB_MENU()
 #              	                  print('i am here in Breast milk reset')
#                        	         global BACK_BREAST_MILK_Option_Flag_For_Next
                                	 BACK_BREAST_MILK_Option_Flag_For_Next = 0
#	                                 global reset_button
        	                         reset_button = 0
				elif (Back_Pumping_Left_Start_OZ_Flag == 1 or Back_Pumping_Left_End_OZ_Flag == 1 ):
					 lcd.PUMPING_LEFT_SUB_MENU()
#					 global Back_Pumping_Left_Start_OZ_Flag 
					 Back_Pumping_Left_Start_OZ_Flag = 0
#					 global Back_Pumping_Left_End_OZ_Flag
                	                 Back_Pumping_Left_End_OZ_Flag = 0
#					 global PUMPING_LEFT_START_Submenu_Flag
                                	 PUMPING_LEFT_START_Submenu_Flag = 1
#	                                 global PUMPING_LEFT_END_Submenu_Flag
        	                         PUMPING_LEFT_END_Submenu_Flag = 1
#					 global reset_button
                        	         reset_button = 0		
	
				elif (Back_Pumping_Left_Start_Flag == 1 or Back_Pumping_Left_End_Flag == 1 ):
					 lcd.PUMPING_SUB_MENU()
#					 global Back_Pumping_Left_Start_Flag
                                	 Back_Pumping_Left_Start_Flag = 0
#	                                 global Back_Pumping_Left_End_Flag
        	                         Back_Pumping_Left_End_Flag = 0
#                	                 global reset_button
                        	         reset_button = 0
#					 global PUMPING_LEFT_START_Submenu_Flag
	                                 PUMPING_LEFT_START_Submenu_Flag = 0
#        	                         global PUMPING_LEFT_END_Submenu_Flag
                	                 PUMPING_LEFT_END_Submenu_Flag = 0
			 
				elif (Back_Pumping_Right_Start_OZ_Flag == 1 or Back_Pumping_Right_End_OZ_Flag == 1 ):
                                	 lcd.PUMPING_RIGHT_SUB_MENU()
#	                                 global Back_Pumping_Right_Start_OZ_Flag
        	                         Back_Pumping_Right_Start_OZ_Flag = 0
#                	                 global Back_Pumping_Right_End_OZ_Flag
                        	         Back_Pumping_Right_End_OZ_Flag = 0
#					 global PUMPING_RIGHT_START_Submenu_Flag
	                                 PUMPING_RIGHT_START_Submenu_Flag = 1
#        	                         global PUMPING_RIGHT_END_Submenu_Flag
                	                 PUMPING_RIGHT_END_Submenu_Flag = 1
#                        	         global reset_button
        	                         reset_button = 0
	
                	        elif (Back_Pumping_Right_Start_Flag == 1 or Back_Pumping_Right_End_Flag == 1 ):
                        	         lcd.PUMPING_SUB_MENU()
#                                	 global Back_Pumping_Right_Start_Flag
	                                 Back_Pumping_Right_Start_Flag = 0
#        	                         global Back_Pumping_Right_End_Flag
                	                 Back_Pumping_Right_End_Flag = 0
#                        	         global reset_button
	                                 reset_button = 0
#        	                         global PUMPING_RIGHT_START_Submenu_Flag
                	                 PUMPING_RIGHT_START_Submenu_Flag = 0
#                        	         global PUMPING_RIGHT_END_Submenu_Flag
                                	 PUMPING_RIGHT_END_Submenu_Flag = 0
				
				elif (Back_Nursing_Left_Flag == 1):
                                         lcd.NURSING_SUB_MENU()
#                                         global Back_Nursing_Left_Flag
                                         Back_Nursing_Left_Flag = 0
#                                         global reset_button
                                         reset_button = 0
#                                         global NURSING_LEFT_START_Submenu_Flag
                                         NURSIING_LEFT_START_Submenu_Flag = 0
#                                         global NURSING_LEFT_END_Submenu_Flag
                                         NURSING_LEFT_END_Submenu_Flag = 0
				
				elif (Back_Nursing_Right_Flag == 1):
                                         lcd.NURSING_SUB_MENU()
#                                         global Back_Nursing_Right_Flag
                                         Back_Nursing_Right_Flag = 0
#                                         global Back_Nursing_Right_End_Flag
#                                         Back_Nursing_Right_End_Flag = 0
#                                         global reset_button
                                         reset_button = 0
#                                         global NURSING_RIGHT_START_Submenu_Flag
                                         NURSING_RIGHT_START_Submenu_Flag = 0
#                                         global NURSING_RIGHT_END_Submenu_Flag
                                         NURSING_RIGHT_END_Submenu_Flag = 0

	                        else:
					lcd.main_menu()
#					global NURSING_Submenu_Flag
					NURSING_Submenu_Flag = 0
#					global PUMPING_Submenu_Flag
	                	        PUMPING_Submenu_Flag = 0
#					global DIAPER_Submenu_Flag
	                                DIAPER_Submenu_Flag = 0
#					global BATH_Submenu_Flag
					BATH_Submenu_Flag = 0
#					global SLEEP_Submenu_Flag
        	                        SLEEP_Submenu_Flag = 0
#					global reset_button
					reset_button = 0
	
			 else:
#				global reset_button
				reset_button = 0
				if(Flag_Main_Menu):
					lcd.lcd_cls()
					lcd.main_menu()
#					global Flag_Main_Menu
					Flag_Main_Menu = 0
                         GPIO.output(20, GPIO.LOW)
#			 global Flag_LCD_Backlight
			 Flag_LCD_Backlight = 1
#			 print ("Flag_Second="+str(Flag_Second))
                elif OK_button:
			 print(" ----- In OK BUTTON Defination ----- ")
#			 global OK_Button_Data_Backup_Flag	
#			 OK_Button_Data_Backup_Flag = 1
			 now = datetime.datetime.now()
#                         global minute_1
			 minute_1 = int(now.minute)
#			 global Flag_0to54_Match
                         Flag_0to54_Match = 1
#                         global Flag_55_Match
                         Flag_55_Match = 1
#                         global Flag_56_Match
                         Flag_56_Match = 1
#                         global Flag_57_Match
                         Flag_57_Match = 1
#                         global Flag_58_Match
                         Flag_58_Match = 1
#                         global Flag_59_Match
                         Flag_59_Match = 1
			 GPIO.output(20, GPIO.HIGH)
#                         global Flag_LCD_Backlight
                         Flag_LCD_Backlight = 1

			 if(OK_Button_Data_Backup_Flag):
				 now = datetime.datetime.now()
#                         date = datetime.datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
				 date = datetime.datetime.now().strftime("%m_%d_%Y")
                	         global Second
                        	 Second = int(now.second)
	    	                 global Minute
        	                 Minute = int(now.minute)
                	         global Hour
                        	 Hour = int(now.hour)

				 print("NURSING_LEFT_SUBMENU = "+ str(NURSING_LEFT_Submenu_Flag))
 				 print("NURSING_RIGHT_SUBMENU = "+ str(NURSING_RIGHT_Submenu_Flag))
				 print("FORMULA_SUBMENU = "+ str(FORMULA_Submenu_NEXT_Flag))
				 print("BREAST_SUBMENU = "+ str(BREAST_MILK_Submenu_NEXT_Flag))
				 print("SOLID_SUBMENU = "+ str(SOLID_Submenu_NEXT_Flag))
                                 print("DIAPER_SUBMENU = "+ str(DIAPER_Submenu_Flag))
                                 print("SLEEP_SUBMENU = "+ str(SLEEP_Submenu_Flag))
                                 print("PUMPING_LEFT_START_Submenu_Flag = "+ str(PUMPING_LEFT_START_Submenu_Flag))
				 print("PUMPING_RIGHT_START_Submenu_Flag = "+ str(PUMPING_RIGHT_START_Submenu_Flag))
				 print("PUMPING_LEFT_END_Submenu_Flag = "+ str(PUMPING_LEFT_END_Submenu_Flag))
				 print("PUMPING_RIGHT_END_Submenu_Flag = "+ str(PUMPING_RIGHT_END_Submenu_Flag))
				 print("BATH_Submenu_Flag = "+ str(BATH_Submenu_Flag))
				 print("MEDICINE_Submenu_Flag = "+ str(MEDICINE_Submenu_Flag))

			 	 if(NURSING_LEFT_Submenu_Flag == 1):
                			file = open("/home/pi/11-06-16/"+ date + ".csv","a")
                			file.write("NURSING, LEFT, ")
                			file.write("Time Stamp = " + str(Hour)+':'+str(Minute)+':'+str(Second)+'\n')
#                			file.write("Thank You")
				
			 	 elif(FORMULA_Submenu_NEXT_Flag == 1):
                                        file = open("/home/pi/11-06-16/"+ date + ".csv","a")
                                        file.write("FEED, FORMULA, ")
                                        file.write("Time Stamp = " + str(Hour)+':'+str(Minute)+':'+str(Second)+'\n')

				 elif(BREAST_MILK_Submenu_NEXT_Flag == 1):
                                        file = open("/home/pi/11-06-16/"+ date + ".csv","a")
                                        file.write("FEED, BREAST MILK, ")
                                        file.write("Time Stamp = " + str(Hour)+':'+str(Minute)+':'+str(Second)+'\n')

                                 elif(SOLID_Submenu_NEXT_Flag == 1):
                                        file = open("/home/pi/11-06-16/"+ date + ".csv","a")
                                        file.write("FEED, SOLID, ")
                                        file.write("Time Stamp = " + str(Hour)+':'+str(Minute)+':'+str(Second)+'\n')
				 
				 elif(DIAPER_Submenu_Flag == 1):
					file = open("/home/pi/11-06-16/"+ date + ".csv","a")
                                        file.write("DIAPER, ")
                                        file.write("Time Stamp = " + str(Hour)+':'+str(Minute)+':'+str(Second)+'\n')

				 elif(SLEEP_Submenu_Flag == 1):
                                        file = open("/home/pi/11-06-16/"+ date + ".csv","a")
                                        file.write("SLEEP, ")
                                        file.write("Time Stamp = " + str(Hour)+':'+str(Minute)+':'+str(Second)+'\n')
				
				 elif(PUMPING_LEFT_START_Submenu_Flag == 1 and PUMPING_RIGHT_START_Submenu_Flag == 0 and PUMPING_LEFT_END_OK_Flag != 1):
					file = open("/home/pi/11-06-16/"+ date + ".csv","a")
                                        file.write("PUMPING, LEFT, START, ")
                                        file.write("Time Stamp = " + str(Hour)+':'+str(Minute)+':'+str(Second)+'\n')
				
				 elif(PUMPING_RIGHT_START_Submenu_Flag == 1 and PUMPING_LEFT_START_Submenu_Flag == 0 and PUMPING_RIGHT_END_OK_Flag != 1 and BATH_Submenu_Flag != 1 and MEDICINE_Submenu_Flag != 1):
                                        file = open("/home/pi/11-06-16/"+ date + ".csv","a")
                                        file.write("PUMPING, RIGHT, START, ")
                                        file.write("Time Stamp = " + str(Hour)+':'+str(Minute)+':'+str(Second)+'\n')

				 elif(PUMPING_LEFT_END_OK_Flag == 1):
                                        file = open("/home/pi/11-06-16/"+ date + ".csv","a")
                                        file.write("PUMPING, LEFT, END, ")
                                        file.write("Time Stamp = " + str(Hour)+':'+str(Minute)+':'+str(Second)+'\n')

				 elif(PUMPING_RIGHT_END_OK_Flag == 1 and BATH_Submenu_Flag != 1 and MEDICINE_Submenu_Flag != 1):
                                        file = open("/home/pi/11-06-16/"+ date + ".csv","a")
                                        file.write("PUMPING, RIGHT, END, ")
                                        file.write("Time Stamp = " + str(Hour)+':'+str(Minute)+':'+str(Second)+'\n')
				
				 elif(BATH_Submenu_Flag == 1):
                                        file = open("/home/pi/11-06-16/"+ date + ".csv","a")
                                        file.write("BATH, ")
                                        file.write("Time Stamp = " + str(Hour)+':'+str(Minute)+':'+str(Second)+'\n')

                                 elif(MEDICINE_Submenu_Flag == 1):
                                        file = open("/home/pi/11-06-16/"+ date + ".csv","a")
                                        file.write("MEDICINE, ")
                                        file.write("Time Stamp = " + str(Hour)+':'+str(Minute)+':'+str(Second)+'\n')

				 elif(NURSING_RIGHT_Submenu_Flag == 1):
                                        file = open("/home/pi/11-06-16/"+ date + ".csv","a")
                                        file.write("NURSING, RIGHT, ")
                                        file.write("Time Stamp = " + str(Hour)+':'+str(Minute)+':'+str(Second)+'\n')
	
#				 global OK_Button_Data_Backup_Flag
				 OK_Button_Data_Backup_Flag = 0
				
			 if clear_flag:
				lcd.lcd_cls()
#                                port.write("Hello\r\n")
#				global clear_flag
				clear_flag = 0
#			 lcd.menu_1()
			 GPIO.output(20, GPIO.HIGH)
#			 global Flag_LCD_Backlight
			 Flag_LCD_Backlight = 1
#############################################################

#-----------------------------Sleep Mode-----------------------------------
 		if(minute_1 < 55):
                        Flag_0to54 = 1
                elif(minute_1 == 55):
                        Flag_55 = 1
                elif(minute_1 == 56):
                        Flag_56 = 1
                elif(minute_1 == 57):
                        Flag_57 = 1
                elif(minute_1 == 58):
                        Flag_58 = 1
                elif(minute_1 == 59):
                        Flag_59 = 1

                if(Flag_0to54 == 1):
                        if(Flag_0to54_Match == 1):
#                                global minute_2
                                minute_2 = minute_1 +  5
#                                global Flag_0to54_Match
                                Flag_0to54_Match = 0
#				global Flag_0to54
				Flag_0to54 = 0
#				print (" ----- SLEEP MODE : In 0to54 MATCH FLAG ----- ")
                elif(Flag_55 == 1 and Flag_0to54_Match == 1):
                        if(Flag_55_Match == 1):
#                                global minute_2
                                minute_2 = 0
#                                global Flag_55_Match
                                Flag_55_Match = 0
#				global Flag_55
				Flag_55 = 0
#                               print (" ----- SLEEP MODE : In 55 MATCH FLAG ----- ")
                elif(Flag_56 == 1):
                        if(Flag_56_Match == 1 and  Flag_55_Match == 1):
#                                global minute_2
#                                minute_2 = 1
#                                global Flag_56_Match
                                Flag_56_Match = 0
#				global Flag_56
                                Flag_56 = 0
#                               print (" ----- SLEEP MODE : In 56 MATCH FLAG ----- ")
                elif(Flag_57 == 1):
                        if(Flag_57_Match == 1 and Flag_56_Match == 1 and Flag_55_Match == 1):
#                                global minute_2
                                minute_2 = 2
#                 		global Flag_57_Match
                                Flag_57_Match = 0
#				global Flag_57
                                Flag_57 = 0
#                               print (" ----- SLEEP MODE : In 57 MATCH FLAG ----- ")
                elif(Flag_58 == 1):
                        if(Flag_58_Match == 1 and Flag_57_Match == 1 and Flag_56_Match == 1 and Flag_55_Match == 1):
#                                global minute_2
                                minute_2 = 3
#                                global Flag_58_Match
                                Flag_58_Match = 0
#				global Flag_58
                                Flag_58 = 0
#                               print (" ----- SLEEP MODE : In 58 MATCH FLAG ----- ")
                elif(Flag_59 == 1):
                        if(Flag_59_Match == 1 and Flag_58_Match == 1 and Flag_57_Match == 1 and Flag_56_Match == 1 and Flag_55_Match == 1):
#                                global minute_2
                                minute_2 = 4
#                                global Flag_59_Match
                                Flag_59_Match = 0
#				global Flag_59
                                Flag_59 = 0
#                               print (" ----- SLEEP MODE : In 59 MATCH FLAG ----- ")

#                print (minute_1)
#                print (minute_2)

                if(minute_1 == minute_2):
                        print("Sleep Mode True")
#			global Flag_LCD_Backlight
			Flag_LCD_Backlight = 0
			lcd.lcd_cls()
			time.sleep(1)
  			GPIO.output(LCD_Backlight,False)
			time.sleep(0.1)
#			lcd.lcd_cls()
			clear_for_reset_button();		
 
#                        global Flag_0to54
                        Flag_0to54 = 0
#                        global Flag_55
                        Flag_55 = 0
#                        global Flag_56
                        Flag_56 = 0
#                        global Flag_57
                        Flag_57 = 0
#                        global Flag_58
                        Flag_58 = 0
#                        global Flag_59
                        Flag_59 = 0

#                        global Flag_0to54_Match
                        Flag_0to54_Match = 1
#                        global Flag_55_Match
                        Flag_55_Match = 1
#                        global Flag_56_Match
                        Flag_56_Match = 1
#                        global Flag_57_Match
			Flag_57_Match = 1
#                        global Flag_58_Match
                        Flag_58_Match = 1
#                        global Flag_59_Match
                        Flag_59_Match = 1
                else:
#                        print("Sleep Mode False")
			if(Flag_LCD_Backlight == 1):
		                GPIO.output(LCD_Backlight,True)
                
#		global Flag_0to54_Match
                Flag_0to54_Match = 0
#                global Flag_55_Match
                Flag_55_Match = 0
#                global Flag_56_Match
                Flag_56_Match = 0
#                global Flag_57_Match
                Flag_57_Match = 0
#                global Flag_58_Match
                Flag_58_Match = 0
#                global Flag_59_Match
                Flag_59_Match = 0

###################### Main Function ########################
if __name__ == "__main__":
#----------------------- Unique ID --------------------------
	myserial = getserial()
        print("\n UNIQUE ID For This Raspberry Pi Is:" + myserial)
	demo()
#############################################################
