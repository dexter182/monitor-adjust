from tkinter import *
from tkinter import ttk
from monitorcontrol import get_monitors


# Get current monitor values
for monitor in get_monitors():
    with monitor:
        print(monitor.get_vcp_capabilities())


class FeetToMeters:

    def __init__(self, root):




        root.title("Monitor")

        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
       

        # Luminance
        luminance_title_label = ttk.Label(mainframe, text="亮度:")
        luminance_title_label.grid(column=1, row=2, sticky=(W, E))
        luminance_current_number = IntVar()
        luminance_number_label = ttk.Label(mainframe, textvariable=luminance_current_number)
        luminance_number_label.grid(column=3, row=2, sticky=(W, E))

        def update_luminance(val):
            new_num = round(float(val))
            luminance_current_number.set(new_num)
            for monitor in get_monitors():
                with monitor:
                    monitor.set_luminance(new_num)
        luminance_bar_entry = ttk.Scale(mainframe, orient=HORIZONTAL, length=300, from_=1, to=100, 
            variable=luminance_current_number, command=update_luminance)
        luminance_bar_entry.grid(column=2, row=2, sticky=(W, E))


        # Contrast
        contrast_title_label = ttk.Label(mainframe, text="对比度:")
        contrast_title_label.grid(column=1, row=4, sticky=(W, E))
        contrast_current_number = IntVar()
        contrast_number_label = ttk.Label(mainframe, textvariable=contrast_current_number)
        contrast_number_label.grid(column=3, row=4, sticky=(W, E))
        # contrast_current_number.setvar("0")
        def update_contrast(val):
            new_num = round(float(val))
            contrast_current_number.set(new_num)
            for monitor in get_monitors():
                with monitor:
                    monitor.set_contrast(new_num)
        contrast_bar_entry = ttk.Scale(mainframe, orient=HORIZONTAL, length=300, from_=1, to=100, 
            variable=contrast_current_number, command=update_contrast)
        contrast_bar_entry.grid(column=2, row=4, sticky=(W, E))

        # bar_entry.focus()
        # root.bind("<Return>", self.calculate)
        
    # def calculate(self, *args):
    #     try:
    #         value = float(self.feet.get())
    #         self.meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
    #     except ValueError:
    #         pass

root = Tk()
FeetToMeters(root)
root.mainloop()