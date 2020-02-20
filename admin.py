from django.contrib import admin
from myapp.models import Account, Subject_range, Subject_code, Subject, Evaluation

admin.site.register(Account)
admin.site.register(Subject_range)
admin.site.register(Subject_code)
admin.site.register(Subject)
admin.site.register(Evaluation)