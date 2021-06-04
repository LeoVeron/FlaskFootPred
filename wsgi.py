from app import db, create_app

# if __name__ == "__main__":
app=create_app()
db.create_all(app=app)
app.run()
#   db.create_all(app=create_app())
  