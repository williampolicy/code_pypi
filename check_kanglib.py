import kanglib
import inspect

functions = inspect.getmembers(kanglib, inspect.isfunction)

for name, func in functions:
    print(f"Function name: {name}")
    print("Documentation:")
    print(inspect.getdoc(func))
    print("\n" + "="*50 + "\n")
