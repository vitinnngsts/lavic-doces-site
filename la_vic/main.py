from flask import Flask, render_template, request
from la_vic.produtos import CARDAPIO_DOCERIA

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template(
        'homepage.html',
        cardapio=CARDAPIO_DOCERIA,
    )

if __name__ == '__main__':
    app.run(debug=True)

