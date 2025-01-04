from app import create_app, db
from app.models import User

app = create_app()

def seed_data():
    with app.app_context():
        db.drop_all()
        db.create_all()
        
        users = [
            User(username="siapa", role="user", email="sukangampus@gmail.com"),
            User(username="suka", role="user", email="apalah@gmail.com"),
            User(username="mboh", role="user", email="mbolah@gmail.com"),
            User(username="woi", role="user", email="alamak@gmail.com")
        ]
        for user in users:
            user.set_password("password")
        db.session.bulk_save_objects(users)
        db.session.commit()
        print("Berhasil Bolo")

if __name__ == "__main__":
    seed_data()