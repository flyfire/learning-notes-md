from pathlib import Path
import argparse


def generate_md(n: int):
    for i in range(n):
        if i < 10:
            name = f"0{i}"
        else:
            name = f"{i}"
        file = Path(f"{name}.md")
        file.touch(exist_ok=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="md文件生成器 eg. python generate_md.py -n 47 会生成00.md到46.md"
    )
    parser.add_argument('-n', type=int, required=True, help="max md file name")
    args = parser.parse_args()
    n = args.n
    generate_md(n)
