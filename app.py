from flask import Flask, render_template, request

app = Flask(__name__)

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def kelvin_to_celsius(k):
    return k - 273.15

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None

    if request.method == 'POST':
        value = float(request.form['value'])
        scale = request.form['scale']

        if scale == "Celsius":
            result = {
                "C → F": celsius_to_fahrenheit(value),
                "C → K": celsius_to_kelvin(value)
            }

        elif scale == "Fahrenheit":
            c = fahrenheit_to_celsius(value)
            result = {
                "F → C": c,
                "F → K": celsius_to_kelvin(c)
            }

        elif scale == "Kelvin":
            c = kelvin_to_celsius(value)
            result = {
                "K → C": c,
                "K → F": celsius_to_fahrenheit(c)
            }

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
