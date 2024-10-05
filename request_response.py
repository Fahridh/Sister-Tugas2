from flask import Flask, request, jsonify

app = Flask(__name__)

# Request Response Cocok untuk skenario seperti pemesanan tiket, di mana client harus
# mendapatkan respons langsung dari server tentang hasil permintaan.
# Ada sinkronisasi antara client dan server.

# Simulasi data kursi bioskop
seats = {'A1': 'available', 'A2': 'booked', 'A3': 'available'}


@app.route('/book_ticket', methods=['POST'])
def book_ticket():
    data = request.json
    seat_number = data['seat_number']

    # Memeriksa apakah kursi tersedia
    if seat_number in seats:
        if seats[seat_number] == 'available':
            seats[seat_number] = 'booked'
            response_data = {'status': 'success', 'message': f"Seat {seat_number} successfully booked!"}
        else:
            response_data = {'status': 'failed', 'message': f"Seat {seat_number} is already booked!"}
    else:
        response_data = {'status': 'failed', 'message': f"Seat {seat_number} does not exist!"}

    return jsonify(response_data)


if __name__ == '__main__':
    app.run(port=5000)
