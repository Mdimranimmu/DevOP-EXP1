from flask import Flask, request, render_template, redirect

app = Flask(__name__)

# Redirect root URL to /register
@app.route('/')
def home():
    return redirect('/register')

# Register route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        # Render success page with the name
        return render_template('success.html', name=name)  

    # Render registration form
    return render_template('register.html') 

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
