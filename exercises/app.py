from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home_page():
	My_favorite_players=["Lebron James", "Ryan", "Phelps"] 
	return render_template("index.html", My_favorite_players=My_favorite_players,likes_same_sport = True)
    

if __name__ == '__main__':
   app.run(debug = True)