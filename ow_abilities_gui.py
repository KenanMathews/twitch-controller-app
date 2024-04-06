import pickle
import tkinter as tk
from overwatch_abilities import OverwatchAbilities
from tkinter import messagebox

class OverwatchAbilitiesGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Overwatch Abilities Configuration")
        self.overwatch_abilities = OverwatchAbilities()
        
        # Load the configuration from the pickle file
        try:
            self.overwatch_abilities.load_config("overwatch_config.pickle")
        except FileNotFoundError:
            messagebox.showwarning("Warning", "Config file not found. Default configuration will be used.")
        
        self.create_widgets()

    def create_widgets(self):
        # Create and place GUI components
        self.hero_label = tk.Label(self.master, text="Select Hero:")
        self.hero_label.pack()

        self.hero_combobox = tk.StringVar()
        self.hero_combobox.set("Tracer")  # Default selection
        self.hero_optionmenu = tk.OptionMenu(self.master, self.hero_combobox, "Tracer", "Reaper", "Genji")
        self.hero_optionmenu.pack()

        self.show_config_button = tk.Button(self.master, text="Show Config", command=self.show_config)
        self.show_config_button.pack()

        self.load_button = tk.Button(self.master, text="Load Config", command=self.load_config)
        self.load_button.pack()

        self.save_button = tk.Button(self.master, text="Save Config", command=self.save_config)
        self.save_button.pack()

        self.config_text = tk.Text(self.master, height=10, width=50)
        self.config_text.pack()

    def load_config(self):
        # Load the configuration from the pickle file
        try:
            self.overwatch_abilities.load_config("overwatch_config.pickle")
            messagebox.showinfo("Info", "Config loaded successfully.")
        except FileNotFoundError:
            messagebox.showerror("Error", "Config file not found.")
    
    def save_config(self):
        # Save the configuration to the pickle file
        try:
            self.overwatch_abilities.save_config("overwatch_config.pickle")
            messagebox.showinfo("Info", "Config saved successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Error occurred while saving config: {e}")

    def show_config(self):
        # Display the loaded configuration
        config_text = ""
        for hero, abilities in self.overwatch_abilities.hero_abilities.items():
            config_text += f"{hero} Abilities:\n"
            for ability, key in abilities.items():
                config_text += f"- {ability}: {key}\n"
            config_text += "\n"
        self.config_text.delete(1.0, tk.END)
        self.config_text.insert(tk.END, config_text)

def main():
    root = tk.Tk()
    OverwatchAbilitiesGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()