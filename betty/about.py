"""Provide information about (this version of) Betty."""

from __future__ import annotations

import platform
import sys
from importlib.metadata import distributions
from pathlib import Path
from typing import Iterator


def version() -> str | None:
    """
    Get the current Betty installation's version, if it has any.
    """
    with open(Path(__file__).parent / 'assets' / 'VERSION', encoding='utf-8') as f:
        release_version = f.read().strip()
    if release_version == '0.0.0':
        return None
    return release_version


def version_label() -> str:
    """
    Get the human-readable label for the current Betty installation's version.
    """
    return version() or 'development'


def is_stable() -> bool:
    """
    Check if the current Betty installation is a stable version.
    """
    return version() is not None


def is_development() -> bool:
    """
    Check if the current Betty installation is an unstable development version.
    """
    return version() is None


def _indent_mapping(items: dict[str, str]) -> str:
    max_indentation = max(map(len, items.keys())) + 4
    return '\n'.join(map(lambda x: '\n'.join(_indent_mapping_item(x[0], x[1], max_indentation)), items.items()))


def _indent_mapping_item(key: str, value: str, max_indentation: int) -> Iterator[str]:
    lines = value.split('\n')
    yield f'{key}{" " * (max_indentation - len(key))}    {lines[0]}'
    for line in lines[1:]:
        yield f'{" " * max_indentation}    {line}'


def report() -> str:
    """
    Produce a human-readable report about the current Betty installation.

    :returns: A human-readable string in US English, using monospace indentation.
    """
    return _indent_mapping({
        'Betty': version_label(),
        'Operating system': platform.platform(),
        'Python': sys.version,
        'Python packages': _indent_mapping({
            x.metadata['Name']: x.version
            for x
            in sorted(
                distributions(),
                key=lambda x: x.metadata['Name'].lower(),  # type: ignore[no-any-return, unused-ignore]
            )
        }),
    })
