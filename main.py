import imp
from Common import file_importer
import Days

day = 1

list_of_strings = (file_importer.get_strings(day))

Days.day1.run_day(list_of_strings)