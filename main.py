from gtts import gTTS
from playsound import playsound
from IPython.display import Audio
from playsound import playsound
import pyttsx3
from bs4 import BeautifulSoup
import requests
from tkinter import *
from tkinter import messagebox
import turtle

tts = gTTS("This project is done by team alphacoders")
tts.save('3.wav')
sound_file_3 = '3.wav'
playsound(sound_file_3)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}


def help():
    tts = gTTS("Thanks vedhaa ,Haneesh ,and sunanth for programming me")
    tts.save('4.wav')
    sound_file_4 = '4.wav'
    playsound(sound_file_4)
    messagebox.showinfo("Thanks", "Thanks")
    turtle.color('black')
    style = ('Arial', 30, 'italic')
    turtle.write('ALPHA CODERS!!', font=style, align='center')
    j = input()
    if j.isalpha(): exit()

    turtle.hideturtle()

    exit()


def hel():
    k = e1.get()
    weather(k)


def weather(city):
    city += " weather"
    # Weather detection funtion starts
    try:
        l = []
        city = city.replace(" ", "+")
        res = requests.get(
            f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8',
            headers=headers)
        print("Searching in google......\n")
        soup = BeautifulSoup(res.text, 'html.parser')
        location = soup.select('#wob_loc')[0].getText().strip()
        time = soup.select('#wob_dts')[0].getText().strip()
        info = soup.select('#wob_dc')[0].getText().strip()
        weather = soup.select('#wob_tm')[0].getText().strip()
        print(location)
        print(time)
        print(info)
        print(weather + "°C")
        print(location)
        splitted = location.split(",")
        # print(splitted)
        l = splitted[0] + " located in " + " ".join(
            splitted[1:]) + " is ," + info + " and the whether is " + weather + "°C"
        # l=[location,",",time,",",info,",",weather+"°F"]
    except:
        print("Hey you entered a wrong area! please.. check again ")
        l = ["Hey you entered a wrong area! please.. check again"]
    tts = gTTS("".join(l))
    tts.save('1.wav')
    sound_file = '1.wav'

    playsound(sound_file)
    messagebox.showinfo("information", l)


master = Tk()
master.title("Weather checker - Alpha coders")
# master.geometry("500x200")
Label(master, text='Enter city: ').grid(row=0)
tts = gTTS("Enter city")
tts.save('2.wav')
sound_file = '2.wav'
playsound(sound_file)
e1 = Entry(master)
e1.grid(row=0, column=1, columnspan=10, sticky=W)
print("hello" + e1.get())

b = Button(master, text="Get temperature", command=hel)
b.grid(row=2, column=1)

b1 = Button(master, text='Quit', command=help).grid(row=4, column=1)

mainloop()
