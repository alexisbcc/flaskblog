from flaskblog import db
from flaskblog.models import User, Post
db.drop_all()
db.create_all()
# user_1 = User(username='bambo', email='test@email.com', password='testing321')
# db.session.add(user_1)
# db.session.commit()
