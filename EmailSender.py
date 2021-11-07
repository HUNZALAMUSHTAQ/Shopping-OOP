import smtplib,ssl
class Email_sender_s:
    '''Verified Email checker using port 465 support gmail '''
    port=465
    smtp_server="smtp.gmail.com"
    def __init__(self):
        '''It takes the sender Email and Password Recommended : Gmail '''
        self.state=False 
        self.sender_email="computerprogram812@gmail.com"
        self.__password="computer812"
        self.__code=None
        print("6-DIGIT CODE HAS BEEN SENT TO YOUR EMAIL")
    def send_code(self,receiver_email,message=None):
        '''It Takes the receiver email and send random 6 digit code and if you want to send extra message Use message parameter if any error received print it as a message  '''
        self.__random_number()
        self.Receiver_email=receiver_email
        if self.__code==None:
            message="Error"
        else :
            message=self.__code
        try :
            context=ssl.create_default_context()
            with smtplib.SMTP_SSL(Email_sender_s.smtp_server,Email_sender_s.port,context=context) as server :
                server.login(self.sender_email,self.__password)
                server.sendmail(self.sender_email,receiver_email,message)
                print("Success")
        except Exception as e :
            print(e)
    def __random_number(self):
        '''It generates Random number '''
        from random import randint
        self.__code=""
        for _ in range(6):
            self.__code+=str(randint(1,9))

    def verify_me(self):
        raw_input=input("Enter the 6 digit Code ")
        if raw_input == self.__code:
            self.state=True
            return "Verified"
            
        else:
            self.state=False
            return "Incorrect"
            
    def resend_code(self):
        '''Resend the Code '''
        self.send_code(self.Receiver_email)



