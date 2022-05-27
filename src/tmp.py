from app import create_app
from core.handler import UserHandler


app = create_app()


from general.debugtool import DebugTool
DebugTool.start_logging(__file__)


if __name__ in '__main__':
    UserHandler.get_teacher_info()

