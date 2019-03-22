from abc import ABC, abstractmethod
from typing import Tuple
from pygame import display, Surface
from lib.properties import Resolution


class Window(ABC):
    """The class represents abstract window."""

    @abstractmethod
    def parent(self) -> Surface:
        """Returns parent window."""
        pass

    @abstractmethod
    def fill(self, color: Tuple[int, ...]) -> None:
        """Fills window with color."""
        pass


class Display(ABC):
    """The class represents display abstraction."""

    @abstractmethod
    def resolution(self) -> Resolution:
        """Returns game display resolution"""
        pass

    @abstractmethod
    def set_resolution(self) -> Window:
        """Sets resolution for a game."""
        pass

    @abstractmethod
    def set_title(self) -> None:
        """Sets title for a game."""
        pass

    @abstractmethod
    def update(self) -> None:
        """Updates game display."""
        pass


class GameDisplay(Display):
    """The class represents game display."""

    def __init__(self, resolution: Tuple[int, int], title: str) -> None:
        self._resolution = resolution
        self._title = title

    def resolution(self) -> Resolution:
        """Returns game display resolution."""
        return Resolution(self._resolution)

    def set_resolution(self) -> Window:
        """Sets resolution for a game."""
        return GameWindow(display.set_mode(self._resolution))

    def set_title(self) -> None:
        """Sets title for a game."""
        display.set_caption(self._title)

    def update(self) -> None:
        """Updates game display."""
        display.update()


class GameWindow(Window):
    """The class represents game window."""

    def __init__(self, window: Surface) -> None:
        self._win = window

    @property
    def parent(self) -> Surface:
        return self._win

    def fill(self, color: Tuple[int, ...]) -> None:
        self._win.fill(color)
