import requests
import tkinter as tk
from tkinter import messagebox

# URL dari server Flask
SERVER_URL = "http://127.0.0.1:5000/book_ticket"


# Fungsi untuk memesan tiket
def book_ticket():
    seat_number = seat_entry.get()

    # Mengirim permintaan POST ke server
    response = requests.post(SERVER_URL, json={"seat_number": seat_number})

    # Menampilkan respons dari server
    response_data = response.json()
    messagebox.showinfo("Response", response_data['message'])


# Membuat jendela utama
root = tk.Tk()
root.title("Ticket Booking System")
root.geometry("300x200")

# Label dan entry untuk nomor kursi
tk.Label(root, text="Enter Seat Number:").pack(pady=10)
seat_entry = tk.Entry(root)
seat_entry.pack(pady=10)

# Tombol untuk memesan tiket
book_button = tk.Button(root, text="Book Ticket", command=book_ticket)
book_button.pack(pady=20)

# Menjalankan aplikasi
root.mainloop()
