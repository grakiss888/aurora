# wsgi.py

from flask import g, Flask, jsonify
from flask_admin import Admin, BaseView, expose
from flask_login import LoginManager, current_user

def create_app():
  app = Flask(__name__)
  return app

application = create_app()
app = application

login_manager = LoginManager(app)
login_manager.session_protection = 'strong'
login_manager.login_view = 'index'

admin = Admin(app)

class MyView(BaseView):
    #127.0.0.1:5000/admin/
    @expose('/')
    def index(self):
        #return self.render('index.html')
        return '<html>Hello, admin</html>'

    def is_accessible(self):
        return g.user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('auth.login', next=request.url))

admin.add_view(MyView(name='Hello'))

admin.add_view(MyView(name='Hello 1', endpoint='test1', category='Test'))
admin.add_view(MyView(name='Hello 2', endpoint='test2', category='Test'))
admin.add_view(MyView(name='Hello 3', endpoint='test3', category='Test'))


@app.before_request
def before_request():
    g.user = current_user


@app.route('/api/v1/auth/login')
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    return (jsonify({'username':'test'}), 201,
            {'Location': url_for('index', id='id', _external=True)})

@app.route('/api/v1/')
def index():
    return jsonify({'index':'ok'})


@app.route('/api/v1/test')
def test():
    return jsonify({'test':'ok'})

if __name__ == '__main__':
    application.run()
