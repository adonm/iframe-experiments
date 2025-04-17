prereqs:
    brew install uv

api:
    uv run api.py
 
serveo PREFIX="portal" PORT="8000":
    ssh -R {{PREFIX}}-$(hostname):80:localhost:{{PORT}} serveo.net

