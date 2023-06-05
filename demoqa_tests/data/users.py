from dataclasses import dataclass


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    phone_number: str
    birthdate_year: int
    birthdate_month: str
    birthdate_day: int
    subject: str
    hobby: str
    filename: str
    address: str
    state: str
    city: str
