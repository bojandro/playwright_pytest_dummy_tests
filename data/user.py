from typing import Optional


class User:
    def __init__(
        self,
        username: str,
        password: str,
        first_name: Optional[str] = '',
        last_name: Optional[str] = '',
        zip_code: Optional[str] = ''
    ):
        self.username = username
        self.password = password
        if first_name:
            self.first_name = first_name
        if last_name:
            self.last_name = last_name
        if zip_code:
            self.zip_code = zip_code
