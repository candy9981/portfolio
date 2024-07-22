from flask import Flask, render_template

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/')
def top():
    return render_template('/home.html')

@app.route('/menu')
def menu():
    return render_template('/menu.html')

@app.route('/seats')
def seets():
    return render_template('/seats.html')

@app.route('/access')
def access():
    return render_template('/access.html')

@app.route('/menu/大皿')
def oozara():
    return render_template('menus/大皿.html')

@app.route('/menu/特選焼肉')
def tokusen():
    return render_template('menus/特選焼肉.html')

@app.route('/menu/牛焼肉')
def beef():
    return render_template('menus/牛焼肉.html')

@app.route('/menu/豚・鶏焼肉')
def pork():
    return render_template('menus/豚・鶏焼肉.html')

@app.route('/menu/ホルモン')
def horumon():
    return render_template('menus/ホルモン.html')

@app.route('/menu/刺身')
def rare():
    return render_template('menus/刺身.html')

@app.route('/menu/サラダ・菜')
def salad():
    return render_template('menus/サラダ・菜.html')

@app.route('/menu/漬物')
def tukemono():
    return render_template('menus/漬物.html')

@app.route('/menu/飯・焼物')
def rice():
    return render_template('menus/飯・焼物.html')

@app.route('/menu/スープ・鍋')
def soup():
    return render_template('menus/スープ・鍋.html')

@app.route('/menu/アルコール')
def beer():
    return render_template('menus/アルコール.html')

@app.route('/menu/アイス・ソフトドリンク')
def ice():
    return render_template('menus/アイス・ソフトドリンク.html')

@app.route('/menu/ランチ')
def lunch():
    return render_template('menus/ランチ.html')

@app.route("/test")
def test():
    return "<p>test</p>"

if __name__ == '__main__':
    app.run(debug=True)