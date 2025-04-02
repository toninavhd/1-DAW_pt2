from __future__ import annotations

class Date:
    def __init__(self, day: int, month: int, year: int):
        self.year = self._validate_year(year)
        self.month = self._validate_month(month)
        self.day = self._validate_day(day, self.month, self.year)

    @staticmethod
    def _validate_year(year: int) -> int:
        return year if 1900 <= year <= 2050 else 1900

    @staticmethod
    def _validate_month(month: int) -> int:
        return month if 1 <= month <= 12 else 1

    @staticmethod
    def _validate_day(day: int, month: int, year: int) -> int:
        return day if 1 <= day <= Date.get_days_in_month(month, year) else 1

    @staticmethod
    def is_leap_year(year: int) -> bool:
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    @staticmethod
    def get_days_in_month(month: int, year: int) -> int:
        if month in {1, 3, 5, 7, 8, 10, 12}:
            return 31
        if month in {4, 6, 9, 11}:
            return 30
        return 29 if Date.is_leap_year(year) else 28

    def get_delta_days(self) -> int:
        days = sum(366 if Date.is_leap_year(y) else 365 for y in range(1900, self.year))
        days += sum(Date.get_days_in_month(m, self.year) for m in range(1, self.month))
        return days + self.day - 1

    def weekday(self) -> int:
        return (self.get_delta_days() + 1) % 7

    def is_weekend(self) -> bool:
        return self.weekday() in {0, 6}

    def short_date(self) -> str:
        return f"{self.day:02}/{self.month:02}/{self.year}"

    def __str__(self) -> str:
        days_of_week = ["DOMINGO", "LUNES", "MARTES", "MIÉRCOLES", "JUEVES", "VIERNES", "SÁBADO"]
        months_of_year = [
            "ENERO", "FEBRERO", "MARZO", "ABRIL", "MAYO", "JUNIO",
            "JULIO", "AGOSTO", "SEPTIEMBRE", "OCTUBRE", "NOVIEMBRE", "DICIEMBRE"
        ]
        day_of_week = days_of_week[self.weekday()]
        month_name = months_of_year[self.month - 1]
        return f"{day_of_week} {self.day} DE {month_name} DE {self.year}"

    def __add__(self, days_to_add: int) -> Date:
        day, month, year = self.day, self.month, self.year
        while days_to_add > 0:
            days_in_month = Date.get_days_in_month(month, year)
            if day + days_to_add <= days_in_month:
                day += days_to_add
                break
            days_to_add -= (days_in_month - day + 1)
            day = 1
            month += 1
            if month > 12:
                month = 1
                year += 1
        return Date(day, month, year)

    def __sub__(self, other: Date | int) -> Date | int:
        if isinstance(other, Date):
            return self.get_delta_days() - other.get_delta_days()
        day, month, year = self.day, self.month, self.year
        while other > 0:
            if day > other:
                day -= other
                break
            other -= day
            month -= 1
            if month < 1:
                month = 12
                year -= 1
            day = Date.get_days_in_month(month, year)
        return Date(day, month, year)

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Date) and (self.day, self.month, self.year) == (other.day, other.month, other.year)

    def __gt__(self, other: object) -> bool:
        return isinstance(other, Date) and (self.year, self.month, self.day) > (other.year, other.month, other.day)

    def __lt__(self, other: object) -> bool:
        return isinstance(other, Date) and (self.year, self.month, self.day) < (other.year, other.month, other.day)
