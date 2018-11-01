import shutil
import argparse


def copy_file(src, dst):
    """Copies a file from source to destination."""
    shutil.copyfile(src, dst)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("src", type=str, help="/source/directory/filename")
    parser.add_argument(
        "dst", type=str, help="/destination/directory/filename")

    arguments = parser.parse_args()

    copy_file(arguments.src, arguments.dst)
