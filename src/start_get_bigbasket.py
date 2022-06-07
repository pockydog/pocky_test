from app import create_app
from core.bigbasket_executer import BigbasketExecuter
from core.daraz_parser import DarazParser

app = create_app()

if __name__ in '__main__':
    # BigbasketExecuter().exec(qty=10)
    print(DarazParser().testt())





