# -*- coding: utf-8 -*-
"""
Created on Thu May  4 21:04:00 2023

@author: vs
"""

from pydantic import StrictInt


class Timestamp(StrictInt):
    pass


from datetime import datetime

from db import BaseModel


class model(BaseModel):
    class Config:
        json_encoders = {
            datetime: lambda dt: dt.timestamp(),
            datetime.timestamp: lambda ts: int(ts.timestamp()),
        }


class Timestamp1(int):
    """
    UNIX timestamp validation. Note: this is just an example, and is not
    intended for use in production; in particular this does NOT guarantee
    a postcode exists, just that it has a valid format.
    """

    # def __init__(self, x):
    #     super().__init__(x)

    @classmethod
    def __get_validators__(cls):
        # one or more validators may be yielded which will be called in the
        # order to validate the input, each validator will receive as an input
        # the value returned from the previous validator
        yield cls.validate

    @classmethod
    def __modify_schema__(cls, field_schema):
        # __modify_schema__ should mutate the dict it receives in place,
        # the returned value will be ignored
        field_schema.update(
            # simplified regex here
            pattern="^[0-9]{1,11}$",
            # some example
            examples=["1682691758"],
        )

    @classmethod
    def validate(cls, value):
        super().validate(value)
        from datetime import date, datetime, time, timedelta

        print("validate timestamp value", value)

        if isinstance(value, (str, float)):
            value = int(value)

        if value is None or 0 == value:
            value = int(datetime.utcnow().timestamp())

        if isinstance(value, (datetime, date, time, timedelta)):
            value = int(value.timestamp())

        if not isinstance(value, int):
            raise TypeError("integer|string|float required")

        return cls(value)

    def __repr__(self):
        return f"timestamp({super().__repr__()})"
