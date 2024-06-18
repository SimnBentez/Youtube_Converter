from typing import Tuple
from customtkinter import *
from tkinter import *
import tkinter.messagebox as messagebox
from pytube import YouTube
from PIL import Image, ImageTk

class FormsYouTubeConverter(CTk):
    #First initialize class for library customtkinter

    def __init__(self):
        super().__init__()
        self.configure_window()
        self.widgets_window()

    def configure_window(self):
        #Here let's to configure the window of main
        self.title("Convertidor de YouTube")
        w, h = 620, 400
        self.geometry(f"{w}x{h}")
        #Icon
        icon_path = "./Frontend/Pictures/icon_image.ico"
        self.iconbitmap(icon_path)
        icon_path1 = "./Frontend/Pictures/icon_Yc.png"
        self.Logo = util_image(icon_path1, 325, 70)
        

    def widgets_window(self):
        #Image of main in the app
        ImageMenu = Label(self, image=self.Logo)
        ImageMenu.place(relx=0.5, rely=0.1, anchor="center") #It's centred
        LabelConverter = CTkLabel(self, text="Coloque el enlace y el tipo de archivo que desea", 
                        font=("Aptos", 14))
        LabelConverter.place(relx=0.25, rely=0.2)
        self.ComboBox = CTkComboBox(self, values=[".mp3", ".mp4"], state="readonly")
        self.ComboBox.place(relx=0.7, rely=0.3)
        self.Entry = CTkEntry(self, placeholder_text="Pegue el enlace aquí...", width=350,
                         text_color="#FFCC70")
        self.Entry.place(relx=0.08, rely=0.3)
        self.Button = CTkButton(self, text="Convertir", corner_radius=32, 
            fg_color="#0366FF", hover_color="#000B48", border_color="#000000", 
            border_width=2, cursor="hand2", 
            command=self.Converter_Button) #The button is customized
        self.Button.place(relx=0.5, rely=0.8, anchor="center") # Make sure the
        #button is centred

    def Converter_Button(self):
        """
        This function will be responsible for when the button 
        is pressed, performing the download either in mp3 or mp4 format
        """
        if self.Entry.get() == "":
             return messagebox.showinfo("Información", "No ha colocado ningún enlace de video")
        elif self.ComboBox.get() == "":
             return messagebox.showinfo("Información", "No ha colocado ningún formato")
        else:
            url = self.Entry.get()
            format_url = self.ComboBox.get()
            self.config(cursor="wait")
            if format_url==".mp3":
                  try:
                       #Make a object
                       ytc = YouTube(url)
                       title = ytc.title
                       title = ''.join(char for char in title if char.isalnum() or char in " -_")
                       audio_url = ytc.streams.filter(only_audio=True).first()
                       audio_url.download(output_path="./Downloads", filename=f"{title}.mp3")
                       self.config(cursor="")
                       return messagebox.showinfo("Información", "Se obtuvo el audio con éxito")
                  except:
                       self.config(cursor="")
                       return messagebox.showinfo("Información", "No se encontró el enlace")
            else:
                 try:
                    #Make a object
                    ytc = YouTube(url)
                    title = ytc.title
                    title = ''.join(char for char in title if char.isalnum() or char in " -_")
                    video = ytc.streams.get_highest_resolution()
                    video.download(output_path="./Downloads", filename=f"{title}.mp4")
                    self.config(cursor="")
                    return messagebox.showinfo("Información", "Se obtuvo el video con éxito")
                 except:
                      self.config(cursor="")
                      return messagebox.showinfo("Información", "No se encontró el enlace")

def util_image(path, a, b):
        """
        This function is used for can resize and load image on window  
        """
        return ImageTk.PhotoImage(Image.open(path).resize((a,b), Image.ADAPTIVE))