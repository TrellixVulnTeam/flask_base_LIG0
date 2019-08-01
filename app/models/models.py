from app import db,login
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin


class User(UserMixin,db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column('user_username',db.String(64),index=True,unique=True)
    email = db.Column('user_useremail',db.String(120),index=True,unique=True)
    password_hash = db.Column(db.String(128))

    posts = db.relationship('Post',backref='author',lazy='dynamic')


    def __repr__(self):
        return f'<User {self.username}>'

    def set_password(self,password):
        self.password_hash = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password_hash,password)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class Post(db.Model):
    id = db.Column('post_id',db.Integer,primary_key = True)
    body = db.Column('body',db.String(140))
    timestamp = db.Column('data_pub',db.DateTime,index=True,default=datetime.utcnow)
    user_id = db.Column('user_id',db.Integer,db.ForeignKey('user.id'))
    
    def __repr__(self):
        return f"<Post {self.body}>"
