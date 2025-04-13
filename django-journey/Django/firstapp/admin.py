from django.contrib import admin
from .models import firstappVarity, AppReview, Store, AppCertificate

# Register your models here.
class firstappReviewInline(admin.TabularInline):
    model = AppReview
    extra = 2

class firstappVarityAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'date_added')
    search_fields = ('name', 'description')
    list_filter = ('type', 'date_added')
    inlines = [firstappReviewInline]

class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    search_fields = ('name', 'location')
    filter_horizontal = ('app_varity',)
    list_filter = ('app_varity',)

class firstappCertificateAdmin(admin.ModelAdmin):
    list_display = ('app', 'certificate_number', 'issue_date', 'valid_until')
    search_fields = ('app__name', 'certificate_number')
    list_filter = ('issue_date', 'valid_until')
    raw_id_fields = ('app',)

admin.site.register(firstappVarity, firstappVarityAdmin)
admin.site.register(AppReview)
admin.site.register(Store, StoreAdmin)
admin.site.register(AppCertificate, firstappCertificateAdmin)
#admin.site.register(firstappVarity)
