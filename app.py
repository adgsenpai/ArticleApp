#ADGSTUDIOS - server.py

from flask import Flask,render_template,send_from_directory
import articleCompiler
import articles as art

app = Flask(__name__,template_folder='./pages')


# allows for files to be refreshed in server
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/articles/<id>')
def article(id):
    return render_template('articlebase.html',pagetitle='ADGSTUDIOS Articles - '+art.return_article(int(id))['headline'],article=art.return_article(int(id)),htmlpayload=articleCompiler.render_article(art.return_filename(int(id))))

# return /Screenshots folder
@app.route('/Screenshots/<path:path>')
def send_screenshots(path):
    return send_from_directory('Screenshots', path)

@app.route('/')
def home():
  return render_template('articles.html',pagetitle='ADGSTUDIOS - Articles',articles=art.return_articles())

#running server on port 8000 - you can change the values here
if __name__ == "__main__":
  app.run(host="0.0.0.0",port=8000,debug=True)