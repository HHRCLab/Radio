import customtkinter as ctk
from PIL import Image
import time
import random


class App(ctk.CTk):
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    def __init__(self):
        super().__init__()
        self.Frame = ArduinoFrame(self)
        self.Frame.grid()


class ArduinoFrame(ctk.CTkFrame):

    def __init__(self, *args, Name="DefaultName", IP="192.168.1.1", Port=5050, **kwargs):
        super().__init__(*args, **kwargs)

        self.Name = ctk.CTkLabel(self, text=f"{Name},{IP},{Port}")
        self.Name.grid(row=0, column=0)
        self.LightImg = ctk.CTkImage(light_image=Image.open("./GreenLight.png"))
        self.button = ctk.CTkButton(self, image=self.LightImg, corner_radius=13)
        self.button.grid(row=1, column=0)



app = App()
app.mainloop()
