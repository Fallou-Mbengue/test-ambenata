from django.urls import reverse
from django.contrib import admin
from django.utils.html import format_html

from .models import Apply, Certificate, Category, Offer, Experience

admin.site.register(Certificate)
admin.site.register(Experience)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # model = Category
    list_per_page = 10
    list_filter = ["title"]
    list_display = ['title']
    list_display_links = ['title']
    fieldsets = (
        # (
        #     'Categorie', {
        #         'classes': ('collapse',),
        #         'fields': (
        #            'title',
        #            'slug'
        #         )
        #     }
        # ),
    )
    prepopulated_fields = {
        "slug": ("title",)
    }


@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    model = Offer
    list_per_page = 10
    date_hierarchy = "created"
    fieldsets = (
        (
            'Offer information', {
                'classes': ('collapse',),
                'fields': (
                    'user',
                    ('title', 'slug'),
                    #    'category',
                    'offer_type',
                    'is_published',
                )
            }
        ),
        (
            'Offer Description', {
                'classes': ('collapse',),
                'fields': (
                    'document_desc',
                    'education_level',
                    'content',
                    'date_validation',
                )
            }
        ),
    )
    list_display = [
        'user', 'title',
        # 'category',
        'offer_type',
        'education_level',
        'created',
        'is_published'
    ]
    list_display_links = ['user', 'title']
    # list_filter = ["category", "is_published"]
    list_editable = ["is_published"]
    search_fields = (
        "user",
        "title",
        "created"
    )
    readonly_fields = [
        'user',
        # 'category',
        'content',
        'date_validation'
    ]
    prepopulated_fields = {
        "slug": ("title",)
    }


@admin.register(Apply)
class ApplyAdmin(admin.ModelAdmin):
    model = Apply
    list_per_page = 10
    date_hierarchy = "created"
    fieldsets = (
        (
            'Information sur la candidature', {
                'classes': ('collapse',),
                'fields': (
                    'candidate',
                    'offer',
                    'status'
                )
            }
        ),
    )
    list_display = [
        'candidate', 'offer',
        'created', 'status'
    ]
    list_display_links = ['candidate', 'offer']
    list_filter = ["offer", "status"]
    search_fields = (
        "offer",
        "status",
        "created"
    )
    readonly_fields = [
        'candidate',
        'offer',
        'status',
    ]
