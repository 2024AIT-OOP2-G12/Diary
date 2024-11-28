from diaries.AbstractDiary import AbstractDiary

class NagataniDiary(AbstractDiary):

    def get_date(self):
        return "2024-11-28"
    def get_summary(self):
        return """今日はオブジェクト指向プログラミング演習2のグループワーク演習だった。
githubは初めて使ったのでまだ理解しきれてない。 
"""

    def get_author(self):
        return "kohei"