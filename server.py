from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    title = 'Home Page'
    return render_template('index.html', title=title)

@app.route('/about')
def about():
    title = 'About Page'
    name = 'Wanticha Susuk'
    email = 'std.67122420330@ubru.ac.th'
    mobile = '062-674-6760'
    age = 20
    return render_template('about.html', title=title, name=name, email=email, mobile=mobile, age=age)

@app.route('/favorite/foods')
def favorite_foods():
    title = 'Favorite Foods Page'
    foods = ['กระเพราหมูกรอบ', 'ซูชิ', 'หมูฝอย', 'ราเมงทงคัตสึ', 'ส้มตำโคราช']
    return render_template('favorite_foods.html', title=title, foods=foods)

@app.route('/favorite/sports')
def favorite_sports():
    title = 'Favorite Sports Page'
    sports = ['ฟุตซอล','วอลเลย์บอล', 'แบดมินตัน']
    return render_template('favorite_sports.html', title=title, sports=sports)

@app.route('/favorite/movies')
def favorite_movies():
    title = 'Favorite Movies Page'
    movies = ['Avatar', 'The Substance', 'M3GAN', 'Final Destination', 'Smile']
    return render_template('favorite_movies.html', title = title, movies = movies)