from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# Load the columns used during training
with open('columns.pkl', 'rb') as f:
    columns = pickle.load(f)

LOCATIONS = columns[3:]

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        location = request.form['location']
        sqft = float(request.form['sqft'])
        bath = int(request.form['bath'])
        bhk = int(request.form['bhk'])
        # Build the input vector in the same order as training
        x = np.zeros(len(columns))
        x[0] = sqft
        x[1] = bath
        x[2] = bhk
        if location in LOCATIONS:
            loc_index = columns.index(location)
            x[loc_index] = 1
        features = x.reshape(1, -1)
        prediction = model.predict(features)[0] * 100000  # Convert lakhs to rupees
    return render_template('index.html', locations=LOCATIONS, prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True) 