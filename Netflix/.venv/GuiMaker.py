import PlotMethods as pm
import Styles as stls
import tkinter as tk
from tkinter import messagebox


class GuiMakerClass:


    def __init__(self, url):
        pm.loadFile(url)



    def create_gui(self):
        root = tk.Tk()
        root.title("Netflix Plotter")

        root.configure(bg=stls.getBackgroundColour())

        button_style = stls.getButtonStyle()

        text_field_style = stls.getTextFieldStyle()

        text_frame = tk.Frame(root, bg=stls.getBackgroundColour(), padx=20, pady=20)
        text_frame.pack(fill='x', pady=(20, 7))


        text_field = tk.Entry(text_frame, **text_field_style)
        text_field.pack(fill='x', pady=7)


        button_frame = tk.Frame(root, padx=20, pady=20)
        button_frame.pack(fill='both', expand=True)

        button_frame.configure(bg=stls.getBackgroundColour())

        plot_button_DT = tk.Button(button_frame, text="Duration watched by Title", command=pm.showTitleToDuration, **button_style)
        plot_button_DT.pack(pady=7)

        plot_button_ES = tk.Button(button_frame, text="Number of episodes watched by Serie", command=pm.showNumOfEpisodesWatched, **button_style)
        plot_button_ES.pack(pady=7)

        plot_button_ED = tk.Button(button_frame, text="Number of episodes watched on Device", command=pm.showNumOfEpisodesWatchedByDevice, **button_style)
        plot_button_ED.pack(pady=7)

        plot_button_DC = tk.Button(button_frame, text="Duration watched by Country", command=pm.showTimeWatchedByCountry, **button_style)
        plot_button_DC.pack(pady=7)

        plot_button_PC = tk.Button(button_frame, text="Users count by Country", command=pm.showUsersCountByCountry, **button_style)
        plot_button_PC.pack(pady=7)


        window_width = 400
        window_height = 420
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        position_top = int(screen_height / 2 - window_height / 2)
        position_right = int(screen_width / 2 - window_width / 2)
        root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

        root.mainloop()

