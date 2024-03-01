from customtkinter import *
from tkcalendar import Calendar
from tkinter import *

custom_font = ('Times New Roman', 16)
custom1_font = ('Times New Roman', 14, "bold")

class todo:
    def __init__(self, root):
        self.root = root
        self.root.configure(bg="light blue")
        self.root.title("To-Do List")
        self.root.geometry("700x480")
        self.root.resizable(False, False)

        self.tasks = self.load_tasks()  # Calling the load_tasks function
        self.list1 = Listbox(root, height=25, width=50, font=custom_font, highlightbackground="#98F5FF",
                             highlightcolor="#98F5FF", background="#262626")
        self.list1.place(x=400, y=60)

        def get_data():
            # Get the dates from the calendar
            dates = cal.get_date()
            text_data = t1.get("1.0", END).strip()  # Get the tasks from the List box
            priority = combobox.get()  # Get the priority from the combobox
            self.list1.insert(END, f"{dates}:{text_data}:{priority}"+'\n')  # simply inserting in list box
            t1.delete("1.0", END)
        def remove_task():
            # Get the index of the selected item
            selected_index = self.list1.curselection()
            if selected_index:  # Check if an item is selected
                index = int(selected_index[0])  # Get the index of the selected item
                self.list1.delete(index)

        t1 = CTkTextbox(root, width=200, height=150, bg_color='transparent', font=custom_font, border_width=2,
                        border_color="#98F5FF")
        t1.place(x=25, y=35)

        label2 = CTkLabel(root, text="Text Box", width=0, height=28, text_color="#F0FFFF", font=custom1_font)
        label2.place(x=100, y=7)

        b1 = CTkButton(root, text="Add Task", command=get_data, width=120, height=28, corner_radius=70,
                       border_width=2, border_color="#98F5FF", text_color="white", font=custom1_font,
                       hover_color="black")
        b1.place(x=5, y=450)

        label1 = CTkLabel(root, text="List View", width=0, height=28, text_color="#F0FFFF", font=custom1_font)
        label1.place(x=440, y=10)

        cal = Calendar(root, selectmode="day", date_pattern="yyyy-mm-dd", background="black", bordercolor="#98F5FF",
                       foreground="#98F5FF")
        cal.place(x=60, y=300)

        combobox = CTkComboBox(root, width=140, height=28, values=["High", "Medium", "Low"], text_color="#98F5FF",
                               dropdown_text_color="#98F5FF")
        combobox.place(x=54, y=337)

        remove_button = CTkButton(root, text="Remove Task", command=remove_task, font=custom1_font, width=120,
                                  height=28,
                                  border_width=2, corner_radius=70, border_color="#98F5FF", text_color="white",
                                  hover_color="black")
        remove_button.place(x=140, y=450)

        self.display_tasks()
        root.protocol("WM_DELETE_WINDOW", self.save_tasks_on_exit)

    def load_tasks(self):
        # Here accessing the file or data stored in the system.
        try:
            with open("tasks.txt", "r") as file:
                tasks = file.readlines()
                # Here split the complete lines into single line and strip each line
                tasks = [task.strip() for task in tasks]
            return tasks
        except FileNotFoundError:
            return []

    def display_tasks(self):
        # Here after accessed tasks are inserting into list box.
        for task in self.tasks:
            self.list1.insert(0, task)

    def save_tasks(self):
        # Here this is the add task to save in the text file.
        self.tasks = [self.list1.get(idx) for idx in range(self.list1.size())]
        with open("tasks.txt", "w") as file:
            # Here adding the task in text file
            file.write("\n".join(self.tasks))
    def save_tasks_on_exit(self):
        # Here save the all added task in our file.
        self.save_tasks()
        self.root.destroy()  # destroys the root window

def main():
    root = CTk()
    todo(root)
    root.mainloop()

if __name__ == "__main__":
    main()