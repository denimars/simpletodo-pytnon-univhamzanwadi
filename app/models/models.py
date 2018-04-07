from app import db

class Mahasiswa(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    nim = db.Column(db.String(50), nullable=False)
    nama = db.Column(db.String(1), nullable=False)