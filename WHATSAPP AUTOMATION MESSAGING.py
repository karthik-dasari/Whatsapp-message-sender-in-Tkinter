from tkinter import *
import selenium,time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def start():
    start.driver=webdriver.Chrome()
    start.driver.maximize_window()
    start.driver.get("https://web.whatsapp.com/")

def send():
    contact_name=contact_entry.get()
    message=message_entry.get()
    start.driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]').send_keys(contact_name)
    start.driver.find_element_by_xpath("//span[@title='"+contact_name+"']").click()
    time.sleep(2)
    start.driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(message + Keys.ENTER)

root = Tk()                                 
root.title("WhatsApp Automation")
root.iconbitmap('wi.ico')

contact_label=Label(root,text="Enter the Name of the Contact you want to Send Message:-(CASE Sensitive)")
contact_label.grid(row=0,column=0)
contact_entry=Entry(root,width=40,borderwidth=5)
contact_entry.grid(row=1,column=0)

message_label=Label(root,text="Enter the Message you want to send:-")
message_label.grid(row=2,column=0)
message_entry=Entry(root,width=40,borderwidth=5)
message_entry.grid(row=3,ipady=40,column=0)

button_start=Button(root,text="Start",padx=40,pady=5,command=start)
button_start.grid(row=4,column=0)

send_label=Label(root,text="Scan the QR Code with your phone\nAfter you have successfully logged in click the 'Send' button below:")
send_label.grid(row=5,column=0)

button_send=Button(root,text="Send",padx=40,pady=5,command=send)
button_send.grid(row=6,column=0)

root.mainloop()