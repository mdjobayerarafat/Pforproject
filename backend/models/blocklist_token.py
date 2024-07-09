# blocklist_token.py

from fastapi.security import OAuth2PasswordBearer
from fastapi import SecurityScopes

blocklisted_tokens = set()

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="token",
    scopes={"me": "Read information about the current user."},
)

def add_token_to_blocklist(token: str):
    blocklisted_tokens.add(token)

def is_token_blocklisted(token: str) -> bool:
    return token in blocklisted_tokens