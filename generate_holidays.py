# Generate a .csv file with the holidays
#
# python generate_holidays.py --start_year 2015 --end_year 2025


import datetime
import argparse
import holidays


OUTPUT_FILENAME = "data/italy_holidays.csv"
HEADER = ["Year", "Month", "Day", "Name"]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Years to compute holidays")
    parser.add_argument(
        "--start_year",
        default=datetime.datetime.now().year,
        type=int,
        help="First year to be considered",
    )
    parser.add_argument(
        "--end_year", default=0, type=int, help="Last year to be considered"
    )
    args = parser.parse_args()

    # check if start_year is previous or after end_year
    if args.start_year <= args.end_year:
        start_year = args.start_year
        end_year = args.end_year
    else:
        start_year = args.start_year
        end_year = args.start_year

    # print(start_year, end_year)

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
    # print(vacanze)

    with open(OUTPUT_FILENAME, "w") as output_file:
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
else:
    pass
