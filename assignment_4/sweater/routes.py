import requests, psycopg2
from flask import Flask, render_template, url_for, request

from sweater import conn, cur, app


@app.route('/nft')
def nft():
    return render_template('nft.html')


@app.route("/res", methods=['POST', "GET"])
def result():
    output = request.form.to_dict()
    address = output["address"]
    url = 'https://solana-gateway.moralis.io/nft/mainnet/' + address + '/metadata'
    headers = {
        "accept": "application/json",
        "X-API-Key": "SWnpmagdLrYt67aFhsaBRRzoubD59cdQkydkZLeljvVREBpWGmpLktfRLZXcvudp"
    }
    response = requests.get(url, headers=headers)
    cur.execute("""SELECT * from nft WHERE nft_address = %s""", (address,))
    answer = cur.fetchall()
    if answer!=[]:
        for row in answer:
            print('nft_address - ', row[0])
            print('nft_info - ', row[1])
            print('fromDB')
        return render_template('res2.html', address=response.text)
    else:
        cur.execute("""INSERT INTO nft (nft_address, nft_info) VALUES (%s, %s);""", (address, response.text))
        conn.commit()
        print('added to db')
        return render_template('res.html', address=response.text)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/sign')
def sign():
    return render_template("sign_in.html")


@app.route('/signres', methods=['POST', "GET"])
def sign_res():
    output = request.form.to_dict()
    name = output["namereg"]
    email = output["emailreg"]
    password = output["passreg"]
    cur.execute("""SELECT * from users WHERE user_name = %s""", (name,))
    answer1 = cur.fetchall()
    if answer1!=[]:
        return render_template("sign_res.html", answer381="User with this name is already registered")
    else:
        cur.execute("""INSERT INTO users (user_name, user_email, user_password) VALUES (%s, %s, %s);""", (name, email, password))
        conn.commit()
        return render_template('sign_res.html', answer381="registration completed successfully")


@app.route('/log')
def log():
    return render_template("log_in.html")


@app.route('/profile')
def prof():
    return render_template("profile.html")


@app.route('/user/<string:name>/<string:password>')
def user(name, password):
    return "User page: " + name + " - " + password


