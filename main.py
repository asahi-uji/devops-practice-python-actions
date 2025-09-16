import argparse
import logging
import sys
from pathlib import Path
from datetime import datetime

def get_app_dir() -> Path:
    # PyInstallerで固めた場合はexeのあるフォルダ、通常時はこのファイルのあるフォルダ
    if getattr(sys, "frozen", False):
        return Path(sys.executable).parent
    return Path(__file__).parent

def setup_logging() -> Path:
    app_dir = get_app_dir()
    log_dir = app_dir / "logs"
    log_dir.mkdir(parents=True, exist_ok=True)
    log_file = log_dir / "app.log"

    fmt = "%(asctime)s [%(levelname)s] %(message)s"
    logging.basicConfig(
        level=logging.INFO,
        format=fmt,
        handlers=[
            logging.FileHandler(log_file, encoding="utf-8"),
            logging.StreamHandler(sys.stdout),  # コンソールにも出す
        ],
    )
    logging.info("=== app start ===")
    return log_file

def compute_sum(a: int, b: int) -> int:
    # 例：単純なロジック（テストしやすい）
    return int(a) + int(b)

def parse_args():
    p = argparse.ArgumentParser(description="DevOps practice app")
    p.add_argument("--a", type=int, default=2, help="first integer")
    p.add_argument("--b", type=int, default=3, help="second integer")
    return p.parse_args()

def main() -> int:
    log_file = setup_logging()
    try:
        args = parse_args()
        logging.info(f"args: a={args.a}, b={args.b}")
        result = compute_sum(args.a, args.b)
        logging.info(f"result: {result}")
        print(f"sum = {result}")
        logging.info(f"log saved to: {log_file}")
        return 0
    except Exception as e:
        logging.exception(f"unhandled error: {e}")
        print("An error occurred. See logs/app.log.", file=sys.stderr)
        return 1

if __name__ == "__main__":
    sys.exit(main())
