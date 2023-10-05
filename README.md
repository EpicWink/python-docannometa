# Python documentation annotation metadata

Document symbols via annotation metadata, as described by
[PEP 727](https://peps.python.org/pep-0727/).

This aliases the same functionality in
[`typing_extensions`](https://pypi.org/project/typing-extensions/) if a sufficient
version is installed.

## Installation

```shell
pip install docannometa
```

## Usage

```python
from typing import Annotated

from docannometa import Doc

def repeat(
    text: Annotated[str, Doc("String to repeat")],
    n: Annotated[int, Doc("Number of times to repeat")],
) -> Annotated[str, Doc("Result string of length `n * len(text)`")]:
    """Repeat a string multiple times then concatenate."""
    return text * n
```
