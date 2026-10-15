# Cloud environment demo

A tiny Python web application for testing development environment setup.
Requires Python 3.10 or later; no packages, API keys, or external services needed.

## Run

```sh
python3 app.py
```

The server listens on port 8000 on the local machine. `/` returns a welcome page;
`/health` returns `{"status": "ok"}`. Stop with Ctrl+C.

## Validate

With the server running, execute:

```sh
python3 - <<'PY'
import json
from urllib.request import urlopen
with urlopen('http://127.0.0.1:8000/') as response:
    assert response.status == 200
    assert b'It works!' in response.read()
with urlopen('http://127.0.0.1:8000/health') as response:
    assert json.load(response) == {'status': 'ok'}
print('Both smoke checks passed')
PY
```
