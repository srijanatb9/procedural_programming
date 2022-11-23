from flask import Flask, request
import mysql.connector

connection = mysql.connector.connect(
         host='127.0.0.1',
         port=3306,
         database='flight_game',
         user='root',
         password='S0prm9oD?',
         autocommit=True
)

# 1
app = Flask(__name__)

@app.route('/prime_num/<number>')
def prime_number(number):
    isPrime = True
    number = int(number)
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                isPrime = False
                break

    response = {
        "isPrime": isPrime,
        "Number": number
    }
    return response

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)


# 2

app = Flask(__name__)

@app.route('/airport/<string:icao>')
def airport(icao_code):
    sql = "SELECT name, municipality FROM airport"
    sql += " WHERE ident='" + icao_code + ";"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            name = row[0]
            town = row[1]

    response = {
        "Airport": name,
        "Location": town,
        "ICAO": icao_code
    }
    return response

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)