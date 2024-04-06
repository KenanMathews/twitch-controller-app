import pickle
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

KEY_CODES = {
    "Q": 0x10, "W": 0x11, "E": 0x12, "R": 0x13, "T": 0x14, "Y": 0x15, "U": 0x16, "I": 0x17, "O": 0x18, "P": 0x19,
    "A": 0x1E, "S": 0x1F, "D": 0x20, "F": 0x21, "G": 0x22, "H": 0x23, "J": 0x24, "K": 0x25, "L": 0x26, "Z": 0x2C,
    "X": 0x2D, "C": 0x2E, "V": 0x2F, "B": 0x30, "N": 0x31, "M": 0x32,
    "LEFT_ARROW": 0xCB, "RIGHT_ARROW": 0xCD, "UP_ARROW": 0xC8, "DOWN_ARROW": 0xD0,
    "ESC": 0x01, "ONE": 0x02, "TWO": 0x03, "THREE": 0x04, "FOUR": 0x05, "FIVE": 0x06, "SIX": 0x07, "SEVEN": 0x08,
    "EIGHT": 0x09, "NINE": 0x0A, "ZERO": 0x0B, "MINUS": 0x0C, "EQUALS": 0x0D, "BACKSPACE": 0x0E,
    "APOSTROPHE": 0x28, "SEMICOLON": 0x27, "TAB": 0x0F, "CAPSLOCK": 0x3A, "ENTER": 0x1C, "LEFT_CONTROL": 0x1D,
    "LEFT_ALT": 0x38, "LEFT_SHIFT": 0x2A, "RIGHT_SHIFT": 0x36, "TILDE": 0x29, "PRINTSCREEN": 0x37,
    "NUM_LOCK": 0x45, "SPACE": 0x39, "DELETE": 0x53, "COMMA": 0x33, "PERIOD": 0x34, "BACKSLASH": 0x35,
    "FORWARDSLASH": 0x2B, "LEFT_BRACKET": 0x1A, "RIGHT_BRACKET": 0x1B, "F1": 0x3B, "F2": 0x3C, "F3": 0x3D,
    "F4": 0x3E, "F5": 0x3F, "F6": 0x40, "F7": 0x41, "F8": 0x42, "F9": 0x43, "F10": 0x44, "F11": 0x57, "F12": 0x58,
    "NUMPAD_0": 0x52, "NUMPAD_1": 0x4F, "NUMPAD_2": 0x50, "NUMPAD_3": 0x51, "NUMPAD_4": 0x4B, "NUMPAD_5": 0x4C,
    "NUMPAD_6": 0x4D, "NUMPAD_7": 0x47, "NUMPAD_8": 0x48, "NUMPAD_9": 0x49, "NUMPAD_PLUS": 0x4E,
    "NUMPAD_MINUS": 0x4A, "NUMPAD_PERIOD": 0x53, "NUMPAD_ENTER": 0x9C, "NUMPAD_BACKSLASH": 0xB5,
    "LEFT_MOUSE": 0x100, "RIGHT_MOUSE": 0x101, "MIDDLE_MOUSE": 0x102, "MOUSE3": 0x103, "MOUSE4": 0x104,
    "MOUSE5": 0x105, "MOUSE6": 0x106, "MOUSE7": 0x107, "MOUSE_WHEEL_UP": 0x108, "MOUSE_WHEEL_DOWN": 0x109
}

class OverwatchAbilitiesGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Overwatch Abilities Configuration")

        self.overwatch_abilities = {}
        self.load_config()

        self.create_widgets()

    def create_widgets(self):
        # Create a tabbed view for adding abilities and showing the saved data
        self.tab_control = ttk.Notebook(self.master)
        self.tab_control.grid(row=0, column=0, columnspan=2)

        # Tab for adding abilities
        self.add_tab = ttk.Frame(self.tab_control)
        self.tab_control.add(self.add_tab, text="Add Abilities")
        self.create_add_tab_widgets()

        # Tab for displaying saved data
        self.display_tab = ttk.Frame(self.tab_control)
        self.tab_control.add(self.display_tab, text="Saved Data")
        self.create_display_tab_widgets()

    def create_add_tab_widgets(self):
        # Labels and entry fields for hero name, ability, and key
        self.hero_label = tk.Label(self.add_tab, text="Hero:")
        self.hero_label.grid(row=0, column=0, sticky="e")
        self.hero_entry = tk.Entry(self.add_tab)
        self.hero_entry.grid(row=0, column=1)

        self.ability_label = tk.Label(self.add_tab, text="Ability:")
        self.ability_label.grid(row=1, column=0, sticky="e")
        self.ability_entry = tk.Entry(self.add_tab)
        self.ability_entry.grid(row=1, column=1)

        self.key_label = tk.Label(self.add_tab, text="Key:")
        self.key_label.grid(row=2, column=0, sticky="e")
        self.key_entry = tk.Entry(self.add_tab)
        self.key_entry.grid(row=2, column=1)

        # Button to add hero abilities
        self.add_button = tk.Button(self.add_tab, text="Add Ability", command=self.add_ability)
        self.add_button.grid(row=3, columnspan=2)

    def create_display_tab_widgets(self):
        # Create a frame for each hero and their abilities
        for hero, abilities in self.overwatch_abilities.items():
            frame = ttk.Frame(self.display_tab)
            frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
            ttk.Label(frame, text=hero, font=("Arial", 12, "bold")).grid(row=0, columnspan=2)
            row = 1
            for ability, key in abilities.items():
                ttk.Label(frame, text=f"{ability}: {key}").grid(row=row, column=0, sticky="w")
                row += 1


    def load_config(self):
        try:
            with open("overwatch_config.pickle", "rb") as file:
                self.overwatch_abilities = pickle.load(file)
        except FileNotFoundError:
            messagebox.showwarning("Warning", "Config file not found. Default configuration will be used.")
            self.overwatch_abilities = {}

    def save_config(self):
        with open("overwatch_config.pickle", "wb") as file:
            pickle.dump(self.overwatch_abilities, file)
        messagebox.showinfo("Info", "Config saved successfully.")
        self.update_tab_view()

    def add_ability(self):
        hero = self.hero_entry.get()
        ability = self.ability_entry.get()
        key = self.key_option.get()

        if hero and ability and key != "Select Key":
            if hero not in self.overwatch_abilities:
                self.overwatch_abilities[hero] = {}
            if key not in self.overwatch_abilities[hero].values():
                self.overwatch_abilities[hero][ability] = KEY_CODES[key]
                messagebox.showinfo("Info", f"Ability added for {hero}: {ability} - {key}")
            else:
                messagebox.showerror("Error", "Key already assigned to another ability.")
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

        self.update_tab_view()

    def update_tab_view(self):
        for tab in self.tab_control.tabs():
            self.tab_control.forget(tab)

        for hero, abilities in self.overwatch_abilities.items():
            frame = ttk.Frame(self.tab_control)
            self.tab_control.add(frame, text=hero)
            for index, (ability, key_code) in enumerate(abilities.items(), start=1):
                tk.Label(frame, text=f"{ability}: {key_code}").grid(row=index, column=0, sticky="w")

def main():
    root = tk.Tk()
    OverwatchAbilitiesGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()