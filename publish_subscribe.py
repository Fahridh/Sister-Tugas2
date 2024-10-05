import paho.mqtt.client as mqtt

# Publish Subscribe Cocok untuk skenario real-time seperti pembaruan cuaca, di mana pesan dikirim oleh publisher
# dan diterima oleh subscriber yang berlangganan tanpa perlu berinteraksi secara langsung.
#Asinkron dan dapat diskalakan.

# Fungsi untuk menangani pesan yang diterima
def on_message(client, userdata, message):
    print(f"Weather Update: {message.payload.decode()}")

client = mqtt.Client()
client.on_message = on_message

# Menghubungkan ke broker MQTT
client.connect("test.mosquitto.org", 1883, 60)
client.subscribe("weather/update")  # Berlangganan ke topik pembaruan cuaca

client.loop_start()

# Publisher - Penerbit pembaruan cuaca
def publish_weather_update(city, weather):
    message = f"Weather in {city}: {weather}"
    client.publish("weather/update", message)

# Contoh Penggunaan - Mengirim pembaruan cuaca
publish_weather_update("New York", "Sunny, 25°C")
publish_weather_update("Los Angeles", "Cloudy, 22°C")

# Program berjalan terus hingga dihentikan manual
try:
    while True:
        pass
except KeyboardInterrupt:
    print("\nProgram stopped by user (Ctrl + C).")
    client.loop_stop()
    client.disconnect()
