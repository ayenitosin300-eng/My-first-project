from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Render the HTML template with the message
    return render_template('index.html', message="Welcome to UI Account!")

if __name__ == '__main__':
    # Run the Flask application
    app.run(host='0.0.0.0', port=9001)
