"""Document symbols via annotation metadata, as described by PEP 727."""


class DocInfo:
    documentation: str

    def __init__(self, documentation: str) -> None:
        self.documentation = documentation

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(documentation={self.documentation!r})"

    def __eq__(self, other) -> bool:
        return (
            isinstance(other, self.__class__)
            and self.documentation == other.documentation
        )

    def __hash__(self) -> int:
        return hash((self.documentation,))


def doc(documentation: str) -> DocInfo:
    return DocInfo(documentation)
