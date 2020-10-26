import subprocess
import tkinter as tk
from time import sleep

class vpnTimer:
    def __init__(self):
        self.window = tk.Tk()
        self.window.rowconfigure([0, 1, 2], minsize = 100, weight = 1)
        self.window.columnconfigure([0, 1, 2], minsize = 100, weight = 1)

        tk.Label(master=self.window, text="Sleep Time (minutes): ").grid(row = 0, column = 1, sticky = 's')

        self.delayTimeBox = tk.Entry(master=self.window, width = 6)
        self.delayTimeBox.insert(10, "60")
        self.delayTimeBox.bind("<Return>", self.wait)
        self.delayTimeBox.grid(row = 1, column = 1)

        self.inHours = tk.Label(master=self.window, text="In Hours: 1")
        self.inHours.grid(row = 2, column = 1, sticky = "n")

    def run(self):
        self.window.mainloop()

    def wait(self, event):
        sleepTime = float(self.delayTimeBox.get())
        self.inHours.configure(text="In Hours: " + str(round((float(sleepTime)/60.0), 2)))
        self.disconnect()
        try:
            sleep(int(60 * sleepTime)) # Sleep time is in minutes, but sleep takes seconds, so 60 * minutes = seconds :)
        except:
            raise
        finally:
            self.window.destroy()
            self.connect()
            exit()

    def disconnect(self):
        subprocess.call(["sh", "/home/james/Documents/cron/piaOff.sh"])

    def connect(self):
        subprocess.Popen(["sh", "/home/james/Documents/cron/piaOn.sh"]) # Using call here breaks it and pia will close anytime you end the program

if __name__ == '__main__':
    timer = vpnTimer()
    timer.run()
