import PlotMethods as pm
import Styles as stls
import tkinter as tk


class GuiMakerClass:

    def __init__(self, url):
        """Accepts url of web page with csv and sends url to function load file in Plot Methods"""
        pm.loadFile(url)

    def create_gui(self):
        """Makes gui for plotting"""
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
        button_frame.pack(padx=10, pady=10, fill='both', expand=True)
        # button_frame.pack(fill='both', expand=True, sticky="nsew")

        button_frame.configure(bg=stls.getBackgroundColour())

        buttons = [
            ("Sessions in a Day", lambda: pm.showSessionsDuringADay(text_field.get())),
            ("Sessions in a Week", lambda: pm.showSessionsDuringAWeek(text_field.get())),
            ("Sessions in a Month", lambda: pm.showSessionsDuringAMonth(text_field.get())),
            ("Duration watched by Title", pm.showTitleToDuration),
            ("Number of episodes watched by Serial", pm.showNumOfEpisodesWatched),
            ("Number of episodes watched on Device", pm.showNumOfEpisodesWatchedByDevice),
            ("Duration watched by Country", pm.showTimeWatchedByCountry),
            ("Users count by Country", pm.showUsersCountByCountry)
        ]

        for i, (title, command) in enumerate(buttons):
            button = tk.Button(button_frame, text=title, command=command, **button_style)
            button.grid(row=i // 2, column=i % 2, padx=5, pady=5, sticky="nsew")

        window_width = 570
        window_height = 400
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        position_top = int(screen_height / 2 - window_height / 2)
        position_right = int(screen_width / 2 - window_width / 2)
        root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

        root.mainloop()

