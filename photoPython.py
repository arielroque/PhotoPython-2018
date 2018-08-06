#coding:utf-8
#Created by: Ariel Luz


from tkinter import*
from PIL import Image
from tkinter import messagebox
from tkinter import filedialog
import PIL.ImageOps

gui = Tk()

gui.title("PhotoPython 2018")

gui.geometry("300x220")

image_source=""

is_selected_image = False

bt_src_imagem=""


def notify_user_error_image():
    title = "Warning!"
    text= "Selected archive is incompatible, please select another image"
    mensage = messagebox.showinfo(title,text)


def notify_user():
    title = "Warning!"
    text= "Select an image before pressing this option"
    mensage = messagebox.showinfo(title,text)
    

def save_image():

    global image_source

def rotate_image():
    global image_source, is_selected_image

    if(is_selected_image == True):
        rotate_image = image_source.rotate(180)
        rotate_image.show()
    else:
        notify_user()

def show_invert_image():
    global image_source, is_selected_image

    if(is_selected_image== True):
        invert_image = PIL.ImageOps.invert(image_source)
        invert_image.show()
    else:
        notify_user()
        

def show_original_image():
    global image_source, is_selected_image

    if(is_selected_image == True):
        image_source.show()
    else:
        notify_user()
        
def select_image():
    global image_source, is_selected_image

    try:
    
        is_selected_image = True
        image_source = Image.open(filedialog.askopenfilename())
        bt_src_image.config(text="   Selected image  ",bg="#228B22")
        bt_src_image.place(x=80,y=20)

    except:
        notify_user_error_image()
        is_selected_image=False

        
    

bt_src_image = Button(gui,text="      Select image   ",bg="#DC143C", command = select_image)
bt_src_image.place(x=80,y=20)

bt_show_image = Button(gui,text="   Original image    ",command = show_original_image)
bt_show_image.place(x=80,y=60)

bt_invert_image = Button(gui,text="     Invert image     ",command = show_invert_image)
bt_invert_image.place(x=80,y=100)

bt_rotate_image = Button(gui,text= "           Rotate         ",command = rotate_image)
bt_rotate_image.place(x=80,y=140)

copyrights=Label(gui,text="© 2018 Ariel Solutions ",bg="#2F4F4F",fg="white")
copyrights.place(x=80,y=190)
