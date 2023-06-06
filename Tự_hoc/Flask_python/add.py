from flask import Flask, redirect,url_for,render_template

app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return"<h1> Thanh Tung </h1>"

@app.route('/')
def hello_world():
    return render_template('home.index.html')
# @app.route('/')
# def hello_world():
#     return render_template('index.html', content ="Thanh Tung hoc gioi",
#                            card = ["Mec","BMW"])


# @app.route('/user/<name>')
# def hello_user(name):
#     if name == 'admin':
#         return redirect(url_for)
#     return f"<h1> Hello {name} !</h1>"

# @app.route('/admin')
# def hello_admin():
#     return f"<h1> Hello admin dz!</h1>"


# @app.route('/blog/<int:blog_id>')
# def blog(blog_id):
#     return f"<h1> Blog {blog_id}!</h1>"

if __name__ =="__main__":
    app.run(debug=True)