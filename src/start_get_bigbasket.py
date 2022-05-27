from app import create_app
from core.bigbasket_executer import BigbasketExecuter


app = create_app()


if __name__ in '__main__':
    BigbasketExecuter().exec(qty=11)

