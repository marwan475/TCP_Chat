import tkinter as t
import tkinter.scrolledtext


class Interface:
    def __init__(self,client):
        self.client = client
        self.count = 0

    def create(self,w):


        self.window = t.Tk()
        self.window.title("Chat")
        self.window.minsize(500,600)
        self.window.maxsize(500,600)
        self.window.config(bg="grey")


        self.label = t.Label(self.window,text="Chat",bg="gray")
        self.label.config(font=("Arial",12))
        self.label.pack(padx=20,pady=5)

        self.text_box = tkinter.scrolledtext.ScrolledText(self.window)
        #self.text_box.configure(state='disabled')
        self.text_box.pack(padx=20,pady=5)

        self.label2 = t.Label(self.window,text="Message",bg="gray")
        self.label2.config(font=("Arial",12))
        self.label2.pack(padx=20,pady=5)

        self.input = t.Text(self.window,height=2)
        self.input.pack(padx=20,pady=5)

        self.send = t.Button(self.window,text="Send",command=self.send)
        self.send.config(font=("Arial",12))
        self.send.pack(padx=20,pady=5)

        w.append(self.text_box)

        self.window.mainloop()

    def send(self):
        msg = self.input.get("1.0", "end")
        self.client.send(msg.strip().encode("utf-8"))
        self.input.delete("1.0", "end")
        if self.count >= 1:
            your_msg = f"\nYou: {msg}"
            self.text_box.insert("end", your_msg)
            self.text_box.yview("end")
            self.count += 1
        else:
            self.count += 1

    def update(self,msg,text_box):
        #self.text_box.configure(state='normal')
        text_box.insert("end", msg)
        text_box.yview("end")
        #self.text_box.configure(state='disabled')
