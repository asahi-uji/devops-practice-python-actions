import sys, pathlib
# リポジトリ直下（testsの1つ上）をインポート検索パスに追加
sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))

import main  # ここで main.py を確実に見つけられる

def test_compute_sum_basic():
    assert main.compute_sum(2, 3) == 5

def test_compute_sum_zero():
    assert main.compute_sum(0, 0) == 0

def test_compute_sum_negative():
    assert main.compute_sum(-5, 10) == 5
