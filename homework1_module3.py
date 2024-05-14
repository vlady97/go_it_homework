from datetime import datetime, date

def is_valid_date_format(date_string):
   try: 
      datetime.strptime(date_string, "%Y-%m-%d")
      return True
   except ValueError:
      return False
   

def get_days_from_today(date):
   if not is_valid_date_format(date):
      return "Неправильний формат дати."
   
   input_date = datetime.strptime(date, "%Y-%m-%d").date()
   today = date.today()
   days_difference = (input_date - today).days
   return days_difference
