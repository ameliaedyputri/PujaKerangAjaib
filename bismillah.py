from flask import Flask, render_template, request, session
from flask_session import Session
import random

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

pesan_default = ["Cobalah membuat krabby patty terbaikmu, dengan tumpukan roti, daging, keju, selada, tomat, dan saus favoritmu.",
    "Terdapat fakta menarik yang harus kamu ketahui. Mr Puff merupakan animasi ikan buntal yang dalam kenyataannya dapat mengembang ketika ia merasa terancam dengan menelan air laut sebanyak-banyaknya.",
    "Mari berburu ubur-ubur bersama spongebob.",
    "Apa kamu sempat beranggapan bahwa Karen atau istri plankton merupakan animasi penerapan artificial intelligence dan robotic yang saat ini banyak dikembangkan?",
    "Jadilah seperti Shandy Cheeks yang mudah beradaptasi. Bahkan ia adalah seekor tupai yang telah beradaptasi dengan kehidupan bawah laut. Luar biasa bukan?",
    "Jadilah seperti Mermaid Man dan Barnacle Boy yang selalu menjadi pahlawan dalam melawan kejahatan.",
    "Terdapat fakta unik yang harus kamu ketahui. Garry merupakan animasi siput laut peliharaan spongebob yang hanya bisa berkata 'meong' seperti suara kucing.",
    "Jalani hari-harimu dengan penuh tawa, seperti spongebob.",
    "Jadilah seperti Plankton yang tidak mudah menyerah dalam mendapatkan resep krabby patty, namun jangan lupa ciptakan inovasi resep terbaikmu. Tidak ada yang tahu keberuntungan terjadi kapan.",
    "Terdapat fakta unik yang harus kamu ketahui. Spongebob merupakan animasi spons laut yang pada kenyataannya berbentuk torus atau cincin memanjang bukan balok."]

pesan_default_nama = ["cobalah membuat krabby patty terbaikmu, dengan tumpukan roti, daging, keju, selada, tomat, dan saus favoritmu.",
    "terdapat fakta menarik yang harus kamu ketahui. Mr Puff merupakan animasi ikan buntal yang dalam kenyataannya dapat mengembang ketika ia merasa terancam dengan menelan air laut sebanyak-banyaknya.",
    "mari berburu ubur-ubur bersama spongebob.",
    "apa kamu sempat beranggapan bahwa Karen atau istri plankton merupakan animasi penerapan artificial intelligence dan robotic yang saat ini banyak dikembangkan?",
    "jadilah seperti Shandy Cheeks yang mudah beradaptasi. Bahkan ia adalah seekor tupai yang telah beradaptasi dengan kehidupan bawah laut. Luar biasa bukan?",
    "jadilah seperti Mermaid Man dan Barnacle Boy yang selalu menjadi pahlawan dalam melawan kejahatan.",
    "terdapat fakta unik yang harus kamu ketahui. Garry merupakan animasi siput laut peliharaan spongebob yang hanya bisa berkata 'meong' seperti suara kucing.",
    "jalani hari-harimu dengan penuh tawa, seperti spongebob.",
    "jadilah seperti Plankton yang tidak mudah menyerah dalam mendapatkan resep krabby patty, namun jangan lupa ciptakan inovasi resep terbaikmu. Tidak ada yang tahu keberuntungan terjadi kapan.",
    "terdapat fakta unik yang harus kamu ketahui. Spongebob merupakan animasi spons laut yang pada kenyataannya berbentuk torus atau cincin memanjang bukan balok."]


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/resultpost', methods=['POST'])
def resultpost():
    submit_type = request.form.get('submit_type')

    if submit_type == 'with_name':
        if 'name' in request.form:
            session['name'] = request.form['name']
           # name = request.form['name']
           # resultpost = f"Selamat Datang, {name}"
            resultpost = f"Selamat datang, {session['name']}, Anda berhasil masuk ke Puja Kerang Ajaib."
    elif submit_type == 'without_name':
        resultpost = "Selamat Datang, Anda Berhasil masuk ke Puja Kerang Ajaib."

    return render_template('resultpost.html', resultpost=resultpost)

@app.route('/resultget/', methods=['GET', 'POST'])
def resultget_noname():
    resultget = random.choice(pesan_default)
    return render_template('resultget.html', resultget=resultget)

@app.route('/resultget/<name>', methods=['GET', 'POST'])
def resultget(name=None):
    if name:
        resultget = f"{name}, {random.choice(pesan_default_nama)}"
    else:
        if request.method == 'GET':

            submit_type = request.form.get('submit_type')

            if submit_type == 'with_name':
                if 'name' in request.form:
                    session['name'] = request.form['name']
                    resultget = f"{session['name']}, {random.choice(pesan_default_nama)}"
                else:
                    resultget = random.choice(pesan_default)

            elif submit_type == 'without_name':
                resultget = random.choice(pesan_default)

    return render_template('resultget.html', resultget=resultget)

if __name__ == '__main__':
    app.run(debug=True)