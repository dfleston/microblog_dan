__author__ = 'Daniel Leston'

from app import db, models

users = models.User.query.all()
for u in users:
        db.session.delete(u)

posts = models.Post.query.all()
for p in posts:
        db.session.delete(p)