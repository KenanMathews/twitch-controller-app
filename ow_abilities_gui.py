import tkinter as tk
from tkinter import messagebox
import pickle
from overwatch_abilites import OverwatchAbilities

class OverwatchAbilitiesGUI:
    def __init__(self, mode='HoldKey'):
        self.root = tk.Tk()
        self.root.title("Overwatch Abilities")
        
        self.controller = OverwatchAbilities(mode)
        
        self.load_actions()

        self.create_widgets()

    def load_actions(self):
        try:
            with open("overwatch_actions.pickle", "rb") as file:
                self.controller.actions = pickle.load(file)
        except FileNotFoundError:
            self.controller.actions = {}

    def save_actions(self):
        with open("overwatch_actions.pickle", "wb") as file:
            pickle.dump(self.controller.actions, file)

    def create_widgets(self):
        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=10, pady=10)

        self.action_label = tk.Label(self.frame, text="Action:")
        self.action_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.action_entry = tk.Entry(self.frame)
        self.action_entry.grid(row=0, column=1, padx=5, pady=5)

        self.key_label = tk.Label(self.frame, text="Key:")
        self.key_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

        self.key_entry = tk.Entry(self.frame)
        self.key_entry.grid(row=1, column=1, padx=5, pady=5)

        self.add_button = tk.Button(self.frame, text="Add Action", command=self.add_action)
        self.add_button.grid(row=2, columnspan=2, padx=5, pady=5)

        self.display_button = tk.Button(self.frame, text="Display Actions", command=self.display_actions)
        self.display_button.grid(row=3, columnspan=2, padx=5, pady=5)

        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def add_action(self):
        action_name = self.action_entry.get()
        key = self.key_entry.get()

        if action_name and key:
            self.controller.add_action(action_name, key)
            messagebox.showinfo("Success", "Action added successfully.")
            self.action_entry.delete(0, tk.END)
            self.key_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please enter action name and key.")

    def display_actions(self):
        actions = "\n".join([f"{action}: {key}" for action, key in self.controller.actions.items()])
        if actions:
            messagebox.showinfo("Actions", actions)
        else:
            messagebox.showinfo("Actions", "No actions found.")

    def on_close(self):
        self.save_actions()
        self.root.destroy()

if __name__ == "__main__":
    OverwatchAbilitiesGUI().root.mainloop()
