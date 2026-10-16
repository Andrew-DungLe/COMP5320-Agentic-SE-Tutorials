"""Placeholder demo code. Replace with your chapter's demo.

It exists so that tests and CI pass from the first commit.
"""


def normalise_task_title(title: str) -> str:
    """Return a task title with surrounding and repeated whitespace removed.

    Raises:
        ValueError: if the title is empty after normalising.
    """
    cleaned = " ".join(title.split())
    if not cleaned:
        raise ValueError("Task title must not be empty")
    return cleaned


def main() -> None:
    print(normalise_task_title("  Write   the demo script  "))


if __name__ == "__main__":
    main()
