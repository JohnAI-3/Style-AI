from st_webservice import app, db, lm
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
    __tablename__ = 'users';
    id = db.Column(db.Integer, primary_key=True)           
    email = db.Column(db.String(120), index=True, nullable=True, unique=True)
    username = db.Column(db.String(120), index=True, nullable=True, unique=True)
    password_hash = db.Column(db.String(128))
    social_id = db.Column(db.String(64), nullable=True, unique=True)
    social_username = db.Column(db.String(64), nullable=True, index=True)
    social_email = db.Column(db.String(120), nullable=True, index=True)
    user_images = db.relationship('Image', backref='img_user', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

    @property
    def is_oauth(self):
        if self.social_id == None:
            return False
        return True

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Image(db.Model):
    __tablename__ = 'images';
    id = db.Column(db.Integer, primary_key=True)
    gen_image_path = db.Column(db.String(64))
    gen_image_width = db.Column(db.Integer)
    gen_image_height = db.Column(db.Integer)
    num_iters = db.Column(db.Integer)
    model_name = db.Column(db.String(64))
    total_loss = db.Column(db.String(64))
    style_loss = db.Column(db.String(64))
    content_loss = db.Column(db.String(64))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return '<Image {}>'.format(self.id)

    def set_user(self, user):
        self.img_user = user


@lm.user_loader
def load_user(id):
    return User.query.get(int(id))