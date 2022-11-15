from tkinter import *
from tkinter import ttk
from monitorcontrol import get_monitors


# Get current monitor values
monitors = []
for monitor in get_monitors():
    monitors.append(monitor)
for m in monitors:
    with m:
        print(m.get_vcp_capabilities())



class MonitorWidget:
    def __init__(self, monitor, frame, start_row):
        isInternal = False
        monitor_name = ""
        first_luminance = 0
        first_contrast = 0
        with monitor:
            monitor_info = monitor.get_vcp_capabilities()
            monitor_name = monitor_info['type'] + "-" + monitor_info['model']
            monitor_name = monitor_name.strip()
            first_luminance = monitor.get_luminance()
            first_contrast = monitor.get_contrast()
        if monitor_name == '-':
            monitor_name = "internal-monitor"
            isInternal = True
        
        # Empty row
        placeholder_label = ttk.Label(frame, text="")
        placeholder_label.grid(column=2, row=start_row, sticky=(W, E))

        # Monitor name label
        monitor_name_label = ttk.Label(frame, text=monitor_name)
        monitor_name_label.grid(column=2, row=start_row + 1, sticky=(W, E))

        # Luminance
        luminance_title_label = ttk.Label(frame, text="亮度:")
        luminance_title_label.grid(column=1, row=start_row + 2, sticky=(W, E))
        luminance_current_number = IntVar()
        luminance_current_number.set(first_luminance)
        luminance_number_label = ttk.Label(frame, textvariable=luminance_current_number)
        luminance_number_label.grid(column=3, row=start_row + 2, sticky=(W, E))

        def update_luminance(val):
            new_num = round(float(val))
            luminance_current_number.set(new_num)
            with monitor:
                monitor.set_luminance(new_num)
        luminance_bar_entry = ttk.Scale(frame, orient=HORIZONTAL, length=300, from_=1, to=100, 
            variable=luminance_current_number, command=update_luminance)
        luminance_bar_entry.grid(column=2, row=start_row + 2, sticky=(W, E))


        # Contrast
        contrast_title_label = ttk.Label(frame, text="对比度:")
        contrast_title_label.grid(column=1, row=start_row + 3, sticky=(W, E))
        contrast_current_number = IntVar()
        contrast_current_number.set(first_contrast)
        contrast_number_label = ttk.Label(frame, textvariable=contrast_current_number)
        contrast_number_label.grid(column=3, row=start_row + 3, sticky=(W, E))
        # contrast_current_number.setvar("0")
        def update_contrast(val):
            new_num = round(float(val))
            contrast_current_number.set(new_num)
            with monitor:
                monitor.set_contrast(new_num)
        contrast_bar_entry = ttk.Scale(frame, orient=HORIZONTAL, length=300, from_=1, to=100, 
            variable=contrast_current_number, command=update_contrast)
        contrast_bar_entry.grid(column=2, row=start_row + 3, sticky=(W, E))

        if isInternal:
            luminance_bar_entry.config(state=DISABLED)
            contrast_bar_entry.config(state=DISABLED)





class FeetToMeters:

    def __init__(self, root):




        root.title("Monitor")

        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
       
        start_row = 1
        for m in monitors:
            MonitorWidget(m, mainframe, start_row)
            start_row += 5

        # Empty row at the bottom
        placeholder_label = ttk.Label(mainframe, text="")
        placeholder_label.grid(column=2, row=start_row + 1, sticky=(W, E))

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