from app import db, create_app


app = create_app()
# db.create_all(app)
app.run()
# if __name__ == "__main__":
#     app = create_app()
#     # db.create_all(app)
#     app.run()
  