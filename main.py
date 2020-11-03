import subprocess
import tkinter as tk
from time import sleep

# Change this to specific location of On/Off files being run
PATH = "/home/james/Documents/cron/"

class vpnTimer:
    def __init__(self):
        self.window = tk.Tk()
        self.window.rowconfigure([0, 1, 2], minsize = 100, weight = 1)
        self.window.columnconfigure([0, 1, 2], minsize = 100, weight = 1)

        tk.Label(master=self.window, text="Sleep Time (hours): ").grid(row = 0, column = 1, sticky = 's')

        self.delayTimeBox = tk.Entry(master=self.window, width = 6)
        self.delayTimeBox.insert(10, "1")
        self.delayTimeBox.bind("<Return>", self.wait)
        self.delayTimeBox.grid(row = 1, column = 1)

        self.timerCountdown = tk.Label(master=self.window, text="Time Remaining: 00:00")
        self.timerCountdown.grid(row = 2, column = 1, sticky = "n")

    def run(self):
        self.window.mainloop()

    def wait(self, event):
        sleepTime = float(self.delayTimeBox.get())
        self.disconnect()
        try:
            for minute in range(0, round(sleepTime * 60)): #convert hours to minutes
                totalMinutesLeft = round(sleepTime * 60) - minute # everything after this based on this variable
                hoursLeft = int(totalMinutesLeft / 60)
                if hoursLeft < 10: # helps formatting so that it is in "HH:MM" format :)
                    hoursLeft = str("0" + str(hoursLeft))
                remainingMinutes = int(totalMinutesLeft % 60)
                if remainingMinutes < 10:
                    remainingMinutes = str("0" + str(remainingMinutes))
                self.timerCountdown.configure(text="Time Remaining: " + str(hoursLeft) + ":" + str(remainingMinutes))
                self.window.update() # necessary because it is in its own loop so allows the new configuration to update
                sleep(60)
        except:
            raise
        finally:
            # Before ending the program, everything is closed and the vpn is reconnected as would make sense :)
            self.window.destroy()
            self.connect()
            exit()

    def disconnect(self):
        subprocess.call(["sh", PATH + "piaOff.sh"])

    def connect(self):
        subprocess.Popen(["sh", PATH + "piaOn.sh"]) # Using call here breaks it and pia will close anytime you end the program
        sleep(5) # Program closes too fast so adding this allows it to actually connect

if __name__ == '__main__':
    timer = vpnTimer()
    timer.run()
