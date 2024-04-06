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
        # Labels and entry fields for hero name and ability
        self.hero_label = tk.Label(self.add_tab, text="Hero:")
        self.hero_label.grid(row=0, column=0, sticky="e", padx=5, pady=5)
        self.hero_entry = tk.Entry(self.add_tab)
        self.hero_entry.grid(row=0, column=1, padx=5, pady=5)

        self.ability_label = tk.Label(self.add_tab, text="Ability:")
        self.ability_label.grid(row=1, column=0, sticky="e", padx=5, pady=5)
        self.ability_entry = tk.Entry(self.add_tab)
        self.ability_entry.grid(row=1, column=1, padx=5, pady=5)

        self.key_label = tk.Label(self.add_tab, text="Key:")
        self.key_label.grid(row=1, column=2, sticky="e", padx=5, pady=5)
        self.selected_key = tk.StringVar(self.add_tab)
        self.selected_key.set("Select Key")
        self.key_option_menu = tk.OptionMenu(self.add_tab, self.selected_key, *KEY_CODES.keys())
        self.key_option_menu.grid(row=1, column=3, padx=5, pady=5)

        # Button to add more ability and key fields
        self.add_more_button = tk.Button(self.add_tab, text="Add More Abilities", command=self.add_more_fields)
        self.add_more_button.grid(row=2, column=1, columnspan=2, pady=5)

        # Button to add ability
        self.add_button = tk.Button(self.add_tab, text="Add Ability", command=self.add_ability)
        self.add_button.grid(row=3, column=1, columnspan=2, pady=10)

    def add_more_fields(self):
        # Add additional ability and key fields
        row_num = len(self.add_tab.grid_slaves()) // 2
        ability_label = tk.Label(self.add_tab, text="Ability:")
        ability_label.grid(row=row_num, column=0, sticky="e", padx=5, pady=5)
        ability_entry = tk.Entry(self.add_tab)
        ability_entry.grid(row=row_num, column=1, padx=5, pady=5)

        key_label = tk.Label(self.add_tab, text="Key:")
        key_label.grid(row=row_num, column=2, sticky="e", padx=5, pady=5)
        selected_key = tk.StringVar(self.add_tab)
        selected_key.set("Select Key")
        key_option_menu = tk.OptionMenu(self.add_tab, selected_key, *KEY_CODES.keys())
        key_option_menu.grid(row=row_num, column=3, padx=5, pady=5)

        self.add_more_button.grid(row=row_num + 1, column=1, columnspan=2, pady=5)
        self.add_button.grid(row=row_num + 2, column=1, columnspan=2, pady=10)





    def add_ability(self):
        hero = self.hero_entry.get()
        abilities = []
        keys = []

        # Collect all abilities and keys entered by the user
        abilities.append(self.ability_entry.get())
        keys.append(self.selected_key.get())  # Change to use selected_key instead of key_entry

        for widget in self.add_tab.grid_slaves():
            if isinstance(widget, tk.Entry):
                if widget != self.ability_entry and widget != self.selected_key:  # Adjusted condition
                    if widget.grid_info()["row"] % 2 == 0:  # Ability entry
                        abilities.append(widget.get())
                    else:  # Key entry
                        keys.append(widget.get())

        # Check if all fields are filled
        if hero and all(abilities) and all(keys) and "Select Key" not in keys:
            if hero:
                if hero not in self.overwatch_abilities:
                    self.overwatch_abilities[hero] = {}
                for ability, key in zip(abilities, keys):
                    if key in KEY_CODES:
                        if key not in self.overwatch_abilities[hero].values():
                            self.overwatch_abilities[hero][ability] = KEY_CODES[key]
                            self.save_config()
                        else:
                            messagebox.showerror("Error", f"Key {key} already assigned to another ability.")
                    else:
                        messagebox.showerror("Error", f"Invalid key: {key}. Please use keys from KEY_CODES.")
                messagebox.showinfo("Info", f"Abilities added for {hero}: {', '.join(abilities)}")
                self.update_tab_view()
            else:
                messagebox.showerror("Error", "Please fill in Hero field.")
        else:
            messagebox.showerror("Error", "Please fill in all fields.")



    def create_display_tab_widgets(self):
        # Counter for positioning frames horizontally and vertically
        column_counter = 0
        row_counter = 0
        
        # Create a frame for each hero and their abilities
        for hero, abilities in self.overwatch_abilities.items():
            frame = ttk.Frame(self.display_tab)
            frame.grid(row=row_counter, column=column_counter, padx=10, pady=10, sticky="nsew")
            ttk.Label(frame, text=hero, font=("Arial", 12, "bold")).grid(row=0, columnspan=2)
            row = 1
            for ability, key in abilities.items():
                ttk.Label(frame, text=f"{ability}: {find_key_by_value(key,KEY_CODES)}").grid(row=row, column=0, sticky="w")
                row += 1
            
            # Increment the column counter, and move to the next row if we've reached 5 columns
            column_counter += 1
            if column_counter == 4:
                column_counter = 0
                row_counter += 1

        # Set the column weight to make the frames take up equal space
        for i in range(4):
            self.display_tab.grid_columnconfigure(i, weight=1)

        # Set the max width of the root window to 800 pixels
        self.master.geometry("800x600")

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

    def update_tab_view(self):
        for tab in self.tab_control.tabs():
            self.tab_control.forget(tab)

        for hero, abilities in self.overwatch_abilities.items():
            frame = ttk.Frame(self.tab_control)
            self.tab_control.add(frame, text=hero)
            for index, (ability, key_code) in enumerate(abilities.items(), start=1):
                tk.Label(frame, text=f"{ability}: {find_key_by_value(key_code,KEY_CODES)}").grid(row=index, column=0, sticky="w")
def find_key_by_value(value, key_codes):
    for key, val in key_codes.items():
        if val == value:
            return key
    return None

def main():
    root = tk.Tk()
    OverwatchAbilitiesGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()