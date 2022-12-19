from flask import Flask, render_template  # added render_template!
app = Flask(__name__)                     
    
@app.route('/levelone')                           
def level_one():
    # Instead of returning a string, 
    # we'll return the result of the render_template method, passing in the name of our HTML file
    return render_template('index.html', num =3)  

@app.route('/leveltwo/<int:num>')
def level_two(num):
    return render_template("index.html", num=num, color="blue")

@app.route('/levelthree/<int:num>/<string:color>')
def level_three(num,color):
    return render_template("index.html", num=num, color=color)

if __name__=="__main__":
    app.run(debug=True, port = 5001)                   

