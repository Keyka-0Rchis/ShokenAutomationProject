from dataclasses import dataclass
from typing import List

@dataclass
class Record:
    grade: int           # 学年
    student_id: int      # 出席番号
    good_points: List[str]  # 良かったところ（1個以上）
    comment: str

# これはコンストラクタ
def __init__(self, grade,student_id, good_points,comment):
    self.grade = grade
    self.student_id = student_id
    self.good_points = good_points
    self.comment = None  # 何も入れないならこれが必要なんだね