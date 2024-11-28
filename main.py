from diaries.DiarySample import DiarySample
from diaries.NunomeDiary import NunomeDiary

from diaries.NiwaDiary import NiwaDiary

from diaries.KoheiDiary import KoheiDiary

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [DiarySample(),
           KoheiDiary(),
           NiwaDiary()
]




for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    
    print()