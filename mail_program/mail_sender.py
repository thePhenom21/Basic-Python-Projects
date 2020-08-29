import tkinter
import smtplib
from tkinter import filedialog 
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
import time

screen = tkinter.Tk()
screen.title("Email Program")
screen.configure(background="grey")


def browseFiles():
    global filename 
    filename = filedialog.askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("Image files", "*.jpg*"), ("all files", "*.*"))) 
    
    label_file_explorer.configure(text="File Opened: "+filename) 


def send():
    finaltext.configure(text="...")
    global receiver_n, subject_n, message_n,sender_n,password_n
    sender_n = sender_name.get()
    password_n = sender_p.get()
    receiver_n = receiver_name.get()
    subject_n = subject_text.get("1.0",tkinter.END)
    message_n = message_text.get("1.0",tkinter.END)
    print(receiver_n, subject_n, message_n)
    sendmail()

def sendmail():
    if chk_state.get() == 1:

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()

        server.login(sender_n,password_n)

        msg = MIMEMultipart()
        msg['From'] = sender_n
        msg['To'] = receiver_n
        msg['Subject'] = subject_n

        msg.attach(MIMEText(message_n, 'plain'))
        global filename
        
        attachment = open(filename, 'rb')

        p = MIMEBase('application','octet-stream')
        p.set_payload(attachment.read())

        encoders.encode_base64(p)

        p.add_header('Content-Disposition', f'attachment; filename={filename}')
        msg.attach(p)

        text = msg.as_string()
        server.sendmail(sender_n,receiver_n,text)
        finaltext.configure(text="Email sent!")
    
        server.quit()
        
    
    else:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()

        server.login(sender_n,password_n)

        msg = f'Subject: {subject_n}\n\n{message_n}'
        msg.encode('utf-8')
        
        server.sendmail(sender_n,receiver_n,msg)
        finaltext.configure(text="Email sent!")
        server.quit()

sender = tkinter.Label(text="Sender's Email Address: ")
sender_name = tkinter.Entry(width=25)
sender_pass = tkinter.Label(text="Sender's App Password for the mail: ")
sender_p = tkinter.Entry(width=25)
receiver = tkinter.Label(text="Receiver's Email Address: ")
receiver_name = tkinter.Entry(width=25)
subject = tkinter.Label(text="Subject: ")
subject_text = tkinter.Text(width=20,height=5)
message = tkinter.Label(text="Your Message: ")
message_text = tkinter.Text(width=20,height=5)
send = tkinter.Button(text="Send",width=10,height=5,command=send)
finaltext = tkinter.Label(text="",width=15,height=1,bg="black",fg="white")

chk_state = tkinter.IntVar()
w_attach = tkinter.Checkbutton(text='with attachment',variable=chk_state)

label_file_explorer = tkinter.Label(text = "Attachment", width = 40, height = 2) 

button_explore = tkinter.Button(text = "Browse Files", command = browseFiles)  

sender.grid(row=0,column=0)
sender_name.grid(row=0,column=1)
sender_pass.grid(row=1,column=0)
sender_p.grid(row=1,column=1)
receiver.grid(row=2,column=0)
receiver_name.grid(row=2,column=1)
subject.grid(row=3,column=0)
subject_text.grid(row=3,column=1)
message.grid(row=4,column=0)
message_text.grid(row=4,column=1)
send.grid(row=4,column=2)
label_file_explorer.grid(row=5,column=0)
button_explore.grid(row=5,column=1)
w_attach.grid(row=5,column=2)
finaltext.grid(row=6,column=1)



screen.mainloop()