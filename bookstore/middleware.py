# Write a middleware that extracts JWT token from the header and validates it
import os

import jwt
from fastapi import HTTPException, Request
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jwt import PyJWTError

from constants import ALGORITHM, SECRET_KEY


class JWTBearer(HTTPBearer):
    def __init__(self):
        super(JWTBearer, self).__init__(auto_error=True)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
        if credentials:
            if not self.verify_jwt(credentials.credentials):
                raise HTTPException(status_code=403, detail="Invalid token or expired token")
            return credentials.credentials
        else:
            raise HTTPException(status_code=403, detail="Invalid authorization code.")

    def verify_jwt(self, jwtoken: str) -> bool:
        try:
            payload = jwt.decode(jwtoken, SECRET_KEY, algorithms=[ALGORITHM])
            return True
        except PyJWTError:
            return False
