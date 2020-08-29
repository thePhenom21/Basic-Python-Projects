import socket
import threading
import tkinter
from tkinter import scrolledtext

screen = tkinter.Tk()
screen.title("Chat Program")
screen.configure(background="grey")

def connected():
    global ip_n , port_n , nickname_n , client
    ip_n = join_ip.get()
    port_n = join_port.get()
    nickname_n = nicknamer.get()
    try:
        client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        client.connect((str(ip_n),int(port_n)))
    except:
        message_area.insert("end","couldn't establish connection! server is down?\n")

    receive_thread = threading.Thread(target=receive)
    receive_thread.start()

def write():
        message = '{}: {}'.format(nickname_n, type_in.get())
        client.send(message.encode('ascii'))

def enter(event):
        message = '{}: {}'.format(nickname_n, type_in.get())
        client.send(message.encode('ascii'))

def closed():
    client.close()
    message_area.insert("end","connection closed\n")



join = tkinter.Label(text="Ip address of the server: ",width=20)
join_ip = tkinter.Entry(width=20)
port = tkinter.Label(text="Port of the server: ",width=20)
join_port = tkinter.Entry(width=10)
blank = tkinter.Label(text="",bg="grey",width=30,height=1)
message_area = scrolledtext.ScrolledText(width=30,height=10)
type_l = tkinter.Label(text="Your Message:")
type_in = tkinter.Entry(width=40)
connecter = tkinter.Button(text="Connect",width=20,height=2,command=connected)
send = tkinter.Button(text="Send Message",width=20,height=2,command=write)
nick = tkinter.Label(text="Your Nickname",width=20)
nicknamer = tkinter.Entry(width=30)
close = tkinter.Button(text="Close Connection",width=20,height=2,command=closed)

screen.bind('<Return>',enter)



nick.grid(row=2,column=0)
nicknamer.grid(row=2,column=1)
connecter.grid(row=1,column=2)
join.grid(row=0,column=0)
join_ip.grid(row=0,column=1)
port.grid(row=1,column=0)
join_port.grid(row=1,column=1)
blank.grid(row=4,column=0)
message_area.grid(row=5,column=1)
type_l.grid(row=6,column=0)
type_in.grid(row=6,column=1)
send.grid(row=6,column=2)
close.grid(row=2,column=2)



def receive():
    while True:
        try:
            #Receive message from server
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname_n.encode('ascii'))
            else:
                message_area.insert("end",message + "\n")
                message_area.see("end")

        except:
            #close connection when error
            client.close()
            break



screen.mainloop()