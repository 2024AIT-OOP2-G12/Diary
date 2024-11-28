from diaries.AbstractDiary import AbstractDiary
class NiwaDiary(AbstractDiary):
    def get_date(self):
        return "2024-11-28"
    def get_summary(self):
        return """gitの仕組みをふわっとしか理解していなかったので、正直結構難しかった｡"""
    def get_author(self):
        return "Niwa"