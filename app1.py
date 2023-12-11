from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

patients = {}
doctors = {}
rooms = {}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/patient', methods=['GET', 'POST'])
def patient():
    if request.method == 'POST':
        id = request.form['id']
        name = request.form['name']
        age = request.form['age']
        sex = request.form['sex']
        ailment = request.form['ailment']
        assigned_room = request.form['assigned_room']
        assigned_doctor = request.form['assigned_doctor']

        patients[id] = (name, age, sex, ailment, assigned_room, assigned_doctor)
        return redirect(url_for('patient'))
    return render_template('patient.html', patients=patients)

@app.route('/doctor', methods=['GET', 'POST'])
def doctor():
    if request.method == 'POST':
        id = request.form['id']
        name = request.form['name']
        specialization = request.form['specialization']
        doctor_rooms = request.form.getlist('doctor_rooms')

        doctors[id] = (name, specialization, doctor_rooms)
        return redirect(url_for('doctor'))
    return render_template('doctor.html', doctors=doctors)

@app.route('/room', methods=['GET', 'POST'])
def room():
    if request.method == 'POST':
        id = request.form['id']
        room_number = request.form['room_number']
        room_type = request.form['room_type']
        beds = request.form['beds']

        rooms[id] = (room_number, room_type, beds)
        return redirect(url_for('room'))
    return render_template('room.html', rooms=rooms)

if __name__ == '__main__':
    app.run(debug=True)