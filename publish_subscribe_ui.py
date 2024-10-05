import paho.mqtt.client as mqtt
import tkinter as tk
from tkinter import scrolledtext

# Fungsi untuk menangani pesan yang diterima
def on_message(client, userdata, message):
    weather_info = message.payload.decode()
    weather_display.config(state=tk.NORMAL)
    weather_display.insert(tk.END, f"{weather_info}\n")
    weather_display.config(state=tk.DISABLED)

# Fungsi untuk menghubungkan klien MQTT dan berlangganan topik
def connect_mqtt():
    client = mqtt.Client()
    client.on_message = on_message
    client.connect("test.mosquitto.org", 1883, 60)
    client.subscribe("weather/update")
    client.loop_start()

# Membuat jendela utama
root = tk.Tk()
root.title("Weather Update System")
root.geometry("400x300")

# Tampilan untuk menampilkan pembaruan cuaca
weather_display = scrolledtext.ScrolledText(root, state=tk.DISABLED)
weather_display.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

# Tombol untuk menghubungkan MQTT
connect_button = tk.Button(root, text="Connect to Weather Updates", command=connect_mqtt)
connect_button.pack(pady=20)

# Menjalankan aplikasi
root.mainloop()
