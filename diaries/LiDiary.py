from diaries.AbstractDiary import AbstractDiary

class LiDiary(AbstractDiary):

    def get_date(self):
        return "2024-11-28"

    def get_summary(self):
        return "GitHubの使用について学んで、大変だった。時間かかった。"

    def get_author(self):
        return "Li"
