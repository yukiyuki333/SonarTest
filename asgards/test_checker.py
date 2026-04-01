import pytest
from checker import main
from io import StringIO

def test_checker_input_0(monkeypatch, capsys):
    # 測試輸入 0
    monkeypatch.setattr('sys.stdin', StringIO('0\n'))
    main()
    captured = capsys.readouterr()
    assert captured.out.strip() == "False"

def test_checker_input_1(monkeypatch, capsys):
    # 測試輸入 1
    monkeypatch.setattr('sys.stdin', StringIO('1\n'))
    main()
    captured = capsys.readouterr()
    assert captured.out.strip() == "True"

def test_checker_input_2(monkeypatch, capsys):
    # 測試輸入 2
    monkeypatch.setattr('sys.stdin', StringIO('2\n'))
    main()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Nooooooooooooooooo!!!"

def test_checker_input_non_numeric(monkeypatch, capsys):
    # 測試輸入非數字 (例如 "abc")
    monkeypatch.setattr('sys.stdin', StringIO('abc\n'))
    main()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Nooooooooooooooooo!!!"
