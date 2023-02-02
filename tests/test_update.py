import pytest

from src.advent_readme_stars.constants import TABLE_MARKER
from src.advent_readme_stars.update import (
    insert_table,
    remove_existing_table,
    update_readme,
)

DEFAULT_TABLE_CONTENT = [
    "## 2022 Progress",
    "",
    "| Day | Part 1 | Part 2 |",
    "| :---: | :---: | :---: |",
    "| [Day 1](https://github.com/tfeuerbach/advent_of_code/tree/main/2022/day-01) | ⭐ | ⭐ |",
    "| [Day 2](https://github.com/tfeuerbach/advent_of_code/tree/main/2022/day-02) | ⭐ |   |",
    "| [Day 3](https://github.com/tfeuerbach/advent_of_code/tree/main/2022/day-03) | ⭐ | ⭐ |",
    "| [Day 4](https://github.com/tfeuerbach/advent_of_code/tree/main/2022/day-04) | ⭐ |   |",
    "| [Day 5](https://github.com/tfeuerbach/advent_of_code/tree/main/2022/day-05) | ⭐ | ⭐ |",
    "| [Day 6](https://github.com/tfeuerbach/advent_of_code/tree/main/2022/day-06) | ⭐ | ⭐ |",
]


@pytest.mark.parametrize(
    "lines, expected",
    [
        (
            [
                "AAAAA",
                TABLE_MARKER,
                "BBBBB",
                "CCCCC",
                "DDDDD",
                TABLE_MARKER,
                "EEEEE",
            ],
            [
                "AAAAA",
                TABLE_MARKER,
                "EEEEE",
            ],
        ),
        (
            [
                TABLE_MARKER,
                TABLE_MARKER,
                "AAAAA",
                "BBBBB",
                "CCCCC",
                "DDDDD",
                "EEEEE",
            ],
            [
                TABLE_MARKER,
                "AAAAA",
                "BBBBB",
                "CCCCC",
                "DDDDD",
                "EEEEE",
            ],
        ),
        (
            [
                "AAAAA",
                "BBBBB",
                "CCCCC",
                "DDDDD",
                "EEEEE",
                TABLE_MARKER,
                TABLE_MARKER,
            ],
            [
                "AAAAA",
                "BBBBB",
                "CCCCC",
                "DDDDD",
                "EEEEE",
                TABLE_MARKER,
            ],
        ),
        (
            [
                TABLE_MARKER,
                "AAAAA",
                "BBBBB",
                "CCCCC",
                "DDDDD",
                "EEEEE",
                TABLE_MARKER,
            ],
            [
                TABLE_MARKER,
            ],
        ),
        (
            [
                TABLE_MARKER,
                "AAAAA",
                "BBBBB",
                "CCCCC",
                "DDDDD",
                "EEEEE",
            ],
            [
                TABLE_MARKER,
                "AAAAA",
                "BBBBB",
                "CCCCC",
                "DDDDD",
                "EEEEE",
            ],
        ),
        (
            [
                "AAAAA",
                "BBBBB",
                "CCCCC",
                TABLE_MARKER,
                "DDDDD",
                "EEEEE",
            ],
            [
                "AAAAA",
                "BBBBB",
                "CCCCC",
                TABLE_MARKER,
                "DDDDD",
                "EEEEE",
            ],
        ),
        (
            [
                "AAAAA",
                "BBBBB",
                "CCCCC",
                "DDDDD",
                "EEEEE",
                TABLE_MARKER,
            ],
            [
                "AAAAA",
                "BBBBB",
                "CCCCC",
                "DDDDD",
                "EEEEE",
                TABLE_MARKER,
            ],
        ),
        (
            [
                "AAAAA",
                "BBBBB",
                "CCCCC",
                "DDDDD",
                "EEEEE",
            ],
            [
                "AAAAA",
                "BBBBB",
                "CCCCC",
                "DDDDD",
                "EEEEE",
            ],
        ),
    ],
)
def test_remove_existing_table(lines, expected):
    assert remove_existing_table(lines) == expected


@pytest.mark.parametrize(
    "lines, expected",
    [
        (
            [
                TABLE_MARKER,
                "AAAAA",
                "BBBBB",
                "CCCCC",
                "DDDDD",
                "EEEEE",
            ],
            [
                TABLE_MARKER,
                *DEFAULT_TABLE_CONTENT,
                TABLE_MARKER,
                "AAAAA",
                "BBBBB",
                "CCCCC",
                "DDDDD",
                "EEEEE",
            ],
        ),
        (
            [
                "AAAAA",
                "BBBBB",
                "CCCCC",
                TABLE_MARKER,
                "DDDDD",
                "EEEEE",
            ],
            [
                "AAAAA",
                "BBBBB",
                "CCCCC",
                TABLE_MARKER,
                *DEFAULT_TABLE_CONTENT,
                TABLE_MARKER,
                "DDDDD",
                "EEEEE",
            ],
        ),
        (
            [
                "AAAAA",
                "BBBBB",
                "CCCCC",
                "DDDDD",
                "EEEEE",
                TABLE_MARKER,
            ],
            [
                "AAAAA",
                "BBBBB",
                "CCCCC",
                "DDDDD",
                "EEEEE",
                TABLE_MARKER,
                *DEFAULT_TABLE_CONTENT,
                TABLE_MARKER,
            ],
        ),
        (
            [
                "AAAAA",
                "BBBBB",
                "CCCCC",
                "DDDDD",
                "EEEEE",
            ],
            [
                "AAAAA",
                "BBBBB",
                "CCCCC",
                "DDDDD",
                "EEEEE",
            ],
        ),
    ],
)
def test_insert_table(lines, expected, default_stars_response):
    assert insert_table(lines) == expected


@pytest.mark.parametrize(
    "lines, expected",
    [
        (
            [
                "AAAAA",
                "BBBBB",
                "CCCCC",
                TABLE_MARKER,
                "FFFFF",
                "GGGGG",
                "HHHHH",
                TABLE_MARKER,
                "DDDDD",
                "EEEEE",
            ],
            [
                "AAAAA",
                "BBBBB",
                "CCCCC",
                TABLE_MARKER,
                *DEFAULT_TABLE_CONTENT,
                TABLE_MARKER,
                "DDDDD",
                "EEEEE",
            ],
        ),
        (
            [
                "AAAAA",
                "BBBBB",
                "CCCCC",
                "DDDDD",
                "EEEEE",
            ],
            [
                "AAAAA",
                "BBBBB",
                "CCCCC",
                "DDDDD",
                "EEEEE",
            ],
        ),
    ],
)
def test_update_readme(lines, expected, default_stars_response):
    assert update_readme(lines) == expected
