from flask import Flask
from .flask_views  import main_views

# 어플리케이션 컨텍스트 생성
def create_app():
    app = Flask(__name__,static_url_path="/static")
    app.config.update(
        SECRET_KEY ="woosangyoon1234",
        SESSION_COOKIE_NAME="User_cookie"
    )
    # Blueprint
    app.register_blueprint(main_views.view)
    return app

    






        