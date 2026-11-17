# Generate a .csv file with the holidays
#
# python generate_holidays.py --start_year 2015 --end_year 2025


import argparse
import datetime

import holidays

OUTPUT_FILENAME = "data/italy_holidays.csv"
HEADER = ["Year", "Month", "Day", "Name"]


def resolve_year_range(start_year, end_year):
    """Return an inclusive year range, collapsing to start_year when end precedes start."""
    if start_year <= end_year:
        return start_year, end_year
    return start_year, start_year


def build_italy_holidays(start_year, end_year):
    """Build a date->name map of Italian holidays, plus Sant'Ambrogio on 7 December."""
    start_year, end_year = resolve_year_range(start_year, end_year)
    vacanze = []
    for y in range(start_year, end_year + 1, 1):
        h = holidays.country_holidays("IT", years=y)
        h[datetime.date(y, 12, 7)] = (
            "Sant'Ambrogio Patrono di Milano"  # add this local holiday for who works in Milano
        )
        h = dict(sorted(h.items()))
        vacanze.append(h)

    # convert vancanze list of dict into dict
    temp = vacanze
    vacanze = {}
    for d in temp:
        vacanze.update(d)
    return vacanze


def write_holidays_csv(vacanze, output_filename=OUTPUT_FILENAME):
    """Write holidays as Year,Month,Day,Name CSV."""
    with open(output_filename, "w") as output_file:
        output_file.write(",".join(HEADER) + "\n")

        for data in vacanze.keys():
            output_file.write(
                str(data.year)
                + ","
                + str(data.month)
                + ","
                + str(data.day)
                + ","
                + vacanze[data]
                + "\n"
            )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Years to compute holidays")
    parser.add_argument(
        "--start_year",
        default=datetime.datetime.now().year,
        type=int,
        help="First year to be considered",
    )
    parser.add_argument("--end_year", default=0, type=int, help="Last year to be considered")
    args = parser.parse_args()

    vacanze = build_italy_holidays(args.start_year, args.end_year)
    write_holidays_csv(vacanze)
else:
    pass
