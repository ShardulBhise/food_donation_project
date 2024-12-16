from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Temporary storage for restaurants
restaurants = []

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Get data from the form
        name = request.form['name']
        food = request.form['food']
        address = request.form['address']
        
        # Save the data in the list
        restaurants.append({'name': name, 'food': food, 'address': address})
        
        return redirect('/donations')  # Redirect to the donations page after registration
    return render_template('register.html')

@app.route('/donations')
def donations():
    return render_template('donations.html', restaurants=restaurants)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

