from flask import Flask, render_template, url_for

app = Flask(__name__, static_url_path='/static')
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def home():
    return render_template('index.html')

app.run()
