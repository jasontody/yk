from flask import Flask, render_template
app = Flask(__name__)
app.debug = True

@app.route('/')
def hello_world():
	return render_template('index.html')

@app.route('/about')
def about():
	return render_template('about-us.html')

@app.route('/price')
def price():
	return render_template('pricing.html')

@app.route('/contact')
def contact():
	return render_template('contact.html')

@app.route('/blog')
def blog():
	return render_template('blog.html')

@app.route('/portfolio')
def portfolio():
	return render_template('portfolio.html')

@app.route('/feature')
def feature():
	return render_template('features.html')

@app.route('/service')
def service():
	return render_template('services.html')

@app.route('/portfolio/<name>')
def portfolio_detail(name=None):
	return render_template('portfolio-item.html', name=name)

@app.route('/comming-soon')
def comming_soon():
	return render_template('comming-soon.html')

@app.route('/signin')
def sign_in():
	return render_template('sign_in.html')



if __name__ == '__main__':
	app.run(host='0.0.0.0')


