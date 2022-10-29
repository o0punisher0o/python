from flask import Flask, request
import requests, psycopg2









conn = psycopg2.connect("dbname=pyhon user=postgres password=LKsd25sf35df221")
cur = conn.cursor()

app = Flask(__name__)
@app.route('/form-example', methods=['GET', 'POST'])
def form_example():
    if request.method == 'POST':
        address=request.form.get('address')
        url = 'https://solana-gateway.moralis.io/nft/mainnet/' + address + '/metadata'
        headers = {
            "accept": "application/json",
            "X-API-Key": "iWXzBLaUXSfgBOJ5y8lmb9h5xAstww6nm2wkDTXOxsL1vLeoANc8njHGpnTrQWcM"
        }
        response = requests.get(url, headers=headers)
        print(response.text)

        cur.execute("""SELECT nft_info from nft WHERE nft_address = %s""", (address,))
        ans = cur.fetchall()  
        if ans==[]:
            cur.execute("INSERT INTO nft (nft_address, nft_info) VALUES (%s, %s)",(address, response.text,))

        return '''
                  <h1>The information about nft: {}</h1>'''.format(response.text)
    return '''
           <form method="POST">
               <div><label>address: <input type="text" name="address"></label></div>
               <input type="submit" value="Get Info">
           </form>'''
if __name__ == '__main__':
    app.run(debug=True, port=5000)




    