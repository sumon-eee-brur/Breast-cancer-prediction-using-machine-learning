import random
from tkinter import *
from tkinter import ttk, messagebox
import time
import tensorflow as tf
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from customtkinter import *

import customtkinter

import labels
import predicted


class Admin:
    def __init__(self, main_root):
        self.root = main_root
        self.root.title("Breast Cancer | created by Sumon Hasan")
        self.root.geometry("1350x700+0+0")
        self.root.resizable(False, False)
        self.root.iconbitmap(r"G:\python\code\basic code\project with tkinter\assets\logo.ico")

        # =========add variables===========
        self.search_option = StringVar()
        self.model_option = StringVar()
        self.search_text = StringVar()

        self.registration_id = StringVar()
        self.name = StringVar()
        self.age = StringVar()
        self.sex = StringVar()
        self.mobile = StringVar()

        self.radius_mean = StringVar()
        self.texture_mean = StringVar()
        self.perimeter_mean = StringVar()
        self.area_mean = StringVar()
        self.smoothness_mean = StringVar()
        self.compactness_mean = StringVar()
        self.concavity_mean = StringVar()
        self.concave_mean = StringVar()
        self.symmetry_mean = StringVar()
        self.fractional_mean = StringVar()

        self.radius_seq = StringVar()
        self.texture_seq = StringVar()
        self.perimeter_seq = StringVar()
        self.area_seq = StringVar()
        self.smoothness_seq = StringVar()
        self.compactness_seq = StringVar()
        self.concavity_seq = StringVar()
        self.concave_seq = StringVar()
        self.symmetry_seq = StringVar()
        self.fractional_seq = StringVar()

        self.radius_worst = StringVar()
        self.texture_worst = StringVar()
        self.perimeter_worst = StringVar()
        self.area_worst = StringVar()
        self.smoothness_worst = StringVar()
        self.compactness_worst = StringVar()
        self.concavity_worst = StringVar()
        self.concave_worst = StringVar()
        self.symmetry_worst = StringVar()
        self.fractional_worst = StringVar()

        self.status_option_box = StringVar()
        self.predicted_result = StringVar()
        self.error_sms = None
        self.value = 0

        self.random_reg_id = random.randint(10 ** 14, 10 ** 15 - 1)
        self.registration_id.set(str(self.random_reg_id))

        bg_color = "#52998e"
        font_style = "Garamond"

        title = Label(
            self.root,
            text="Breast Cancer",
            bg=bg_color,
            font=(font_style, 18),
            bd=5,
            pady=5
        )
        title.pack(fill=X)

        left_side_frame = LabelFrame(
            self.root,
            text="Actions part",
            bg=bg_color,
            font=(
                font_style,
                10
            )

        )
        left_side_frame.place(x=0, y=60, width=200, height=340)

        check_result = Button(
            left_side_frame,
            text="Check Result",
            command=self.check_result,
            font=(
                font_style,
                10
            ),
            bg=bg_color,
            fg="white",
            width=23
        )
        check_result.grid(
            row=0,
            column=0,
            padx=10,
            pady=5
        )

        demo_btn = Button(
            left_side_frame,
            text="Check with demo data",
            command=self.check_with_demo_data,
            font=(
                font_style,
                10
            ),
            bg=bg_color,
            fg="white",
            width=23
        )
        demo_btn.grid(
            row=5,
            column=0,
            padx=10,
            pady=5
        )

        clear_btn = Button(
            left_side_frame,
            text="Clear",
            command=self.clear,
            font=(
                font_style,
                10
            ),
            bg=bg_color,
            fg="white",
            width=23
        )
        clear_btn.grid(
            row=6,
            column=0,
            padx=10,
            pady=5
        )

        exit_btn = Button(
            left_side_frame,
            text="Exit",
            command=self.exit_app,
            font=(
                font_style,
                10
            ),
            bg=bg_color,
            fg="white",
            width=23
        )
        exit_btn.grid(
            row=10,
            column=0,
            padx=20,
            pady=5
        )

        right_side_frame = LabelFrame(
            self.root,
            text="Patient Info",
            bg=bg_color,
            font=(
                font_style,
                8
            )

        )
        right_side_frame.place(x=200, y=60, relwidth=1, height=340)

        search_frame = LabelFrame(
            right_side_frame,
            text="Search",
            bg=bg_color,
            font=(
                font_style,
                8
            )
        )
        search_frame.place(x=80, y=10, width=450, height=80)

        # =========options============
        option_box = ttk.Combobox(
            search_frame,
            textvariable=self.search_option,
            values=(
                "Select",
                "Username",
                "Mobile"
            ),
            font=(
                font_style,
                10
            ),
            state="readonly",
            justify=CENTER
        )
        option_box.place(
            x=10,
            y=50,
            width=100
        )
        option_box.current(0)

        option_box.grid(
            row=0,
            column=0,
            padx=10
        )

        search = Entry(
            search_frame,
            textvariable=self.search_text,
            font=(
                font_style,
                12
            ),
        )
        search.grid(
            row=0,
            column=1,
            padx=10,
            pady=10
        )
        search_btn = Button(
            search_frame,
            # command=self.search,
            text="Search",
            font=(
                font_style,
                10,
                "bold"
            ),
            cursor="hand2"
        )
        search_btn.grid(
            row=0,
            column=2,
            padx=10,
            pady=10
        )

        # ==============patient info frame============

        patient_frame = LabelFrame(
            right_side_frame,
            text="Patient info",
            bg=bg_color,
            font=(
                font_style,
                8
            )
        )
        patient_frame.place(x=550, y=10, width=550, height=80)

        labels.Labels(right_side_frame, "Name", 570, 35).label()
        labels.Entries(right_side_frame, self.name, 570, 63, width=15).entry()

        labels.Labels(right_side_frame, "Registration No", 675, 35).label()
        labels.Entries(right_side_frame, self.registration_id, 675, 63, width=20, entry_state="disabled").entry()

        labels.Labels(right_side_frame, "Age", 810, 35).label()
        labels.Entries(right_side_frame, self.age, 810, 63, width=10).entry()

        labels.Labels(right_side_frame, "Sex", 890, 35).label()
        labels.Entries(right_side_frame, self.sex, 890, 63, width=10).entry()

        labels.Labels(right_side_frame, "Phone", 960, 35).label()
        labels.Entries(right_side_frame, self.mobile, 960, 63, width=20).entry()

        # ========user label===================

        user_label = Label(
            right_side_frame,
            text="Report Details",
            font=(
                font_style,
                10
            ),
            bg="#000000",
            fg="white"
        )
        user_label.place(
            x=30,
            y=100,
            width=1100,
            height=20
        )
        # =================user id ================

        labels.Labels(right_side_frame, "Radius mean", 30, 130).label()
        labels.Entries(right_side_frame, self.radius_mean, 30, 160).entry()

        # ===============================
        labels.Labels(right_side_frame, "Texture mean", 130, 130).label()
        labels.Entries(right_side_frame, self.texture_mean, 130, 160).entry()

        # ===============================
        labels.Labels(right_side_frame, "Perimeter mean", 230, 130).label()
        labels.Entries(right_side_frame, self.perimeter_mean, 230, 160).entry()

        # ===============================
        labels.Labels(right_side_frame, "Area mean", 330, 130).label()
        labels.Entries(right_side_frame, self.area_mean, 330, 160).entry()

        # ===============================
        labels.Labels(right_side_frame, "Smoothness mean", 410, 130).label()
        labels.Entries(right_side_frame, self.smoothness_mean, 410, 160).entry()

        # ===============================
        labels.Labels(right_side_frame, "Compactness mean", 530, 130).label()
        labels.Entries(right_side_frame, self.compactness_mean, 530, 160).entry()

        # ===============================
        labels.Labels(right_side_frame, "Concavity mean", 660, 130).label()
        labels.Entries(right_side_frame, self.concavity_mean, 660, 160).entry()

        # ===============================
        labels.Labels(right_side_frame, "Concave mean", 775, 130).label()
        labels.Entries(right_side_frame, self.concave_mean, 775, 160).entry()

        # ===============================
        labels.Labels(right_side_frame, "Symmetry mean", 870, 130).label()
        labels.Entries(right_side_frame, self.symmetry_mean, 870, 160).entry()

        # ===============================
        labels.Labels(right_side_frame, "Fractal dimension mean", 970, 130).label()
        labels.Entries(right_side_frame, self.fractional_mean, 970, 160).entry()

        # ===============================
        labels.Labels(right_side_frame, "Radius seq.", 30, 200).label()
        labels.Entries(right_side_frame, self.radius_seq, 30, 230).entry()

        # ===============================
        labels.Labels(right_side_frame, "Texture seq.", 130, 200).label()
        labels.Entries(right_side_frame, self.texture_seq, 130, 230).entry()

        # ===============================
        labels.Labels(right_side_frame, "Perimeter seq.", 230, 200).label()
        labels.Entries(right_side_frame, self.perimeter_seq, 230, 230).entry()

        # ===============================
        labels.Labels(right_side_frame, "Area seq.", 330, 200).label()
        labels.Entries(right_side_frame, self.area_seq, 330, 230).entry()

        # ===============================
        labels.Labels(right_side_frame, "Smoothness seq.", 410, 200).label()
        labels.Entries(right_side_frame, self.smoothness_seq, 410, 230).entry()

        # ===============================
        labels.Labels(right_side_frame, "Compactness seq.", 530, 200).label()
        labels.Entries(right_side_frame, self.compactness_seq, 530, 230).entry()

        # ===============================
        labels.Labels(right_side_frame, "Concavity seq.", 660, 200).label()
        labels.Entries(right_side_frame, self.concavity_seq, 660, 230).entry()

        # ===============================
        labels.Labels(right_side_frame, "Concave seq.", 775, 200).label()
        labels.Entries(right_side_frame, self.concave_seq, 775, 230).entry()

        # ===============================
        labels.Labels(right_side_frame, "Symmetry seq.", 870, 200).label()
        labels.Entries(right_side_frame, self.symmetry_seq, 870, 230).entry()

        # ===============================
        labels.Labels(right_side_frame, "Fractal dimension seq.", 970, 200).label()
        labels.Entries(right_side_frame, self.fractional_seq, 970, 230).entry()

        # ===============================
        labels.Labels(right_side_frame, "Radius worst", 30, 265).label()
        labels.Entries(right_side_frame, self.radius_worst, 30, 290).entry()

        # ===============================
        labels.Labels(right_side_frame, "Texture worst", 130, 265).label()
        labels.Entries(right_side_frame, self.texture_worst, 130, 290).entry()

        # ===============================
        labels.Labels(right_side_frame, "Perimeter worst", 230, 265).label()
        labels.Entries(right_side_frame, self.perimeter_worst, 230, 290).entry()

        # ===============================
        labels.Labels(right_side_frame, "Area worst", 330, 265).label()
        labels.Entries(right_side_frame, self.area_worst, 330, 290).entry()

        # ===============================
        labels.Labels(right_side_frame, "Smoothness worst", 410, 265).label()
        labels.Entries(right_side_frame, self.smoothness_worst, 410, 290).entry()

        # ===============================
        labels.Labels(right_side_frame, "Compactness worst", 530, 265).label()
        labels.Entries(right_side_frame, self.compactness_worst, 530, 290).entry()

        # ===============================
        labels.Labels(right_side_frame, "Concavity worst", 660, 265).label()
        labels.Entries(right_side_frame, self.concavity_worst, 660, 290).entry()

        # ===============================
        labels.Labels(right_side_frame, "Concave worst", 775, 265).label()
        labels.Entries(right_side_frame, self.concave_worst, 775, 290).entry()

        # ===============================
        labels.Labels(right_side_frame, "Symmetry worst", 870, 265).label()
        labels.Entries(right_side_frame, self.symmetry_worst, 870, 290).entry()

        # ===============================
        labels.Labels(right_side_frame, "Fractal dimension worst", 970, 265).label()
        labels.Entries(right_side_frame, self.fractional_worst, 970, 290).entry()

        # ========user data label===================

        user_data_label = Label(
            self.root,
            text="Result",
            font=(
                font_style,
                10
            ),
            bg="#000000",
            fg="white"
        )
        user_data_label.place(
            x=0,
            y=400,
            relwidth=1,
            height=20
        )

        # ========user data ================
        user_data = Frame(
            self.root,
            relief=RIDGE
        )
        user_data.place(
            x=0,
            y=420,
            relwidth=1,
            height=285
        )

        def patient_info(reg_id, name, age, sex, mobile, result):
            patient_info.config(
                text=f"Reg. No : {reg_id}\nName : {name}\nAge : {age}\nSex : {sex}\nMobile : {mobile}\nResult : {result}")
            root.after(1000 * 60 * 60 * 24 * 365, self.patient_info, reg_id, name, age, sex, mobile, result)

        self.patient_info = patient_info

        patient_info = Label(self.root, text="Patient info", justify="left", font=(font_style, 16), bg="white")
        patient_info.place(
            x=1050,
            y=440
        )

        def update_text(result, accuracy):
            report_result.config(text=f"Result : {result} \nPredicted accuracy : {accuracy}%")
            root.after(1000 * 60 * 60 * 24 * 365, self.update_text, result, accuracy)

        self.update_text = update_text

        report_result = Label(self.root, text="Report details", justify="left", font=(font_style, 16), bg="white")
        report_result.place(
            x=785,
            y=440
        )

        def create_graph(data, input_data, x_label, y_label, graph_title):
            figure, ax = plt.subplots(figsize=(4, 2))
            ax.plot(input_data, data)
            ax.set_xlabel(x_label, font=font_style)
            ax.set_ylabel(y_label, font=font_style)
            ax.set_title(graph_title, font=font_style)
            return figure

        def show_graph():
            benign_data = [8.196, 16.84, 51.71, 201.9, 0.086, 0.05943, 0.01588, 0.005917, 0.1769, 0.06503, 0.1563,
                           0.9567, 1.094, 8.205, 0.008968, 0.01646, 0.01588, 0.005917, 0.02574, 0.002582, 8.964, 21.96,
                           57.26, 242.2, 0.1297, 0.1357, 0.0688, 0.02564, 0.3105, 0.07409]

            malignant_data = [17.99, 10.38, 122.8, 1001, 0.1184, 0.2776, 0.3001, 0.1471, 0.2419, 0.07871, 1.095, 0.9053,
                              8.589,
                              153.4, 0.006399, 0.04904, 0.05373, 0.01587, 0.03003, 0.006193, 25.38, 17.33, 184.6, 2019,
                              0.1622,
                              0.6656, 0.7119, 0.2654, 0.4601, 0.1189]

            input_data = [self.radius_mean.get(), self.texture_mean.get(),
                          self.perimeter_mean.get(),
                          self.area_mean.get(), self.smoothness_mean.get(),
                          self.compactness_mean.get(),
                          self.concavity_mean.get(), self.concave_mean.get(),
                          self.symmetry_mean.get(),
                          self.fractional_mean.get(), self.radius_seq.get(),
                          self.texture_seq.get(),
                          self.perimeter_seq.get(), self.area_seq.get(),
                          self.smoothness_seq.get(),
                          self.compactness_seq.get(), self.concavity_seq.get(),
                          self.concave_seq.get(),
                          self.symmetry_seq.get(),
                          self.fractional_seq.get(), self.radius_worst.get(),
                          self.texture_worst.get(),
                          self.perimeter_worst.get(), self.area_worst.get(),
                          self.smoothness_worst.get(),
                          self.compactness_worst.get(), self.concavity_worst.get(),
                          self.concave_worst.get(),
                          self.symmetry_worst.get(), self.fractional_worst.get()]

            fig1 = create_graph(benign_data, input_data, "Input vale", "Benign data value",
                                "Benign tumor graph")
            canvas = FigureCanvasTkAgg(fig1, master=self.root)
            canvas.get_tk_widget().place(x=10, y=440)  # Adjust the position as needed
            canvas.draw()

            fig2 = create_graph(malignant_data, input_data, "Input vale", "Malignant data value",
                                "Malignant tumor graph")
            canvas = FigureCanvasTkAgg(fig2, master=self.root)
            canvas.get_tk_widget().place(x=380, y=440)  # Adjust the position as needed
            canvas.draw()

        self.show_graph = show_graph

        # ============footer =============

        footer_frame = Frame(
            self.root,
            bg=bg_color,
        )
        footer_frame.place(x=0, y=690, relwidth=1, height=35)

    # ==============call functions ==================
    def check_result(self):
        if self.name.get() != "" and self.age.get() != "" and self.sex.get() != "" and self.mobile.get() != "" and self.radius_mean.get() != "" and self.texture_mean.get() != "" and self.perimeter_mean.get() != "" and self.area_mean.get() != "" and self.smoothness_mean.get() != "" and self.compactness_mean.get() != "" and self.concavity_mean.get() != "" and self.concave_mean.get() != "" and self.symmetry_mean.get() != "" and self.fractional_mean.get() != "" and self.radius_seq.get() != "" and self.texture_seq.get() != "" and self.perimeter_seq.get() != "" and self.area_seq.get() != "" and self.smoothness_seq.get() != "" and self.compactness_seq.get() != "" and self.concavity_seq.get() != "" and self.concave_seq.get() != "" and self.symmetry_seq.get() != "" and self.fractional_seq.get() != "" and self.radius_worst.get() != "" and self.texture_worst.get() != "" and self.perimeter_worst.get() != "" and self.area_worst.get() != "" and self.smoothness_worst.get() != "" and self.compactness_worst.get() != "" and self.concavity_worst.get() != "" and self.concave_worst.get() != "" and self.symmetry_worst.get() != "" and self.fractional_worst.get() != "":
            predicted_value = predicted.PredictedClass(self.radius_mean.get(), self.texture_mean.get(),
                                                       self.perimeter_mean.get(),
                                                       self.area_mean.get(), self.smoothness_mean.get(),
                                                       self.compactness_mean.get(),
                                                       self.concavity_mean.get(), self.concave_mean.get(),
                                                       self.symmetry_mean.get(),
                                                       self.fractional_mean.get(), self.radius_seq.get(),
                                                       self.texture_seq.get(),
                                                       self.perimeter_seq.get(), self.area_seq.get(),
                                                       self.smoothness_seq.get(),
                                                       self.compactness_seq.get(), self.concavity_seq.get(),
                                                       self.concave_seq.get(),
                                                       self.symmetry_seq.get(),
                                                       self.fractional_seq.get(), self.radius_worst.get(),
                                                       self.texture_worst.get(),
                                                       self.perimeter_worst.get(), self.area_worst.get(),
                                                       self.smoothness_worst.get(),
                                                       self.compactness_worst.get(), self.concavity_worst.get(),
                                                       self.concave_worst.get(),
                                                       self.symmetry_worst.get(), self.fractional_worst.get())

            prediction, prediction_label = predicted_value.get_predict()

            if prediction_label[0] == 0:
                self.update_text("Malignant tumor", round(prediction[0][1] * 100, 2))
                result = "This is dangerous tumor"
            else:
                self.update_text("Benign tumor", round(prediction[0][1] * 100, 2))
                result = "This is normal tumor"

            self.patient_info(self.random_reg_id, self.name.get(), self.age.get(), self.sex.get(),
                              self.mobile.get(),
                              result)

            self.show_graph()

        else:
            answer = messagebox.askyesno("Alert", "Fill up all field first.")
            if answer:
                pass

    def check_with_demo_data(self):
        answer = messagebox.askyesno("Alert", "Are are want to check by demo data?")
        if answer:
            self.name.set("Rohima Begum")
            self.registration_id.set("")
            self.age.set("55")
            self.sex.set("Female")
            self.mobile.set("01929836273")

            self.radius_mean.set("15.37")
            self.texture_mean.set("22.76")
            self.perimeter_mean.set("100.2")
            self.area_mean.set("728.2")
            self.smoothness_mean.set("0.092")
            self.compactness_mean.set("0.1036")
            self.concavity_mean.set("0.1122")
            self.concave_mean.set("0.07483")
            self.symmetry_mean.set("0.1717")
            self.fractional_mean.set("0.06097")

            self.radius_seq.set("0.3129")
            self.texture_seq.set("0.8413")
            self.perimeter_seq.set("2.075")
            self.area_seq.set("29.44")
            self.smoothness_seq.set("0.009882")
            self.compactness_seq.set("0.02444")
            self.concavity_seq.set("0.04531")
            self.concave_seq.set("0.01763")
            self.symmetry_seq.set("0.02471")
            self.fractional_seq.set("0.002142")

            self.radius_worst.set("16.43")
            self.texture_worst.set("25.84")
            self.perimeter_worst.set("107.5")
            self.area_worst.set("830.9")
            self.smoothness_worst.set("0.1257")
            self.compactness_worst.set("0.1997")
            self.concavity_worst.set("0.2846")
            self.concave_worst.set("0.1476")
            self.symmetry_worst.set("0.2556")
            self.fractional_worst.set("0.06828")

            self.search_text.set("")
            self.search_option.set("Select")

            self.random_reg_id = random.randint(10 ** 14, 10 ** 15 - 1)
            self.registration_id.set(str(self.random_reg_id))

    def clear(self):
        answer = messagebox.askyesno("Alert", "Are are want to clear field?")
        if answer:
            self.name.set("")
            self.registration_id.set("")
            self.age.set("")
            self.sex.set("")
            self.mobile.set("")

            self.radius_mean.set("")
            self.texture_mean.set("")
            self.perimeter_mean.set("")
            self.area_mean.set("")
            self.smoothness_mean.set("")
            self.compactness_mean.set("")
            self.concavity_mean.set("")
            self.concave_mean.set("")
            self.symmetry_mean.set("")
            self.fractional_mean.set("")

            self.radius_seq.set("")
            self.texture_seq.set("")
            self.perimeter_seq.set("")
            self.area_seq.set("")
            self.smoothness_seq.set("")
            self.compactness_seq.set("")
            self.concavity_seq.set("")
            self.concave_seq.set("")
            self.symmetry_seq.set("")
            self.fractional_seq.set("")

            self.radius_worst.set("")
            self.texture_worst.set("")
            self.perimeter_worst.set("")
            self.area_worst.set("")
            self.smoothness_worst.set("")
            self.compactness_worst.set("")
            self.concavity_worst.set("")
            self.concavity_worst.set("")
            self.symmetry_worst.set("")
            self.fractional_worst.set("")

            self.search_text.set("")
            self.search_option.set("Select")

            self.random_reg_id = random.randint(10 ** 14, 10 ** 15 - 1)
            self.registration_id.set(str(self.random_reg_id))

        else:
            pass

    @staticmethod
    def exit_app():
        answer = messagebox.askyesno("Quit", "Are you sure to quit?")
        if answer:
            time.sleep(2)
            root.quit()
            exit(0)
        else:
            pass


if __name__ == "__main__":
    root = customtkinter.CTk()
    obj = Admin(root)
    root.mainloop()
