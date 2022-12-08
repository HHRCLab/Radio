import customtkinter as ctk
from PIL import Image
import random


class App(ctk.CTk):
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    def __init__(self):
        super().__init__()
        self.Frame = ArduinoFrame(self)
        self.Frame.grid(row=0, column=0)
        self.Frame1 = ArduinoFrame(self)
        self.Frame1.grid(row=0, column=1)
        self.Frame1.LevelUpdate()


class ArduinoFrame(ctk.CTkFrame):

    def __init__(self, *args, Name="DefaultName", IP="192.168.1.1", Port=5050, **kwargs):
        self.test = [3, 5, 3, 4, 4, 4, 4, 3, 3, 3, 4, 3, 4, 4, 4, 4, 5, 4, 5, 4, 5, 4, 3, 5]
        super().__init__(*args, **kwargs)

        self.Name = ctk.CTkLabel(self, text=f"{Name} | {IP} | {Port}")
        self.Name.grid(row=0, column=0, columnspan=2)

        self.GreenCircle = ctk.CTkImage(light_image=Image.open("./GreenLight-removebg-preview.png"))
        self.RedCircle = ctk.CTkImage(light_image=Image.open("./RedCircle-removebg-preview.png"))
        self.YellowCircle = ctk.CTkImage(light_image=Image.open("./YellowCircle-removebg-preview.png"))
        self.GreyCircle = ctk.CTkImage(light_image=Image.open("./GreyCircle-removebg-preview.png"))
        self.Lights = [self.GreyCircle, self.RedCircle, self.YellowCircle, self.GreyCircle]
        self.lightIter = iter(self.Lights)

        self.button = ctk.CTkLabel(self, text="", image=self.GreenCircle, corner_radius=13)
        self.button.grid(row=1, column=0, sticky="w")

        self.SignalLevel = ctk.CTkLabel(self, text=f"{self.test}")
        self.SignalLevel.grid(row=1, column=1)

        self.FqButton = ctk.CTkButton(self, text="FqSet", command=lambda: self.switchLight(button=self.button, imgs=self.lightIter))
        self.FqButton.grid(row=2, column=0)

        self.FqEntry = ctk.CTkEntry(self)
        self.FqEntry.grid(row=2, column=1)

    @classmethod
    def switchLight(cls, button, imgs):
        button.configure(image=next(imgs))

    def LevelUpdate(self):
        self.after(500, self.LevelUpdate)
        self.SignalLevel.configure(text=f"{random.randint(1, 34)}")





app = App()
app.mainloop()
