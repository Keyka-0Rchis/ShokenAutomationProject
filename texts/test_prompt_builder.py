import pytest
from util.prompt_builder import build_prompt
from domain.student_record import Record

# 本テストの意義
# Excelの値がきちんとプロンプトに反映されていることを確認する。

def test_current_student():

    # Recordのフィールド変数
    grade = 1
    id = 1
    good_points = ["GP1","GP2"]

    dummy_record = Record(grade,id,good_points)

    prompt = build_prompt(dummy_record)

    # 返り値が str であること
    assert isinstance(prompt, str)

    # 進級メッセージが含まれていること
    assert "進級おめでとうございます。" in prompt

    # 良かったところが反映されていること
    assert "- GP1" in prompt
    assert "- GP2" in prompt

def test_graduate_student():

    # Recordのフィールド変数
    grade = 3
    id = 1
    good_points = ["GP1","GP2"]

    dummy_record = Record(grade,id,good_points)

    prompt = build_prompt(dummy_record)

    # 返り値が str であること
    assert isinstance(prompt, str)

    # 進級メッセージが含まれていること
    assert "卒業おめでとうございます。" in prompt

    # 良かったところが反映されていること
    assert "- GP1" in prompt
    assert "- GP2" in prompt

def test_noGoodPoint_student():
    # Recordのフィールド変数
    grade = 3
    id = 1
    good_points = []

    dummy_record = Record(grade,id,good_points)

    prompt = build_prompt(dummy_record)

    # 返り値が str であること
    assert isinstance(prompt, str)

    # 進級メッセージが含まれていること
    assert "卒業おめでとうございます。" in prompt

    # 良かったところが補完されていること
    assert "特に目立った記録はありません。" in prompt