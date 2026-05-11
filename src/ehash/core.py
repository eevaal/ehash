from typing import Optional

import bcrypt

def hashify(text: str, salt: Optional[str] = None, rounds: int = 12) -> str:
    encoded = text.encode("utf-8")
    if salt:
        c_salt = salt.encode('utf-8')
    else:
        c_salt = bcrypt.gensalt(rounds=rounds)
    return bcrypt.hashpw(encoded, c_salt).decode("utf-8")

def verify(text: str, hashed: str) -> bool:
    return bcrypt.checkpw(text.encode("utf-8"), hashed.encode("utf-8"))