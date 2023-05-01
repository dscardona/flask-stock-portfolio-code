from flask import Flask, escape, render_template, request, session, redirect, url_for, flash
from pydantic import BaseModel, validator, ValidationError

class StockModel(BaseModel):
    """Class for parsing new stock data from a form."""

    stock_symbol: str
    number_of_shares: int
    purchase_price: float

    @validator("stock_symbol")
    def stock_symbol_check(cls, value):
        if not value.isalpha() or len(value) > 5:
            raise ValueError("Stock symbol must be 1-5 characters")
        return value.upper()


app = Flask(__name__)
app.secret_key = "b'7Hq\xcbB\x9d\x1d\x0b\x16\xa8\xc2y\x93\xca`\xaf#\xba\xc9d\x9f)\x91po\xa9i\x87t-\xc1\xe9'"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html", company_name="TestDriven.io")
    # return render_template('about.html')


@app.route("/stocks/")
def list_stocks():
    return render_template('stocks.html')


@app.route("/hello/<message>")
def hello_message(message):
    return f"<h1>Welcome {escape(message)}!</h1>"


@app.route("/blog_posts/<int:post_id>")
def display_blog_post(post_id):
    return f"<h1>Blog Post #{post_id}...</h1"


@app.route("/add_stock", methods=["GET", "POST"])
def add_stock():
    if request.method == "POST":
        # Print the form data to the console
        for key, value in request.form.items():
            print(f"{key}: {value}")

        try:
            stock_data = StockModel(
                stock_symbol=request.form["stock_symbol"],
                number_of_shares=request.form["number_of_shares"],
                purchase_price=request.form["purchase_price"],
            )

            print(stock_data)

            # Save the form data to the session object
            session['stock_symbol'] = stock_data.stock_symbol
            session['number_of_shares'] = stock_data.number_of_shares
            session['purchase_price'] = stock_data.purchase_price
            flash(f"Added new stock ({stock_data.stock_symbol})!")
            return redirect(url_for('list_stocks'))

        except ValidationError as e:
            print(e)

    return render_template("add_stock.html")
