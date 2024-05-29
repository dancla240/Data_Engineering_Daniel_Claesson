# This file just tests how it works to print out the name and version of installed packages
from importlib.metadata import distributions

packages = distributions()

sorted_packages = sorted((pkg.metadata["Name"], pkg.version) for pkg in packages)

print("Packages:")
for name, version in sorted_packages:
    print(f"Name: {name}, version: {version}")
    
print(type(packages))


