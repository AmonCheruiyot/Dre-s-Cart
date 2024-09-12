from flask import Flask
from .models import db
from .routes.auth_routes import auth_bp
from .routes.product_routes import product_bp
from .routes.order_routes import order_bp
from .routes.cart_routes import cart_bp
from .routes.review_routes import review_bp
from .routes.category_routes import category_bp
from .routes.payment_routes import payment_bp

app = Flask(__name__)

# Configure database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db.init_app(app)

# Register blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(product_bp)
app.register_blueprint(order_bp)
app.register_blueprint(cart_bp)
app.register_blueprint(review_bp)
app.register_blueprint(category_bp)
app.register_blueprint(payment_bp)

if __name__ == '__main__':
    app.run(debug=True)
