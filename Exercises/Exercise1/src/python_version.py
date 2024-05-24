import sys
from importlib.metadata import distributions

def print_packages():
    packages = distributions()
    sorted_packages = sorted((pkg.metadata["Name"], pkg.version) for pkg in packages)
    print("Python print_package:")
    for name, version in sorted_packages:
        print(f"Name: {name}, version: {version}")

def print_version():
    print("Python print_version:")
    print(f"Python version: {sys.version}")

if __name__ == '__main__':
    print_version()
    print_packages()