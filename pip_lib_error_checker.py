import pkg_resources

for dist in pkg_resources.working_set:
    try:
        __import__(dist.key)
        print(f"{dist.key} is working fine")
    except ImportError:
        print(f"ERROR: could not import {dist.key}")
