from flask import Flask, render_template

app = Flask(__name__)

goods = [{
    "name":"Snus-200mg",
    "desc":"Good-Snus",
    "price":100,
    "imgpath":"piwo.jpg"
},{
    "name":"Snus-100mg",
    "desc":"Bad-Snus",
    "price":50,
    "imgpath":'piwo.jpg'
   }
    ,{
    "name":"Snus-20mg",
    "desc":"School-Snus",
    "price":10,
    "imgpath":"piwo.jpg"
    }

]

@app.route('/')
def display_main_page():
    return render_template('home_template.html', title = 'Главная',goods=goods)

@app.route('/product')
def display_product_page():
    return render_template('product_template.html', title = 'О товаре')

@app.route('/cart')
def display_cart():
    return render_template('cart.html', title = 'Корзина')

if __name__ == "__main__":
    app.run(debug=True)




