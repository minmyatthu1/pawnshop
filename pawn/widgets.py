from django.forms import DateInput

class DatePicker(DateInput):
    template_name = 'datepicker.html'
