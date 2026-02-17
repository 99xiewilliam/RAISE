import argparse
import importlib


def main() -> None:
    parser = argparse.ArgumentParser(description="Run raise algorithm by name")
    parser.add_argument("--algorithm", required=True, help="Algorithm module name, e.g. randomalgo")
    args, unknown = parser.parse_known_args()

    module = importlib.import_module(f"raisex.search.algorithms.{args.algorithm}")
    if not hasattr(module, "main"):
        raise AttributeError(f"Algorithm module {args.algorithm} has no main()")

    import sys

    sys.argv = [sys.argv[0], *unknown]
    module.main()


if __name__ == "__main__":
    main()
