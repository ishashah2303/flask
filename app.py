from flask import Flask, request, jsonify
import mysql.connector
app = Flask(__name__)

@app.route('/add_patient', methods=['POST'])
def add_patient():
    try:
        patient_id = request.form['patient_id']
        patient_name = request.form['patient_name']
        patient_age = request.form['patient_age']
        patient_address = request.form['patient_address']
        patient_phone = request.form['patient_phone']

        cnx = mysql.connector.connect(user='<user>', password='<password>',
                                        host='127.0.0.1',
                                        database='<database>')
        cursor = cnx.cursor()
        query = "INSERT INTO patients (patient_id, patient_name, patient_age, patient_address, patient_phone) VALUES (%s, %s, %s, %s, %s)"
        data = (patient_id, patient_name, patient_age, patient_address, patient_phone)
        cursor.execute(query, data)
        cnx.commit()
        return jsonify({'message': 'Patient added successfully!'})
    except Exception as e:
        return jsonify({'error': str(e)})
    finally:
        if 'cnx' in locals() or 'cnx' in globals():
            cnx.close()

@app.route('/get_patient', methods=['GET'])
def get_patient():
    try:
        patient_id = request.args.get('patient_id')
        cnx = mysql.connector.connect(user='<user>', password='<password>',
                                        host='127.0.0.1',
                                        database='<database>')
        cursor = cnx.cursor()
        query = "SELECT * FROM patients WHERE patient_id = %s"
        data = (patient_id,)
        cursor.execute(query, data)
        patients = cursor.fetchall()
        return jsonify({'patients': [i[0] for i in patients]})
    except Exception as e:
        return jsonify({'error': str(e)})
    finally:
        if 'cnx' in locals() or 'cnx' in globals():
            cnx.close()

if __name__ == '__main__':
    app.run(debug=True)