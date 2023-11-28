# run.py
from users.routes import app as users_app
from products.routes import app as products_app

if __name__ == '__main__':
    # Iniciar o servidor Flask para usuários na porta 5001
    users_app.run(port=5001, debug=True, threaded=True)

    # Iniciar o servidor Flask para produtos na porta 5002
    products_app.run(port=5002, debug=True, threaded=True)
