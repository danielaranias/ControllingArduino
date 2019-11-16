
import serial   

INVALID_COM_NUM = -666

class ArduinoSerialController:
    def __init__(self,Serialcom_number,baud_rate=9600):
        print("init")
        self.com_number = Serialcom_number
        self.baud_rate = baud_rate
        self.arduino_serial = INVALID_COM_NUM
        try:
            #Create Serial port object called arduinoSerialData
            self.arduino_serial = serial.Serial(self.com_number,self.baud_rate)
            print(self.arduino_serial.readline()) 
        except:
            self.arduino_serial = INVALID_COM_NUM
            print("init failed")
            raise AssertionError("Init failed")
            
            
        
    #This is a decorator that tell python it is a property. this property has a function.
    #that way I can add validation or logic in. whenever num is called, the function will be invoked
    @property
    def com_number(self):
        print("Getting private property")
        #by putting _ before the attribute, I am signaling to the user that it is a private member
        #(although there is not such thing in python)
        return self._com_number
        
    #in order to implement "Setter", I am using also a Decoretaor which says that the property"com_number" has a "Setter" function
    @com_number.setter
    def com_number(self,SerialcomStr):
        self._com_number = SerialcomStr

    def ControllingLED_FromUserInput(self):
        """
        infinite loop that waits until user enters data for controlling the LED in the Arduino
        """
        print(self.com_number)

        if self.arduino_serial == INVALID_COM_NUM:
            print("no valid serila connection!")
            exit

        while 1:     
            print ("Enter 1- to ON LED; 0 - to OFF LED; 3 - to BLINK")                                
            input_data = input()   
            #prints the data for confirmation               
            print ("you entered", input_data)           
            
            if (input_data == '1'):      
                #send 1 to arduino                          
                self.arduino_serial.write(input_data.encode())           
                print("LED ON")
            
            if (input_data == '0'):                                   
                self.arduino_serial.write(input_data.encode())              
                print("LED OFF")

            if (input_data == '3'):                                   
                self.arduino_serial.write(input_data.encode())     
                print("LED BLINK")



def main():
    try:
        arduino_ctrl = ArduinoSerialController('com3')
        arduino_ctrl.ControllingLED_FromUserInput()
    except AssertionError as error:
        print(error)
        print('LED Controll was not executed')





if __name__ == "__main__":
    main()



  

                            



