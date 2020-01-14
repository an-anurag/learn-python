"""
Convert string-hex to int, return integer if it can be convertible or else return passed string
Create date regex with named group - (11,01/14/20,07:20:45,) - (?P<day>\d{2})\/(?P<month>\d{2})\/(?P<year>\d{2})[,\s+]?(?P<hour>\d{2}):(?P<minute>\d{2}):(?P<second>\d{2})
"""