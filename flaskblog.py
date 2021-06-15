from flask import Flask, render_template, url_for
app = Flask(__name__)

app.config["SECRET_KEY"] = '67a35a44e471ea97f19c43e348ff533d'

posts = [
    {
        "author": "Rand Al-Thor",
        "title": "Blog Post 1",
        "content": "First Post content",
        "date_posted": "May 1st"
    },
    {
        "author": "Anasurimbor Kellhus",
        "title": "Blog Post 2",
        "content": "Second Post content",
        "date_posted": "May 5th"
    },
    {
        "author": "Paul Atreides",
        "title": "Blog Post 3",
        "content": "Third Post content",
        "date_posted": "May 7th"
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", title="About")


if __name__ == "__main__":
    app.run(debug=True)
