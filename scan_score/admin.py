from django.contrib import admin

# Register your models here.
from scan_score.models import Document, AnswerFile, TestType, TestName, TestSection, Question, PercentileFile, Percentile



class TestTypeAdmin(admin.ModelAdmin):

    list_display = ( 'name',)
    # list_display_links = ('id', 'name')
    # search_fields = ('name',)
    list_per_page = 25


class TestNameAdmin(admin.ModelAdmin):

    list_display = ( 'name',)
    # list_display_links = ('id', 'section_no')
    search_fields = ('name',)

class TestSectionAdmin(admin.ModelAdmin):

    list_display = ( 'section_number', 'section_type')
    # list_display_links = ('id', 'name')
    # search_fields = ('name',)
    list_per_page = 25

class QuestionAdmin(admin.ModelAdmin):

    list_display = ('question_number', 'answer_key')
    # list_display_links = ( 'name')
    # search_fields = ('name',)
    list_per_page = 25

class PercentileAdmin(admin.ModelAdmin):

    list_display = ('composite_score', 'percentile')
    # list_display_links = ( 'name')
    # search_fields = ('name',)
    list_per_page = 25

class DocumentAdmin(admin.ModelAdmin):

    list_display = ('document', 'uploaded_at')
    # list_display_links = ( 'name')
    # search_fields = ('name',)
    list_per_page = 25

admin.site.register(AnswerFile)
admin.site.register(TestType, TestTypeAdmin)
admin.site.register(TestName, TestNameAdmin)
admin.site.register(TestSection, TestSectionAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(PercentileFile)
admin.site.register(Percentile, PercentileAdmin)
admin.site.register(Document, DocumentAdmin)

