import main
import pytest

def _set_inputs(monkeypatch, inputs):
    it = iter(inputs)
    monkeypatch.setattr("builtins.input", lambda prompt="": next(it))

def test_addition_and_quit(monkeypatch, capsys):
    _set_inputs(monkeypatch, ["1", "3", "4", "q"])
    main.main()
    out = capsys.readouterr().out
    assert "결과: 7.0" in out

def test_divide_by_zero(monkeypatch, capsys):
    _set_inputs(monkeypatch, ["4", "5", "0", "q"])
    main.main()
    out = capsys.readouterr().out
    assert "0으로 나눌 수 없습니다." in out

def test_modulo_by_zero(monkeypatch, capsys):
    _set_inputs(monkeypatch, ["6", "5", "0", "q"])
    main.main()
    out = capsys.readouterr().out
    assert "0으로 나눌 수 없습니다." in out

def test_sqrt_negative(monkeypatch, capsys):
    _set_inputs(monkeypatch, ["7", "-4", "q"])
    main.main()
    out = capsys.readouterr().out
    assert "음수의 제곱근은 계산할 수 없습니다." in out

def test_invalid_choice(monkeypatch, capsys):
    _set_inputs(monkeypatch, ["x", "q"])
    main.main()
    out = capsys.readouterr().out
    assert "잘못된 입력입니다. 다시 선택하세요." in out

def test_non_numeric_input(monkeypatch, capsys):
    _set_inputs(monkeypatch, ["1", "a", "q"])
    main.main()
    out = capsys.readouterr().out
    assert "숫자를 입력하세요." in out

def test_power_operation(monkeypatch, capsys):
    _set_inputs(monkeypatch, ["5", "2", "3", "q"])
    main.main()
    out = capsys.readouterr().out
    assert "결과: 8.0" in out