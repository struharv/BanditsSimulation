import csv
import os
from datetime import datetime
from zoneinfo import ZoneInfo

from bandits.Simulator import Simulator


class ElectricityMaps2:

    COUNTRIES = [("AT", "Europe/Vienna"),
                 ("CZ", "Europe/Prague"),
                 ("FR", "Europe/Madrid"),
                 ("HK", "Hongkong"),
                 ("HU", "Europe/Budapest"),
                 ("ES", "Europe/Madrid"),
                 ("US-NY-NYIS", "Asia/Qatar"),
                 ("NZ", "Pacific/Auckland"),
                 ("PT", "Europe/Lisbon")]

    default_timezone = "Europe/Prague"

    def __init__(self):
        self.database = None
        self.aligned = {}

    def read_file(self, filename_in: str, timezone=None):
        res = []

        with open(filename_in) as csvfile:
            next(csvfile, None)
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in spamreader:
                datetime_split = row[0].split(" ")
                date_split = datetime_split[0].split("-")
                time_split = datetime_split[1].split(":")

                year = int(date_split[0])
                month = int(date_split[1])
                day = int(date_split[2])

                hour = int(time_split[0])
                mins = int(time_split[1])

                try:
                    renewable = float(row[7]) / 100
                except:
                    renewable = 0

                if timezone:
                    year, month, day, hour, mins = ElectricityMaps2.convert_timezone(timezone, year, month, day, hour, mins, self.default_timezone)

                res += [{"year": year,
                         "month": month,
                         "day": day,

                         "hour": hour,
                         "min": mins,
                         "renewable": renewable}]


        return res

    def read_all_files(self):
        self.database = {}

        for country in self.COUNTRIES:
            code = country[0]
            timezone = country[1]

            path = os.path.dirname(__file__)
            timeserie = self.read_file(f"{path}/data/{code}_2024_hourly.csv", timezone)

            self.database[code] = {"serie": timeserie, "timezone": timezone}

    @staticmethod
    def convert_timezone(timezone_from: str, year: int, month: int, day: int, hours: int, mins: int, timezone_to: str):
        original = datetime(year, month, day, hours, mins, tzinfo=ZoneInfo(timezone_from))
        converted = original.astimezone(ZoneInfo(timezone_to))

        return (int(converted.strftime("%Y")),
                int(converted.strftime("%m")),
                int(converted.strftime("%d")),
                int(converted.strftime("%H")),
                int(converted.strftime("%M")))

    def get_day(self, country, year, month, day, limit=25):
        res = []

        inRead = False

        for item in self.database[country]["serie"]:
            if year == item["year"] and month == item["month"] and day == item["day"]:
                inRead = True

            if inRead:
                res += [item]

            if len(res) >= limit:
                return res

        return res


class ElectricityMap2Node:

    @staticmethod
    def toGreen(country, year, month, day, limit=25):
        res = []

        elMap = ElectricityMaps2()
        elMap.read_all_files()
        entries = elMap.get_day(country, year, month, day, limit)

        for i in range(len(entries)):
            entry = entries[i]
            #[(7 * NewSimulator.HOUR_SECONDS, 0.0),
            # (12 * NewSimulator.HOUR_SECONDS, 0.5), (14 * NewSimulator.HOUR_SECONDS, 0.5), (19 * NewSimulator.HOUR_SECONDS, 0.0)]
            #print(entry)

            res += [[i * Simulator.HOUR_SECONDS, entry["renewable"]]]

        return res

def main():
    #elMap = ElectricityMaps2()
    #elMap.read_all_files()
    #elMap.get_day("ES", 2024, 8, 20)
    # elMap.export(2024, 8, 20)

    countryEs = ElectricityMap2Node.toGreen("ES", 2024, 11, 20)
    pass

if __name__ == "__main__":
    main()