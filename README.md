# Flask-blog
Blogs are great way to share information. I am taking this project as my learning in Flask & also for my personal hobby of writing blogs 

## db queries on terminal
- from server import db, User, Post
- db.create_all()
- db.drop_all()
- user1 = User(username = "ak00029" , email="akumar00029@gmail.com", password="password")
- db.session.add(user1)
- db.session.commit()
- User.query.all()
- User.query.first()
- User.query.get(id)
- User.query.filter_by(username='ak00029')
- User.query.first().posts
