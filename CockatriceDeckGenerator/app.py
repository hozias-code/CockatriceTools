import csv
import io
import xml.etree.ElementTree as ET
from flask import Flask, render_template, request, Response, jsonify

app = Flask(__name__)

# Load the data from the CSV file
with open('data.csv') as f:
    data = list(csv.DictReader(f))

# Get the list of unique product codes and product names
product_codes = sorted(list(set(row['ProductCode'] for row in data)))
product_names = sorted(list(set(row['ProductName'] for row in data)))


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        selected_product_code = request.form['product_code']
        selected_product_name = request.form['product_name']
        filtered_data = [row for row in data if row['ProductCode'] == selected_product_code and row['ProductName'] == selected_product_name]
        return render_template('index.html', product_codes=product_codes, product_names=product_names, selected_product_code=selected_product_code, selected_product_name=selected_product_name, filtered_data=filtered_data)

    return render_template('index.html', product_codes=product_codes, product_names=product_names)

@app.route('/get_product_names', methods=['GET'])
def get_product_names():
    product_code = request.args.get('product_code')
    filtered_data = [row for row in data if row['ProductCode'] == product_code]
    product_names = sorted(list(set(row['ProductName'] for row in filtered_data)))
    ##return {'product_names': product_names}
    return ({'product_names': product_names})

@app.route('/download', methods=['GET'])
def download():
    selected_product_code = request.args.get('product_code')
    selected_product_name = request.args.get('product_name')
    filtered_data = [row for row in data if row['ProductCode'] == selected_product_code and row['ProductName'] == selected_product_name]

    # Create the XML file
    root = ET.Element("cockatrice_deck", version="1")
    deckname = ET.SubElement(root, "deckname")
    comments = ET.SubElement(root, "comments")
    zone = ET.SubElement(root, "zone", name="main")

    for row in filtered_data:
        card = ET.SubElement(zone, "card", number=row["TotalCardQuantity"], name=row["CardName"])

    xml_string = ET.tostring(root, encoding='utf8', method='xml')

    # Create a Response object with the XML file as its data
    response = Response(io.BytesIO(xml_string), mimetype='text/xml')
    response.headers.set('Content-Disposition', 'attachment', filename=f'{selected_product_name}.cod')
    return response


if __name__ == '__main__':
    app.run(debug=True)