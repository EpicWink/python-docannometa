import typing as t

import docannometa


def repeat(
    text: t.Annotated[str, docannometa.doc("String to repeat")],
    n: t.Annotated[int, docannometa.doc("Number of times to repeat")],
) -> t.Annotated[str, docannometa.doc("Result string of length `n * len(text)`")]:
    """Repeat a string multiple times then concatenate."""
    return text * n


def test_annotations() -> None:
    assert repeat.__annotations__ == {
        "text": t.Annotated[str, docannometa.DocInfo(documentation="String to repeat")],
        "n": t.Annotated[
            int, docannometa.DocInfo(documentation="Number of times to repeat")
        ],
        "return": t.Annotated[
            str, docannometa.DocInfo("Result string of length `n * len(text)`")
        ],
    }
