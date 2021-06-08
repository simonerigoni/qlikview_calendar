# QlikView Caledar

## Introduction

Many times you have to create calendar based reports so it would be nice to have a calendar already in place and ready to copy/paste into your reports script. In this case I am focusing on QlikView reports and since I am currently based in Italy I will consider the working days/non working days are based on Italian legislation.
To generate a **italy_holidays.csv** CSV file containing the holidays in the required timeframe I am going to use [Python](https://www.python.org/) and then I will use [QlikView](https://www.qlik.com/us/products/qlikview) to ETL the data and create the report.

The working days/non working days are based on Italian legislation (example for year 2020):
* New Year’s Day (Capodanno) – 01/01/2020
* Epiphany (Epifania) - 06/01/2020
* Easter Monday (Lunedì di Pasqua) – 13/04/2020
* Liberation Day (Liberazione dal nazifascismo) - 25/04/2020
* Labour Day (Festa del lavoro) - 01/05/2020
* Republic Day (Festa della Repubblica) - 02/06/2020
* Assumption of Mary (Assunzione di Maria) – 15/08/2020
* All Saint’s Day (Ognissanti) - 01/11/2020
* Saint Ambrose Patron of Milano (Sant'Ambrogio Patrono di Milano) - 07/12/2020 (only valid for Milano)
* Immaculate Conception (Immacolata Concezione) - 08/12/2020
* Christmas Day (Natale di Gesù) - 25/12/2020
* St. Stephen’s Day (Santo Stefano) - 26/12/2020

## Software and Libraries

This project uses Python 3.8.5 and the following libraries:
* [argparse](https://docs.python.org/3/library/argparse.html)
* [holidays](https://pypi.org/project/holidays/)


For the report I have used [QlikView](https://www.qlik.com/us/products/qlikview) version 12.50.20200.0

## Running the code

To generate the holiday CSV file you have to run `python generate_holidays.py --start_year 2015 --end_year 2025` where `--start_year` and `--end_year` are optional parameters

To reload the qvw document you can run `run_report.cmd`

## Results

The report is pretty simple and it is just a check that everything is working as expected:

![Report](images/report.JPG)

Of course it is possible to play around with the filters and check how the count of day_type changes

You can find more information in this [blog post](https://medium.com/@simone.rigoni01/quick-and-easy-calendar-with-python-and-qlikview-cdd5d2db30e1)

## Acknowledgements

The QlikView script is based on this awesome [post](https://community.qlik.com/t5/QlikView-Documents/How-to-create-a-Calendar/ta-p/1491361) from [mov](https://community.qlik.com/t5/user/viewprofilepage/user-id/6636) on the [community.qlik.com](https://community.qlik.com) website
