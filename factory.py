import tkinter as tk
from tkinter import filedialog
import tkinter.messagebox as msg
import configparser as cp
import ComponentsFactory as comp
import ntpath

comp_type_init = ""
components = []

class CentralForm(tk.Toplevel):
    def __init__(self, master, my_height=250):
        super().__init__()
        self.master = master

        master_pos_x = self.master.winfo_x()
        master_pos_y = self.master.winfo_y()

        master_width = self.master.winfo_width()
        master_height = self.master.winfo_height()

        my_width = 300

        pos_x = (master_pos_x + (master_width // 2)) - (my_width // 2)
        pos_y = (master_pos_y + (master_height // 2)) - (my_height // 2)

        geometry = "{}x{}+{}+{}".format(my_width, my_height, pos_x, pos_y)
        self.geometry(geometry)


class AddSectionForm(CentralForm):
    def __init__(self, master):
        super().__init__(master)

        self.title("Add New Component")

        self.main_frame = tk.Frame(self, bg="lightgrey")
        self.text_label = tk.Label(self.main_frame, text="Text", bg="lightgrey", fg="black")
        self.text_entry = tk.Entry(self.main_frame, bg="white", fg="black")
        self.width_label = tk.Label(self.main_frame, text="Width", bg="lightgrey", fg="black")
        self.width_entry = tk.Entry(self.main_frame, bg="white", fg="black")
        self.height_label = tk.Label(self.main_frame, text="Height", bg="lightgrey", fg="black")
        self.height_entry = tk.Entry(self.main_frame, bg="white", fg="black")
        self.x_pos_label = tk.Label(self.main_frame, text="X-Position", bg="lightgrey", fg="black")
        self.x_pos_entry = tk.Entry(self.main_frame, bg="white", fg="black")
        self.y_pos_label = tk.Label(self.main_frame, text="Y-Position", bg="lightgrey", fg="black")
        self.y_pos_entry = tk.Entry(self.main_frame, bg="white", fg="black")
        self.submit_button = tk.Button(self.main_frame, text="Create", command=self.create_section)

        self.main_frame.pack(expand=1, fill=tk.BOTH)
        self.text_label.pack(side=tk.TOP, fill=tk.X)
        self.text_entry.pack(side=tk.TOP, fill=tk.X, padx=10)
        self.width_label.pack(side=tk.TOP, fill=tk.X)
        self.width_entry.pack(side=tk.TOP, fill=tk.X, padx=10)
        self.height_label.pack(side=tk.TOP, fill=tk.X)
        self.height_entry.pack(side=tk.TOP, fill=tk.X, padx=10)
        self.x_pos_label.pack(side=tk.TOP, fill=tk.X)
        self.x_pos_entry.pack(side=tk.TOP, fill=tk.X, padx=10)
        self.y_pos_label.pack(side=tk.TOP, fill=tk.X)
        self.y_pos_entry.pack(side=tk.TOP, fill=tk.X, padx=10)
        self.submit_button.pack(side=tk.TOP, fill=tk.X, pady=(10, 0), padx=10)

    def create_section(self):
        text = self.text_entry.get()
        width = self.width_entry.get()
        height = self.height_entry.get()
        x_pos = self.x_pos_entry.get()
        y_pos = self.y_pos_entry.get()
        print(comp_type_init)
        comp_type = comp_type_init
        new_comp = comp.ComponentsFactory.create_component(comp_type, width, height, text, x_pos, y_pos)
        print('Width is {0} of a {1}'.format(new_comp.get_text(), comp_type))

        test = "Type: " + comp_type + "\n Width: " + "\n Height: " + height + "\n Text: " + text + "\n X-Pos: " + x_pos + "\n Y-Pos: " + y_pos
        text = comp_type + ", " + text + ", " + width + ",\n " + height + ", " + x_pos + ", " + y_pos
        components.append(new_comp)
        ini_editor.section_select.insert(0, text)
        return new_comp


class IniEditor(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("UI Creator")
        self.geometry("800x600")

        self.html_file = open("file.html", "w")
        # SAVE AS JAVAFX APP
        self.javafx_file = open("file.fx", "w")
        self.component = "button"
        self.width = "100%"
        self.height = "20px"
        self.x = "0"
        self.y = "0"

        self.ini_elements = []

        self.menubar = tk.Menu(self, bg="lightgrey", fg="black")

        self.file_menu = tk.Menu(self.menubar, tearoff=0, bg="lightgrey", fg="black")
        self.file_menu.add_command(label="New", command=self.file_new, accelerator="Ctrl+N")
        # self.file_menu.add_command(label="Open", command=self.file_open, accelerator="Ctrl+O")
        self.file_menu.add_command(label="Save", command=self.file_save, accelerator="Ctrl+S")

        self.menubar.add_cascade(label="File", menu=self.file_menu)

        self.config(menu=self.menubar)

        self.left_frame = tk.Frame(self, width=200, bg="grey")
        self.left_frame.pack_propagate(0)

        self.right_frame = tk.Frame(self, width=400, bg="lightgrey")
        self.right_frame.pack_propagate(0)

        self.file_name_var = tk.StringVar(self)
        self.file_name_label = tk.Label(self, textvar=self.file_name_var, fg="black", bg="white", font=(None, 12))
        self.file_name_label.pack(side=tk.TOP, expand=1, fill=tk.X, anchor="n")

        self.section_select = tk.Listbox(self.left_frame, selectmode=tk.SINGLE)
        self.section_select.configure(exportselection=False)
        self.section_select.pack(expand=1)
        self.section_select.bind("<<ListboxSelect>>", self.display_section_contents)

        self.section_add_button = tk.Button(self.left_frame, text="Add Button", command=self.button_add_section_form)
        self.section_add_button.pack(pady=(0, 20))

        self.section_add_button = tk.Button(self.left_frame, text="Add Textbox", command=self.textbox_add_section_form)
        self.section_add_button.pack(pady=(0, 20))

        self.section_add_button = tk.Button(self.left_frame, text="Add Label", command=self.label_add_section_form)
        self.section_add_button.pack(pady=(0, 20))

        self.section_add_button = tk.Button(self.left_frame, text="Add Canvas", command=self.canvas_add_section_form)
        self.section_add_button.pack(pady=(0, 20))

        self.left_frame.pack(side=tk.LEFT, fill=tk.BOTH)
        self.right_frame.pack(side=tk.LEFT, expand=1, fill=tk.BOTH)

        self.right_frame.bind("<Configure>", self.frame_height)

        self.bind("<Control-n>", self.file_new)
        # self.bind("<Control-o>", self.file_open)
        self.bind("<Control-s>", self.file_save)

    def button_add_section_form(self):
        global comp_type_init
        comp_type_init = "Button"
        AddSectionForm(self)

    def textbox_add_section_form(self):
        global comp_type_init
        comp_type_init = "TextBox"
        AddSectionForm(self)

    def label_add_section_form(self):
        global comp_type_init
        comp_type_init = "Label"
        AddSectionForm(self)

    def canvas_add_section_form(self):
        global comp_type_init
        comp_type_init = "Canvas"
        AddSectionForm(self)

    def add_section(self, section_name):
        self.active_ini[section_name] = {}
        self.populate_section_select_box()

    def frame_height(self, event=None):
        new_height = self.winfo_height()
        self.right_frame.configure(height=new_height)

    def file_new(self, event=None):
        self.ini_elements = []

    def file_save(self, event=None):
        self.writeHTML()
        self.writeJavaFX()


    def writeHTML(self):
        print("WRITING TO HTML")
        self.html_file.write("<html>")
        for element in components:
            if isinstance(element, comp.ButtonComponent):
                self.html_file.write("<button style=width: %s; height: %s; top: %s; left: %s;>Text</button>" % (element.width, element.height, element.x_pos, element.y_pos))
            if isinstance(element, comp.TextBoxComponent):
                self.html_file.write("<textbox style=width: %s; height: %s; top: %s; left: %s;></textbox>" % (element.width, element.height, element.x_pos, element.y_pos))
            if isinstance(element, comp.LabelComponent):
                self.html_file.write("<label style=width: %s; height: %s; top: %s; left: %s;></label>" % (element.width, element.height,element.x_pos, element.y_pos))
            if isinstance(element, comp.CanvasComponent):
                self.html_file.write("<canvas style=width: %s; height: %s; top: %s; left: %s;></canvas>" % (element.width, element.height, element.x_pos, element.y_pos))
        self.html_file.write("</html>")
        self.html_file.close()



    def writeJavaFX(self):
        if self.component == "label":
            self.javafx_file.write(
                "Label label1 = new Label(); label1.setStyle('width: %s; height: %s; top: %s; left: %s;');" % (self.width, self.height, self.x, self.y))

        if self.component == "button":
            self.javafx_file.write(
                "Button button1 = new Button(); button1.setStyle('width: %s; height: %s; top: %s; left: %s;');" % (self.width, self.height, self.x, self.y))

    def add_item(self, item_name, item_value):
        chosen_section = self.section_select.get(self.section_select.curselection())
        self.active_ini[chosen_section][item_name] = item_value
        self.display_section_contents()

    def clear_right_frame(self):
        for child in self.right_frame.winfo_children():
            child.destroy()

    def populate_section_select_box(self):
        self.section_select.delete(0, tk.END)

        for index, section in enumerate(self.active_ini.sections()):
            self.section_select.insert(index, section)
            self.ini_elements[section] = {}
        if "DEFAULT" in self.active_ini:
            self.section_select.insert(len(self.active_ini.sections()) + 1, "DEFAULT")
            self.ini_elements["DEFAULT"] = {}

    def display_section_contents(self, event=None):

        chosen_section = self.section_select.get(self.section_select.curselection())

        for child in self.right_frame.winfo_children():
            child.pack_forget()

        for key in sorted(self.active_ini[chosen_section]):
            new_label = tk.Label(self.right_frame, text=key, font=(None, 12), bg="black", fg="white")
            new_label.pack(fill=tk.X, side=tk.TOP, pady=(10, 0))

            try:
                section_elements = self.ini_elements[chosen_section]
            except KeyError:
                section_elements = {}

            try:
                ini_element = section_elements[key]
            except KeyError:
                value = self.active_ini[chosen_section][key]

                if value.isnumeric():
                    spinbox_default = tk.IntVar(self.right_frame)
                    spinbox_default.set(int(value))
                    ini_element = tk.Spinbox(self.right_frame, from_=0, to=99999, textvariable=spinbox_default,
                                             bg="white", fg="black", justify="center")
                else:
                    ini_element = tk.Entry(self.right_frame, bg="white", fg="black", justify="center")
                    ini_element.insert(0, value)

                self.ini_elements[chosen_section][key] = ini_element

            ini_element.pack(fill=tk.X, side=tk.TOP, pady=(0, 10))

        save_button = tk.Button(self.right_frame, text="Save Changes", command=self.file_save)
        save_button.pack(side=tk.BOTTOM, pady=(0, 20))

        add_button = tk.Button(self.right_frame, text="Add Item", command=self.add_item_form)
        add_button.pack(side=tk.BOTTOM, pady=(0, 20))


if __name__ == "__main__":
    ini_editor = IniEditor()
    ini_editor.mainloop()
