import tkinter as tk
from tkinter import ttk
import datetime
import pygame
import threading


font = "Times new Roman", 13
font2 = "Times new Roman", 13, "bold"
root = tk.Tk()
root.title("Mini Alarm")
root.geometry("+300+50")
root.minsize(300, 50)
root.resizable(False, False)
root.configure(bg="black")


def musicPlay():
    pygame.mixer.init()
    pygame.mixer.music.load("D:/MySpace/Music/Galti_se_mistake.mp3")        # give your file path
    pygame.mixer.music.play()
    pygame.time.delay(20000)

    pygame.mixer.music.stop()
    pygame.mixer.quit()
    pygame.quit()


def alarmClock():
    while True:
        try:
            currTime = datetime.datetime.now()
            setTime = f"{setHour.get()}:{setMinute.get()}"
            if currTime.strftime("%H:%M") == setTime:
                textLabel.config(text="Time to wake up!")
                root.update()
                threading.Thread(target=musicPlay).start()
                break
        except ValueError:
            print("Invalid. Please try again.")
            continue


def closeAlarm():
    while pygame.mixer.music.get_busy():
        pygame.mixer.music.stop()
        pygame.mixer.quit()
        pygame.quit()


def close():
    root.destroy()
    exit()


# Label for any text
textLabel = tk.Label(root, text="Set your alarm", bg="black", fg="white", font=font2)
textLabel.place(relx=0.01, rely=0.01, relheight=0.3, relwidth=0.98)

# set date and time
setHour = ttk.Combobox(root, values=[f"{hour:02d}" for hour in range(24)])
setMinute = ttk.Combobox(root, values=[f"{minute:02d}" for minute in range(0, 60, 5)])
setHour.set("hr")
setMinute.set("min")
setHour.config(font=font)
setMinute.config(font=font)
setHour.place(relx=0.01, rely=0.60, relheight=0.18, relwidth=0.2)
setMinute.place(relx=0.22, rely=0.60, relheight=0.18, relwidth=0.2)

# Set alarm button
setAlarm = tk.Button(root, text="Set", font=font2, command=alarmClock)
setAlarm.place(relx=0.43, rely=0.60, relheight=0.18, relwidth=0.27)
# Close alarm button
setAlarm = tk.Button(root, text="Stop", font=font2, command=closeAlarm)
setAlarm.place(relx=0.71, rely=0.60, relheight=0.18, relwidth=0.27)
# Close button
closeButton = tk.Button(root, text="Close", font=font2, bg="red", fg="white", command=close)
closeButton.place(relx=0.01, rely=0.79, relheight=0.2, relwidth=0.98)


if __name__ == "__main__":
    root.mainloop()
