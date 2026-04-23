from flask import Flask, render_template, request
import requests
import smtplib
import os

posts_url = "https://api.npoint.io/0adeedbf49d9fee6c128"
response = requests.get(posts_url)
all_posts = response.json()

OWN_EMAIL = os.environ.get("GMAIL")
OWN_PASSWORD = os.environ.get("GPASS")

app = Flask(__name__)

@app.route('/')
def get_all_posts():
    return render_template("index.html", posts=all_posts)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        data = request.form
        print(data)
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)

def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
    print(email_message)
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=OWN_EMAIL, password=OWN_PASSWORD)
        connection.sendmail(from_addr=OWN_EMAIL, to_addrs=OWN_EMAIL, msg=email_message)

@app.route('/form-entry', methods=['POST'])
def receive_data():
    return "<h1> SUCCESSFUL!!</h1>"

@app.route('/post/<int:index>')
def show_post(index):
    request_post = None
    for blog_post in all_posts:
        if blog_post['id'] == index:
            request_post = blog_post
    return render_template("post.html", post=request_post)

if __name__ == "__main__":
    app.run(debug=True)