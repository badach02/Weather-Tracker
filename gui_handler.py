import tkinter as tk
import requests

class gui():
    bgcolor = "#A5A5FF"
    
    # setup window
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Weather")
        self.window.geometry("1100x300")
        self.window.config(bg=self.bgcolor)

        self.frame_input = tk.Frame(self.window, bg=self.bgcolor)

        self.title_label = tk.Label(self.frame_input, text="Enter latitude,longitude to get weather:", font = ("Arial", 24, "bold"), bg=self.bgcolor)
        self.title_label.pack(side="left")

        self.entry_label = tk.Entry(self.frame_input)
        self.entry_label.insert(0, "42.1292,-80.0851") # default Erie coordinates
        self.entry_label.pack(side="left")

        self.frame_input.pack()

        self.go_button = tk.Button(self.window, text="Lookup weather", bg="green", command=self.grab_weather_data)
        self.go_button.pack()

        self.frame_days = tk.Frame(self.window, bg="white", height=600)

    # grab weather info from open-meteo api and make into dictionary
    def grab_weather_data(self):
        coordinates = self.entry_label.get().split(",")
        response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={coordinates[0]}&longitude={coordinates[1]}&daily=temperature_2m_max,temperature_2m_min,uv_index_max,precipitation_probability_max&temperature_unit=fahrenheit&windspeed_unit=mph&timezone=auto")
        
        if response.status_code == 200:
            data = response.json()
            self.set_forecast(data)
        else:
            print("Failed to fetch weather data")

    # iterate through the forecast and make a header with information for each day
    def set_forecast(self, data):

        # clear widget first incase weather was already searched
        for widget in self.frame_days.winfo_children():
            widget.destroy()

        # loop through each day and make header
        for day in range(len(data["daily"]["time"])):
            frame_day = tk.Frame(self.frame_days)

            title = tk.Label(frame_day, text=data["daily"]["time"][day], width=9, height=3, font = ("Arial", 16, "bold"))
            title.pack()

            temp_max = tk.Label(frame_day, text="Max temp: " + str(data["daily"]["temperature_2m_max"][day]))
            temp_max.pack()

            temp_min = tk.Label(frame_day, text="Min temp: " + str(data["daily"]["temperature_2m_min"][day]))
            temp_min.pack()

            uv_index = tk.Label(frame_day, text="UV Index: " + str(data["daily"]["uv_index_max"][day]))
            uv_index.pack()

            precip_prob = tk.Label(frame_day, text="Precipitation Chance: " + str(data["daily"]["precipitation_probability_max"][day]) + "%")
            precip_prob.pack()

            frame_day.pack(side="left")

        self.frame_days.pack(pady=10)


    
        