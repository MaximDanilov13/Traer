import argparse
import tracert


def main():
    parser = argparse.ArgumentParser("Трассировка автономных систем")
    parser.add_argument('-host', type=str, help='ip or domain')
    args = parser.parse_args()
    tracert.get_path(args.host)


if __name__ == "__main__":
    main()
