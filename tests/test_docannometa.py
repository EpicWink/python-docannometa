import typing as t

import docannometa


def repeat(
    text: t.Annotated[str, docannometa.Doc("String to repeat")],
    n: t.Annotated[int, docannometa.Doc("Number of times to repeat")],
) -> t.Annotated[str, docannometa.Doc("Result string of length `n * len(text)`")]:
    """Repeat a string multiple times then concatenate."""
    return text * n


def test_annotations() -> None:
    assert repeat.__annotations__ == {
        "text": t.Annotated[str, docannometa.Doc("String to repeat")],
        "n": t.Annotated[int, docannometa.Doc("Number of times to repeat")],
        "return": t.Annotated[
            str, docannometa.Doc("Result string of length `n * len(text)`")
        ],
    }

    assert repeat.__annotations__["text"].__metadata__[0].documentation == (
        "String to repeat"
    )
    assert repeat.__annotations__["n"].__metadata__[0].documentation == (
        "Number of times to repeat"
    )
    assert repeat.__annotations__["return"].__metadata__[0].documentation == (
        "Result string of length `n * len(text)`"
    )
