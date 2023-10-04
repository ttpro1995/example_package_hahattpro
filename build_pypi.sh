rm -r dist/*
pip install --upgrade build
python -m build
twine upload --repository testpypi dist/*