# Check env  

echo $VIRTUAL_ENV

# Linter

## Python
```
pip install pylint
pylint --generate-rcfile > .pylintrc
```

Change file .pylintrc:

add unser [MAIN]:
```
disable=
    C0116, #missing function docstring
    E0015, #unrecognized-option
    C0114, #missing-module-docstring
```

Add settings.json in .vscode folder

# Commits

```
pip install pre-commit
```

Create file: .pre-commit-config.yaml

Then run
```
pre-commit install
```

Try commit something like:
``` python
def teste():
    x = 123
    print('ola')
```

And will get:

```
± |main S:9 ✗| → git commit -m "test"
pylint...................................................................Failed
- hook id: pylint
- exit code: 4

************* Module example
example.py:2:4: W0612: Unused variable 'x' (unused-variable)
```

If need ignore can use flag:

```
git commit -m "feat: Starting implementing use_cases" --no-verify
```