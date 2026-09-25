from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    projects = [
        {"number": "01", "name": "KINFIELD", "type": "Frontend · React", "color": "#d9f06c", "image": "https://images.unsplash.com/photo-1515879218367-8466d910aaa4?auto=format&fit=crop&w=1000&q=85", "description": "A responsive storefront built with reusable React components."},
        {"number": "02", "name": "OFFSCRIPT", "type": "Backend · API", "color": "#ffb7a2", "image": "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?auto=format&fit=crop&w=1000&q=85", "description": "A secure API powering a fast, reliable e-commerce experience."},
        {"number": "03", "name": "COMMON GROUND", "type": "Full-stack · Web app", "color": "#b9b4ff", "image": "https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=1000&q=85", "description": "A collaborative web app connecting local communities."},
    ]
    return render_template("index.html", projects=projects)


if __name__ == "__main__":
    app.run(debug=True)
