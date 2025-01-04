import os

class Config:
    # Secret Key untuk sesi Flask
    SECRET_KEY = os.urandom(24)
    
    # Database Config (Ubah dengan kredensial Anda)
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost:3306/pwp'

    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Menghindari warning

    # Konfigurasi JWT
    JWT_SECRET_KEY = 'bebff5ecf61ed5519ca9bc6044da54d64804c1cede983dbe'  # Gantilah dengan kunci yang aman

