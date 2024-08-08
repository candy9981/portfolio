from flask import Flask, render_template
import os
import psycopg2

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

# 環境変数から接続情報を取得
db_url = os.getenv("postgres://default:9nyhCRNvspg7@ep-round-rice-a4ceazjc-pooler.us-east-1.aws.neon.tech/verceldb?sslmode=require")
db_user = os.getenv("default")
db_password = os.getenv("9nyhCRNvspg7")
db_host = os.getenv("ep-round-rice-a4ceazjc-pooler.us-east-1.aws.neon.tech")
db_name = os.getenv("yakiniku-okazaki-bokujo-postgres")

# 接続
conn = psycopg2.connect(
    database=db_name,
    user=db_user,
    password=db_password,
    host=db_host,
)

@app.route('/')
def top():
    cur = conn.cursor()
    cur.execute("SELECT count FROM visitor")
    count = cur.fetchone()[0]
    count += 1
    cur.execute("UPDATE visitor SET count = %s;",(count,))
    conn.commit()
    return render_template('/home.html',count=count)

@app.route('/menu')
def menu():
    return render_template('/menu.html')

@app.route('/seats')
def seets():
    return render_template('/seats.html')

@app.route('/access')
def access():
    return render_template('/access.html')

@app.route('/menu/platter')
def oozara():
    return render_template('menus/大皿.html')

@app.route('/menu/specialbeef')
def tokusen():
    return render_template('menus/特選焼肉.html')

@app.route('/menu/beef')
def beef():
    return render_template('menus/牛焼肉.html')

@app.route('/menu/porkchicken')
def pork():
    return render_template('menus/豚・鶏焼肉.html')

@app.route('/menu/innards')
def horumon():
    return render_template('menus/ホルモン.html')

@app.route('/menu/sashimi')
def rare():
    return render_template('menus/刺身.html')

@app.route('/menu/salad')
def salad():
    return render_template('menus/サラダ・菜.html')

@app.route('/menu/pickles')
def tukemono():
    return render_template('menus/漬物.html')

@app.route('/menu/risedish')
def rice():
    return render_template('menus/飯・焼物.html')

@app.route('/menu/soup')
def soup():
    return render_template('menus/スープ・鍋.html')

@app.route('/menu/alcohol')
def beer():
    return render_template('menus/アルコール.html')

@app.route('/menu/softdrink')
def ice():
    return render_template('menus/アイス・ソフトドリンク.html')

@app.route('/menu/lunch')
def lunch():
    return render_template('menus/ランチ.html')

if __name__ == '__main__':
    app.run(debug=True)