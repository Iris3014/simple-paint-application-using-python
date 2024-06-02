import tkinter as tk
from tkinter.colorchooser import askcolor

class PaintApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Paint Application")

        self.current_color = "black"
        self.canvas = tk.Canvas(self.root, bg="white", width=800, height=600)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<Button-1>", self.on_button_press)

        self.setup_color_palette()
        self.setup_clear_button()

        self.previous_x = None
        self.previous_y = None

    def setup_color_palette(self):
        color_palette = tk.Frame(self.root, bg="white")
        color_palette.pack(side=tk.TOP, fill=tk.X)

        colors = ["black", "red", "green", "blue", "yellow", "pink", "orange", "purple"]
        for color in colors:
            color_button = tk.Button(color_palette, bg=color, width=2, command=lambda col=color: self.change_color(col))
            color_button.pack(side=tk.LEFT, padx=2, pady=2)

        choose_color_button = tk.Button(color_palette, text="More Colors", command=self.choose_color)
        choose_color_button.pack(side=tk.LEFT, padx=2, pady=2)

    def setup_clear_button(self):
        clear_button = tk.Button(self.root, text="Clear", command=self.clear_canvas)
        clear_button.pack(side=tk.BOTTOM, padx=2, pady=2)

    def change_color(self, color):
        self.current_color = color

    def choose_color(self):
        color = askcolor(color=self.current_color)[1]
        if color:
            self.current_color = color

    def on_button_press(self, event):
        self.previous_x = event.x
        self.previous_y = event.y

    def paint(self, event):
        if self.previous_x and self.previous_y:
            self.canvas.create_line(self.previous_x, self.previous_y, event.x, event.y, fill=self.current_color, width=3)
            self.previous_x = event.x
            self.previous_y = event.y

    def clear_canvas(self):
        self.canvas.delete("all")

if __name__ == "__main__":
    root = tk.Tk()
    app = PaintApp(root)
    root.mainloop()
