import smtplib # Importing the SMTPLIB Module for this Program.

Sender_Mail = "suryathakur.0705@gmail.com" # Giving it our Mail ID to Sign in.
Password = "Your App Password" # Giving our Program a specefic 16-Digit App Password. Check the Readme.md file where I have told how to get it.

Server = smtplib.SMTP('smtp.gmail.com', 587) # Defining the Server and giving it the Port.
Server.starttls() # Starting the Server.
Server.login(Sender_Mail, Password) # Giving SMTP our Mail ID and Password to Sign in.
print("Signed in Successfully...") # If the Program has Signed in Successfully then Printing it.

Receivers_Mail = input("Enter the Receiver's Mail Id: ") # Taking the Receiver's Mail ID from the User.
SUBJECT = input("What should be the Subject of the Mail? Type in here: ") # Taking the Mail's Subject from the User.
TEXT = input("Type in your Message: ") # Taking the Message from the User.
Message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT) # Giving the Subject and Content a Format.

Server.sendmail(Sender_Mail, Receivers_Mail, Message) # Telling the Program about Receiver's Mail, Sender's Mail, and the Content.
print("Email sent Succesfully !") # Printing that Email has been Sent.
Server.quit() # Quitting the Server.