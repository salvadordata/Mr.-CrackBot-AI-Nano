import pytest
from ui.intro import run_intro

def test_run_intro(monkeypatch):
    def mock_pygame_init():
        pass

    monkeypatch.setattr("pygame.init", mock_pygame_init)
    run_intro()
