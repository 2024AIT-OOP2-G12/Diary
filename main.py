from diaries.DiarySample import DiarySample
from diaries.NiwaDiary import NiwaDiary
from diaries.kittaDiary import kittaDiary
# ↓のリストには、メンバーの各日記が格納されます。
diaries = [DiarySample(),NiwaDiary(),kittaDiary()]
for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    
    print()