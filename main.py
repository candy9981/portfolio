from flask import Flask, render_template, make_response
import psycopg2

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

db_url = "postgres://default:9nyhCRNvspg7@ep-round-rice-a4ceazjc-pooler.us-east-1.aws.neon.tech/verceldb?sslmode=require"
db_user = "default"
db_password = "9nyhCRNvspg7"
db_host = "ep-round-rice-a4ceazjc-pooler.us-east-1.aws.neon.tech"
db_name = "verceldb"

connect_str = f"dbname='{db_name}' user='{db_user}' password='{db_password}' host='{db_host}'"

@app.route('/api/count', methods=['GET'])
def count():
    with psycopg2.connect(connect_str) as conn:
        with conn.cursor() as cur:
            cur.execute("UPDATE visitor SET count = count + 1 RETURNING count;")
            new_count = cur.fetchone()[0]
    return {"count": new_count}

@app.route('/')
def top():
    response = make_response(render_template('/home.html'))
    response.headers['Cache-Control'] = 'public, s-max-age=3600 max-age=0'
    return response

@app.route('/menu')
def menu():
    response = make_response(render_template('/menu.html'))
    response.headers['Cache-Control'] = 'public, s-max-age=3600 max-age=0'
    return response

@app.route('/seats')
def seets():
    response = make_response(render_template('/seats.html'))
    response.headers['Cache-Control'] = 'public, s-max-age=3600 max-age=0'
    return response

@app.route('/access')
def access():
    response = make_response(render_template('/access.html'))
    response.headers['Cache-Control'] = 'public, s-max-age=3600 max-age=0'
    return response

@app.route('/menu/platter')
def oozara():
    response = make_response(render_template('menus/大皿.html'))
    response.headers['Cache-Control'] = 'public, s-max-age=3600 max-age=0'
    return response

@app.route('/menu/specialbeef')
def tokusen():
    response = make_response(render_template('menus/特選焼肉.html'))
    response.headers['Cache-Control'] = 'public, s-max-age=3600 max-age=0'
    return response

@app.route('/menu/beef')
def beef():
    response = make_response(render_template('menus/牛焼肉.html'))
    response.headers['Cache-Control'] = 'public, s-max-age=3600 max-age=0'
    return response

@app.route('/menu/porkchicken')
def pork():
    response = make_response(render_template('menus/豚・鶏焼肉.html'))
    response.headers['Cache-Control'] = 'public, s-max-age=3600 max-age=0'
    return response

@app.route('/menu/innards')
def horumon():
    response = make_response(render_template('menus/ホルモン.html'))
    response.headers['Cache-Control'] = 'public, s-max-age=3600 max-age=0'
    return response

@app.route('/menu/sashimi')
def rare():
    response = make_response(render_template('menus/刺身.html'))
    response.headers['Cache-Control'] = 'public, s-max-age=3600 max-age=0'
    return response

@app.route('/menu/salad')
def salad():
    response = make_response(render_template('menus/サラダ・菜.html'))
    response.headers['Cache-Control'] = 'public, s-max-age=3600 max-age=0'
    return response

@app.route('/menu/pickles')
def tukemono():
    response = make_response(render_template('menus/漬物.html'))
    response.headers['Cache-Control'] = 'public, s-max-age=3600 max-age=0'
    return response

@app.route('/menu/risedish')
def rice():
    response = make_response(render_template('menus/飯・焼物.html'))
    response.headers['Cache-Control'] = 'public, s-max-age=3600 max-age=0'
    return response

@app.route('/menu/soup')
def soup():
    response = make_response(render_template('menus/スープ・鍋.html'))
    response.headers['Cache-Control'] = 'public, s-max-age=3600 max-age=0'
    return response

@app.route('/menu/alcohol')
def beer():
    response = make_response(render_template('menus/アルコール.html'))
    response.headers['Cache-Control'] = 'public, s-max-age=3600 max-age=0'
    return response

@app.route('/menu/softdrink')
def ice():
    response = make_response(render_template('menus/アイス・ソフトドリンク.html'))
    response.headers['Cache-Control'] = 'public, s-max-age=3600 max-age=0'
    return response

@app.route('/menu/lunch')
def lunch():
    response = make_response(render_template('menus/ランチ.html'))
    response.headers['Cache-Control'] = 'public, s-max-age=3600 max-age=0'
    return response

if __name__ == '__main__':
    app.run(debug=True)