rm -f ./dist/*
find . -name "*.pyc" -exec rm -rf {} \;
python3 setup.py  bdist_wheel