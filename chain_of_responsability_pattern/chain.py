from __future__ import annotations
from abc import ABC, abstractmethod

from .numbers import Numbers

class Chain(ABC):
    @abstractmethod
    def set_next_chain(next_chain: Chain)-> None:
        pass

    @abstracmethod
    def calculate(request: Numbers)-> None:
        pass