import shutil
import argparse


def copy(src, dst):
    """Copies a file or folder from source to destination."""
    try:
        shutil.copyfile(src, dst)
    # shutil.copyfile will throw an IsADirectoryError if src is a directory instead of a file.
    except IsADirectoryError:
        shutil.copytree(src, dst)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "src", type=str, help="source directory and/or filename")
    parser.add_argument(
        "dst", type=str, help="destination directory and/or filename")

    arguments = parser.parse_args()

    copy(arguments.src, arguments.dst)
