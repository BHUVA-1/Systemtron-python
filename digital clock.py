import tkinter as tk
import time

class DigitalClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Digital Clock")
        self.time_label = tk.Label(root, font=('Helvetica', 48), bg='black', fg='white')
        self.time_label.pack(anchor='center')
        self.update_clock()

    def update_clock(self):
        current_time = time.strftime('%H:%M:%S')
        self.time_label.config(text=current_time)
        self.root.after(1000, self.update_clock)

if __name__ == '__main__':
    root = tk.Tk()
    clock = DigitalClock(root)
    root.mainloop()
