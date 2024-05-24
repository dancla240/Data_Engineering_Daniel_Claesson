from importlib.metadata import distributions

packages = distributions()

sorted_packages = sorted((pkg.metadata["Name"], pkg.version) for pkg in packages)

for name, version in sorted_packages:
    print(f"Name: {name}, version: {version}")
    

print(type(packages))


