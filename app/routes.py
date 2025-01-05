from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from .models import User, db

main = Blueprint('main', __name__)

def is_logged_in():
    return 'user_id' in session

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            session['user_id'] = user.id  
            return redirect(url_for('main.dashboard'))
        else:
            flash('Email atau password salah', 'error')
            return redirect(url_for('main.login'))

    return render_template('login.html')

@main.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        role = request.form.get('role')

        
        if User.query.filter_by(email=email).first():
            flash('Email sudah digunakan', 'error')
            return redirect(url_for('main.register'))

      
        user = User(username=username, email=email, role=role)
        user.set_password(password)  
        db.session.add(user)
        db.session.commit()

        flash('Registrasi berhasil! Silakan login.', 'success')
        return redirect(url_for('main.login')) 

    return render_template('register.html')

@main.route('/dashboard')
def dashboard():
    if not is_logged_in():
        flash('Anda harus login terlebih dahulu', 'error')
        return redirect(url_for('main.login'))

    users = User.query.all()  
    return render_template('dashboard.html', users=users)


@main.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if not is_logged_in():
        flash('Anda harus login terlebih dahulu', 'error')
        return redirect(url_for('main.login'))

    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        role = request.form.get('role')

        if User.query.filter_by(email=email).first():
            flash('Email sudah digunakan', 'error')
            return redirect(url_for('main.add_user'))

        user = User(username=username, email=email, role=role)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()

        flash('Pengguna berhasil ditambahkan', 'success')
        return redirect(url_for('main.dashboard'))
    
    return render_template('add_user.html')

# Edit Pengguna
@main.route('/edit_user/<int:id>', methods=['GET', 'POST'])
def edit_user(id):
    if not is_logged_in():
        flash('Anda harus login terlebih dahulu', 'error')
        return redirect(url_for('main.login'))

    user = User.query.get_or_404(id)

    if request.method == 'POST':
        user.username = request.form.get('username')
        user.email = request.form.get('email')
        user.role = request.form.get('role')

        password = request.form.get('password')
        if password:
            user.set_password(password)

        db.session.commit()
        flash('Pengguna berhasil diperbarui', 'success')
        return redirect(url_for('main.dashboard'))

    return render_template('edit_user.html', user=user)

# Hapus Pengguna
@main.route('/delete_user/<int:id>', methods=['GET'])
def delete_user(id):
    if not is_logged_in():
        flash('Anda harus login terlebih dahulu', 'error')
        return redirect(url_for('main.login'))

    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    flash('Pengguna berhasil dihapus', 'success')
    return redirect(url_for('main.dashboard'))

# Logout Pengguna
@main.route('/logout')
def logout():
    session.pop('user_id', None)  
    return redirect(url_for('main.index'))
