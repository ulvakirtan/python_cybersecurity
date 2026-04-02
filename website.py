from flask import Flask, request, render_template_string

app = Flask(__name__)

# Fake credentials
USERNAME = "admin"
PASSWORD = "secret123"

login_page = """
<h2>Login Page</h2>
<form method="POST">
    Username: <input name="username"><br>
    Password: <input name="password" type="password"><br>
    <input type="submit" value="Login">
</form>
<p>{{ message }}</p>
"""

@app.route("/admin")
def admin():
    return "Admin Panel"

@app.route("/dashboard")
def dashboard():
    return "User Dashboard"

@app.route("/secret")
def secret():
    return "Top Secret Data"

@app.route("/login", methods=["GET", "POST"])
def login2():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # 🔥 Vulnerability: weak auth logic
        if "admin" in username:
            return "Welcome admin"

        return "Invalid login"

    return """
    <form method="POST">
        Username: <input name="username"><br>
        Password: <input name="password"><br>
        <input type="submit">
    </form>
    """

@app.route("/login2", methods=["GET", "POST"])
def login_sql():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # 🔥 Simulated SQL Injection vulnerability
        if username == "' OR '1'='1" or password == "' OR '1'='1":
            return "Logged in via SQL Injection!"

        return "Invalid login"

    return """
    <form method="POST">
        Username: <input name="username"><br>
        Password: <input name="password"><br>
        <input type="submit">
    </form>
    """

attempts = {}
@app.route("/", methods=["GET", "POST"])
def login():
    global attempts
    message = ""
    ip = request.remote_addr
    ipheader = request.headers.get("X-Forwarded-For", request.remote_addr)
    if ip not in attempts:
        attempts[ip] = 0

    if attempts[ip] >= 5:
        return "Too many attempts. Try later."


    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == USERNAME and password == PASSWORD:
            message = "Login successful"
        else:
            attempts[ip] += 1
            message = "Invalid credentials"

    return render_template_string(login_page, message=message)

if __name__ == "__main__":
    app.run(debug=False)