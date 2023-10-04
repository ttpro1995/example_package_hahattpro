# How to build ?

```
pip install --upgrade build
python -m build
twine upload --repository testpypi dist/*
```

# How to install 
```
pip install -i https://test.pypi.org/simple/ --no-cache-dir --force-reinstall -U example-package-hahattpro
```


# How to add extra data 

[tool.setuptools.package-data]
example_package_hahattpro = ["*.txt", "*.rst"]
"example_package_hahattpro.template" = ["*.txt"]
