# app = create_app()
from core.score_record_hanlder import ScoreRecordHandler
from test.score_test import GETINFO

if __name__ == '__main__':
    # ScoreRecordHandler.del_info()
    GETINFO.post_info()
