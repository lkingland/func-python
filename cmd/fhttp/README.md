# HTTP Function

This is an example usage of the Functions HTTP middleware.

To see the actual middleware which is used when buildig a Python Function,
see the [Functions Python Scaffolding](https://github.com/knative/func/tree/main/templates/python/http)

## Running

Create a local virtual environment if it does not already exist:
```bash
python3 -m venv venv
```
Activate the virtual environment:
```bash
source ./venv/bin/activate
```
Install parliament from local source:
```bash
pip install -e ../..
```
Run the application:
```bash
python3 ./main.py
```
use `^C` to stop the application

To Deactivate the virtual environment:
```bash
deactivate
```
