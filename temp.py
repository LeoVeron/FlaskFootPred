from app import db, create_app
def createapp():
    db.create_all(app=create_app())