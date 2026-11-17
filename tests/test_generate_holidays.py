import datetime
from pathlib import Path

from generate_holidays import (
    HEADER,
    build_italy_holidays,
    resolve_year_range,
    write_holidays_csv,
)


def test_resolve_year_range_keeps_ordered_bounds():
    assert resolve_year_range(2015, 2018) == (2015, 2018)


def test_resolve_year_range_collapses_when_end_precedes_start():
    assert resolve_year_range(2020, 0) == (2020, 2020)
    assert resolve_year_range(2020, 2019) == (2020, 2020)


def test_build_italy_holidays_includes_new_year_and_sant_ambrogio():
    holidays_map = build_italy_holidays(2020, 2020)
    assert holidays_map[datetime.date(2020, 1, 1)]
    assert holidays_map[datetime.date(2020, 12, 7)] == "Sant'Ambrogio Patrono di Milano"
    # Easter Monday 2020 was 13 April
    assert datetime.date(2020, 4, 13) in holidays_map


def test_build_italy_holidays_spans_multiple_years():
    holidays_map = build_italy_holidays(2020, 2021)
    assert datetime.date(2020, 1, 1) in holidays_map
    assert datetime.date(2021, 1, 1) in holidays_map


def test_write_holidays_csv(tmp_path):
    holidays_map = {
        datetime.date(2020, 1, 1): "New Year's Day",
        datetime.date(2020, 12, 7): "Sant'Ambrogio Patrono di Milano",
    }
    output = tmp_path / "italy_holidays.csv"
    write_holidays_csv(holidays_map, str(output))
    lines = output.read_text().splitlines()
    assert lines[0] == ",".join(HEADER)
    assert "2020,1,1,New Year's Day" in lines
    assert "2020,12,7,Sant'Ambrogio Patrono di Milano" in lines
    assert Path(output).is_file()
