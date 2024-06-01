from tkinter import ttk


class Labels:
    def __init__(self, position, text, x_position, y_position):
        self.position = position
        self.text = text
        self.x_position = x_position
        self.y_position = y_position

    def label(self):
        font_style = "Garamond"
        font_size = 11
        label_widget = ttk.Label(
            self.position,
            text=self.text,
            font=(font_style, font_size),
        )

        label_widget.place(x=self.x_position, y=self.y_position)


class Entries:
    def __init__(self, position, text_variable, x_position, y_position, width=10, entry_state="normal"):
        self.position = position
        self.radius_mean_id = text_variable
        self.x_position = x_position
        self.y_position = y_position
        self.width = width
        self.entry_state = entry_state

    def entry(self):
        font_style = "Garamond"
        font_size = 10
        entry_widget = ttk.Entry(
            self.position,
            textvariable=self.radius_mean_id,
            font=(
                font_style,
                font_size
            ),
            width=self.width
        )

        entry_widget.config(state=self.entry_state)
        entry_widget.place(x=self.x_position, y=self.y_position)


class Buttons:
    def __init__(self, position, text, command, row, col, pad_x, pad_y, bg="#52998e", fg="white", width=23,
                 font_style="Garamond", font_size=10):
        self.position = position
        self.text = text
        self.command = command
        self.row = row
        self.col = col
        self.pad_x = pad_x
        self.pad_y = pad_y
        self.bg = bg
        self.fg = fg
        self.width = width
        self.font_style = font_style
        self.font_size = font_size

    def button_position(self):
        ttk.Button(
            self.position,
            compound=self.command,
            text=self.text,
            width=self.width,
            style=self.font_style
        ).grid()
