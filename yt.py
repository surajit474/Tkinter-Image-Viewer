import threading
import tkinter as tk

import customtkinter as ctk
import requests
from PIL import Image


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1100x800")
        self.resizable(False,False)
        
        url = "https://mangaverse-api.p.rapidapi.com/manga/latest"
        querystring = {"page":"1","genres":"Harem,Fantasy","nsfw":"true","type":"all"}
        headers = {
            "X-RapidAPI-Key": "025bad191amsh7331ace778f51f6p1de833jsnd83c55b30d26",
            "X-RapidAPI-Host": "mangaverse-api.p.rapidapi.com"
        }

        self.r = requests.get(url, headers=headers, params=querystring)
        self.response=self.r.json()


        self.t1=threading.Thread(target=self.image_genaretor, daemon=True)
        self.t1.start()
        self.layout()
        

        self.mainloop()

    def layout(self):
        # canvas = tk.Canvas(self)
        self.upper_frame=ctk.CTkFrame(self)
        # ctk.CTK



        self.frame = ctk.CTkFrame(self)
        # scrollabl_frame=ctk.CTkScrollableFrame(self,width=200,height=700,fg_color='black')
        self.frame.columnconfigure((0, 1, 2, 3, 4), weight=1, uniform="a")
        self.frame.rowconfigure(0, weight=1, uniform="b")
        self.frame.rowconfigure((1, 2, 3), weight=2, uniform="b")
        for i in range(1,4):
            for j in range(5):
                ctk.CTkLabel(self.frame, text="img").grid(
                    column=j, row=i, sticky="nesw", pady=8, padx=8
                )
            # ctk.CTkLabel(frame,text='hiiiii',fg_color='yellow').pack(expand=True,fill='both')

        self.frame.pack(expand=True, fill="both")
        # canvas.pack(expand=True, fill="both")

    def image_genaretor(self):
        self.button=[]
        self.image_index=[]
        self.image_i=[]
        # genarating image from api
        a=0
        print("rrrrrrrrrr")
        for i in self.response['data']:
            self.image_i.append(i['thumb'])

            # r=requests.get(url)

            # open(f"{j}.jpg", "wb").write(r.content)
                

        for i in (range(1,4)):
            for j in (range(5)):

                response = requests.get(self.image_i[a])
                # response = requests.get("https://random.imagecdn.app/900/600")
                open(f"{i}{j}.jpg", "wb").write(response.content)
                im = ctk.CTkImage(
                    light_image=Image.open(f"{i}{j}.jpg"), size=(200, 250)
                )

                button = ctk.CTkButton(self.frame, image=im, text=f"{a}",text_color="black", fg_color="black",hover_color='gray',)
                button.configure(command=lambda button=button: self.black_frame(button))
                button.grid(
                    column=j, row=i, sticky="nesw", pady=8, padx=8
                )
                self.button.append(button)
                
                self.image_index.append(f"{i}{j}")
                
                # print(self.button)
                self.frame.update()
                a+=1






    def black_frame(self,button):

        im = ctk.CTkImage(
                    light_image=Image.open(f"{self.image_index[int(button.cget('text'))]}.jpg"), size=(1000, 700)
                )
        self.second_frame=ctk.CTkFrame(self,fg_color='black',)
        ctk.CTkLabel(self.second_frame,text='',image=im).pack(expand=True,fill='both')
        self.second_frame.place(relx=0,rely=0,relheight=1,relwidth=1)
        self.bind_all('<Escape>',func=lambda a:self.second_frame.place_forget())
        



# class Black_frame(ctk.CTkFrame):
#     def __int__(self,parent):
#         super.__init__(parent,fg_color='black')
#         im = ctk.CTkImage(
#                         light_image=Image.open("00.jpg"), size=(1000, 700)
#                     )

#         self.place(relx=0,rely=0,relheight=1,relwidth=1)
#         ctk.CTkLabel(self,text='',image=im).pack(expand=True,fill='both')


app = App()
