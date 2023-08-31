# Python documentation annotation metadata

Document symbols via annotation metadata, as described by
[PEP 727](https://peps.python.org/pep-0727/).

This will become an alias to the same functionality in
[`typing_extensions`](https://pypi.org/project/typing-extensions/) if and when it is
implemented.

## Installation

```shell
pip install docannometa
```

## Usage

```python
from typing import Annotated

from docannometa import doc

def repeat(
    text: Annotated[str, doc("String to repeat")],
    n: Annotated[int, doc("Number of times to repeat")],
) -> Annotated[str, doc("Result string of length `n * len(text)`")]:
    """Repeat a string multiple times then concatenate."""
    return text * n
```
