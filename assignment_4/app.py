import requests, psycopg2
from flask import Flask, render_template, url_for, request

conn = psycopg2.connect("dbname=pyhon user=postgres password=LKsd25sf35df221")
cur = conn.cursor()

app = Flask(__name__)


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
        return render_template('res.html', address=response.text)
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


@app.route('/user/<string:name>/<int:id>')
def user(name, id):
    return "User page: " + name + " - " + str(id)


if __name__ == "__main__":
    app.run(debug=True)



'''
address = '4Jb9EzcUd6k1gC7GSH2iu6H7UcL2ez3NgvAF8n6a1QDs'
'''