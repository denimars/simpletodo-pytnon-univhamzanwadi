from app import db

class Ayam(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    jenis = db.Column(db.String(50), nullable=False)
    kelamin = db.Column(db.String(1), nullable=False)