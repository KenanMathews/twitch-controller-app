import pickle
import tkinter as tk
from overwatch_abilites import OverwatchAbilities
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
        # For example, buttons to load and save configurations
        self.load_button = tk.Button(self.master, text="Load Config", command=self.load_config)
        self.load_button.pack()

        self.save_button = tk.Button(self.master, text="Save Config", command=self.save_config)
        self.save_button.pack()

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

def main():
    root = tk.Tk()
    OverwatchAbilitiesGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
