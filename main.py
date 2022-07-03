from flask import Flask, render_template

app = Flask(__name__)

goods = [{
    "Name":"Snus-200mg",
    "Desc":"Good-Snus",
    "Price":"100$",
},{
    "Name":"Snus-100mg",
    "Desc":"Bad-Snus",
    "Price":"50$",
   }
    ,{
    "Name":"Snus-20mg",
    "Desc":"School-Snus",
    "Price":"10$",}

]

@app.route('/')
def display_main_page():
    return render_template('index.html', title = 'Главная')

@app.route('/product')
def display_product_page():
    return render_template('index.html', title = 'О товаре')

@app.route('/cart')
def display_cart():
    return render_template('index.html', title = 'Корзина')

if __name__ == "__main__":
    app.run(debug=True)




