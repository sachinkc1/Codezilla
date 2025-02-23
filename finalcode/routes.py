from flask import render_template, request, url_for, redirect, flash
from db import get_db_connection
from werkzeug.security import generate_password_hash, check_password_hash

def init_routes(app):
    app.secret_key = 'your_secret_key'  # Needed for flash messages

    @app.route('/')
    def index():
        return render_template('login.html')

    @app.route('/register_page')
    def register_page():
        return render_template('registration.html')

    @app.route('/login', methods=['POST'])
    def login():
        username = request.form['username']
        password = request.form['password']
        
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        user = cursor.fetchone()
        conn.close()

        if user and check_password_hash(user['password'], password):
            flash(f"Welcome, {username}!")
            return render_template('home.html')
        else:
            flash("Invalid credentials. Please try again.")
            return redirect(url_for('index'))

    @app.route('/register', methods=['POST'])
    def register():
        username = request.form['username']
        email = request.form['email']
        age = request.form['age']
        password = request.form['password']
        
        hashed_password = generate_password_hash(password)

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, email, age, password) VALUES (%s, %s, %s, %s)", (username, email, age, hashed_password))
        conn.commit()
        conn.close()

        flash(f"User {username} registered successfully!")
        return redirect(url_for('index'))

    @app.route('/pomodoro')
    def pomodoro():
        return render_template('pomodoro.html')

    @app.route('/remeals')
    def remeals():
        return render_template('remeals.html')

    @app.route('/fitness')
    def fitness():
        return render_template('fitness.html')

    @app.route('/journal')
    def journal():
        return render_template('journal.html')

    @app.route('/aboutus')
    def aboutus():
        return render_template('aboutus.html')

    @app.route('/rpg_fitness')
    def rpg_fitness():
        return render_template('rpg.html')

    @app.route('/execise')
    def execise():
        return render_template('execise.html')

    @app.route('/loneliness')
    def loneliness():
        return render_template('loneliness.html')

    @app.route('/breathing')
    def breathing():
        return render_template('breathing.html')

    @app.route('/energy')
    def energy():
        return render_template('energy.html')

    @app.route('/metabolism')
    def metabolism():
        return render_template('metabolism.html')