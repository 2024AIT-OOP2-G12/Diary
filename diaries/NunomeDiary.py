from diaries.AbstractDiary import AbstractDiary
class NunomeDiary(AbstractDiary):
    def get_date(self):
        return "2021-12-01"
    
    def get_summary(self):
        return "レポート作成に追われています"
    
    def get_author(self):
        return "Nunome"
    