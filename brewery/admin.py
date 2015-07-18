from django.contrib import admin

from .models import Batch
from .models import Sensor
from .models import Note
from .models import Measurement

class BatchAdmin(admin.ModelAdmin):
    list_display=('name','recipe','date_init','date_end')

class NoteAdmin(admin.ModelAdmin):
    list_display=('batch','date','content')

class SensorAdmin(admin.ModelAdmin):
    list_display=('name','description','unit')

class MeasurementAdmin(admin.ModelAdmin):
    list_display=('date','batch','sensor','value')

admin.site.register(Batch,BatchAdmin)
admin.site.register(Note,NoteAdmin)
admin.site.register(Sensor,SensorAdmin)
admin.site.register(Measurement,MeasurementAdmin)
