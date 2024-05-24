import tkinter as tk
import math
import time


class AnalogClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Analog Clock")
        self.canvas = tk.Canvas(root, width=400, height=400, bg='white')
        self.canvas.pack()

        self.center_x = 200
        self.center_y = 200
        self.clock_radius = 180
        self.draw_clock_face()
        self.update_clock()

    def draw_hand(self, length, angle, width, color):
        end_x = self.center_x + length * math.cos(angle)
        end_y = self.center_y - length * math.sin(angle)
        self.canvas.create_line(self.center_x, self.center_y, end_x, end_y, width=width, fill=color, tags='hands')

    def update_clock(self):
        self.canvas.delete('hands')
        current_time = time.localtime()
        seconds = current_time.tm_sec
        minutes = current_time.tm_min
        hours = current_time.tm_hour % 12

        # Calculate the angles for each hand
        seconds_angle = math.radians(90 - (seconds * 6))
        minutes_angle = math.radians(90 - (minutes * 6 + seconds * 0.1))
        hours_angle = math.radians(90 - (hours * 30 + minutes * 0.5))

        # Draw the clock hands
        self.draw_hand(self.clock_radius - 20, seconds_angle, 1, 'red')
        self.draw_hand(self.clock_radius - 40, minutes_angle, 3, 'blue')
        self.draw_hand(self.clock_radius - 60, hours_angle, 6, 'black')

        # Schedule the update_clock function to be called after 1000 ms (1 second)
        self.root.after(1000, self.update_clock)

    def draw_clock_face(self):
        for i in range(12):
            angle = math.radians(90 - i * 30)
            x = self.center_x + (self.clock_radius - 10) * math.cos(angle)
            y = self.center_y - (self.clock_radius - 10) * math.sin(angle)
            self.canvas.create_text(x, y, text=str(i if i != 0 else 12), font=('Helvetica', 15, 'bold'))


if __name__ == '__main__':
    root = tk.Tk()
    clock = AnalogClock(root)
    root.mainloop()
