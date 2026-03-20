# Koch_snowflake.py
from tkinter import *
import math

class KochSnowflake:
    def __init__(self):
        window = Tk()
        window.title("Koch Snowflake")
        self.width = 500
        self.height = 500
        self.canvas = Canvas(window, width=self.width, height=self.height)
        self.canvas.pack()

        # Entry frame
        frame1 = Frame(window)
        frame1.pack()
        Label(frame1, text="Enter an order:").pack(side=LEFT)
        self.order = StringVar()
        Entry(frame1, textvariable=self.order, justify=RIGHT).pack(side=LEFT)
        Button(frame1, text="Display", command=self.display).pack(side=LEFT)

        window.mainloop()

    def display(self):
        # Clear previous drawing
        self.canvas.delete("line")

        size = 300
        # Triangle points
        p1 = [self.width / 2 - size / 2, self.height / 2 + size / 3]
        p2 = [self.width / 2 + size / 2, self.height / 2 + size / 3]
        height = size * math.sqrt(3) / 2
        p3 = [self.width / 2, self.height / 2 - 2 * height / 3]

        order = int(self.order.get())

        for start, end in ((p1, p2), (p2, p3), (p3, p1)):
            self.koch_line(start, end, order)

    def koch_line(self, p1, p2, order):
        if order == 0:
            self.canvas.create_line(p1[0], p1[1], p2[0], p2[1], tags="line")
        else:
            dx = (p2[0] - p1[0]) / 3
            dy = (p2[1] - p1[1]) / 3
            pA = [p1[0] + dx, p1[1] + dy]
            pB = [p1[0] + 2 * dx, p1[1] + 2 * dy]

            # Rotate 60° counterclockwise for spike
            angle = math.radians(60)
            px = pA[0] + math.cos(angle) * (pB[0] - pA[0]) - math.sin(angle) * (pB[1] - pA[1])
            py = pA[1] + math.sin(angle) * (pB[0] - pA[0]) + math.cos(angle) * (pB[1] - pA[1])
            pC = [px, py]

            # Recurse on the 4 segments
            self.koch_line(p1, pA, order - 1)
            self.koch_line(pA, pC, order - 1)
            self.koch_line(pC, pB, order - 1)
            self.koch_line(pB, p2, order - 1)

# Run the GUI
KochSnowflake()


