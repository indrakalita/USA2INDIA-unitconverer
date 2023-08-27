from flask import Flask, render_template, request

app = Flask(__name__)

conversion_data = {
    'Weight': {
        'Pounds to Kilograms': 0.453592,
        'Kilograms to Pounds': 2.20462,
        'Ounces to Grams': 28.3495,
        'Grams to Ounces': 0.03527396,
    },
    'Liquid': {
        'Gallons to Liters': 3.78541,
        'Liters to Gallons': 0.264172,
        'Fluid Ounces to Milliliters': 29.5735,
        'Milliliters to Fluid Ounces': 0.033814,
    },
    # Add more measurement categories and conversions here
}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        source_measurement = request.form['source_measurement']
        target_measurement = request.form['target_measurement']
        value = float(request.form['value'])
        
        if source_measurement in conversion_data and target_measurement in conversion_data[source_measurement]:
            conversion_factor = conversion_data[source_measurement][target_measurement]
            result = value * conversion_factor
            return render_template('index.html', result=result, conversion_data=conversion_data)

    return render_template('index.html', conversion_data=conversion_data)

if __name__ == '__main__':
    app.run(debug=True)

