import tkinter as tk
import time


class DigitalClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Digital Clock")
        self.root.attributes('-fullscreen', True)
        self.root.configure(bg='black')

        # Bind the Escape key to exit fullscreen mode
        self.root.bind('<Escape>', self.exit_fullscreen)

        self.time_label = tk.Label(root, font=('Helvetica', 120), bg='black', fg='white')
        self.time_label.pack(expand=True)

        self.update_clock()

    def update_clock(self):
        current_time = time.strftime('%H:%M:%S')
        self.time_label.config(text=current_time)
        self.root.after(1000, self.update_clock)

    def exit_fullscreen(self, event=None):
        self.root.attributes('-fullscreen', False)
        self.root.quit()


if __name__ == '__main__':
    root = tk.Tk()
    clock = DigitalClock(root)
    root.mainloop()
