from abc import ABC, abstractmethod
from typing import TypeAlias, Generic, TypeVar

S = TypeVar('S')  # Can be anything (e.g., your 2D board list[list[int]])
I = TypeVar('I')  # Can be anything (e.g., your coordinate list[int])

class BaseEnvironment(ABC, Generic[S,I]):
    """
    Abstract Base Class for Search Problems.
    Enforces structure across state-spaces using generic types.
    """
    
    @abstractmethod
    def get_initial_puzzle_state(self) -> tuple[S,I]:
        """Returns the initial state wrapper containing board and empty indices."""
        pass
    
    @abstractmethod
    def get_next_states(self, current_state: tuple[S,I]) -> list[tuple[S,I]]:
        """Generates legal neighbor states matching the enforced state structure."""
        pass
    
    @abstractmethod
    def check_goal(self, current_state: tuple[S,I]) -> bool:
        """Verifies if the structured state tuple matches the termination criteria."""
        pass
