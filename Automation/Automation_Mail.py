import smtplib          # Used to send mail using SMTP Protocol
import schedule         # Used to schedule task periodically
import time             # Used for sleep()
import sys              # Used for command line arguments

from email.mime.text import MIMEText
# MIMEText is used to create mail body

from email.mime.multipart import MIMEMultipart
# MIMEMultipart is used to create complete mail
# (Sender + Receiver + Subject + Body)

#----------------------------------------------------------
# SendMail function sends the mail
#----------------------------------------------------------

def SendMail(Sender,Password,Receiver):

    # Create Mail Object
    Message = MIMEMultipart()

    # Sender Mail ID
    Message["From"] = Sender

    # Receiver Mail ID
    Message["To"] = Receiver

    # Mail Subject
    Message["Subject"] = "Automation Report From Prathamesh"

    # Mail Body
    Body = """

        Hello,

        This mail is generated automatically.

        Automation Script is working successfully.

        Status : SUCCESS

        Thank You
        Prathamesh Tiparkar

        """


    # Attach Body with Mail
    Message.attach(MIMEText(Body,"plain"))

    try:

        # Gmail SMTP Server
        Obj = smtplib.SMTP("smtp.gmail.com",587)

        # Start Encryption
        Obj.starttls()

        # Login into Gmail
        Obj.login(Sender,Password)

        # Send Mail
        Obj.sendmail(Sender,
                     Receiver,
                     Message.as_string())

        # Close Connection
        Obj.quit()

        print("Mail sent successfully")

    except Exception as E:

        print("Unable to send mail")
        print(E)

#----------------------------------------------------------
# Main Function
#----------------------------------------------------------

def main():

    Border = "-"*50
    print(Border)
    print(" T-Parkar Mail Automation ")
    print(Border)

    if(len(sys.argv)==5):

        Sender = sys.argv[1]
        Password = sys.argv[2]

        Receiver = sys.argv[3]

        TimeInterval = int(sys.argv[4])

        print("Scheduler Started...")
        print("Press Ctrl + C to stop")

        # Schedule the function
        schedule.every(TimeInterval).minutes.do(
            SendMail,
            Sender,
            Password,
            Receiver
        )

        while True:
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invalid Arguments")
        print("Usage : ")
        print("python MailAutomation.py Sender Password Receiver Time")

    print(Border)
    print(" Thank You ")
    print(Border)


if __name__=="__main__":
    main()