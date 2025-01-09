import pytest
from main import display_menu, take_order, display_order, menu

def test_display_menu(capfd):
    """Test if the menu is displayed correctly."""
    display_menu()
    captured = capfd.readouterr()
    assert "+------------+--------+" in captured.out
    assert "Burger" in captured.out

def test_take_order(monkeypatch):
    """Test taking orders from the menu."""
    inputs = iter(["burger", "pizza", "done"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    global orders
    orders = []
    take_order()
    assert "Burger" in orders
    assert "Pizza" in orders

def test_display_order(capfd):
    """Test if the order displays correctly."""
    global orders
    orders = ["Burger", "Pizza"]
    display_order()
    captured = capfd.readouterr()
    assert "Burger" in captured.out
    assert "Total" in captured.out
