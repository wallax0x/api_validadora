# run.py
from app import create_app

app = create_app()

if __name__ == '__main__':
    # O debug=True faz o servidor reiniciar automaticamente a cada alteração no código.
    app.run(debug=True)
