"""Document symbols via annotation metadata, as described by PEP 727."""


class Doc:
    documentation: str

    def __init__(self, documentation: str) -> None:
        self.documentation = documentation

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(documentation={self.documentation!r})"

    def __eq__(self, other) -> bool:
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self.documentation == other.documentation

    def __hash__(self) -> int:
        return hash(self.documentation)


try:
    from typing import Doc
except ImportError:
    try:
        from typing_extensions import Doc
    except ImportError:
        pass
