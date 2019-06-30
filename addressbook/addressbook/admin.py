from django.contrib import admin

from .models import Contacts, PhoneNumber, Address


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    """Contacts admin model."""

    list_display = (
        "first_name",
        "last_name",
        "phone_number",
        "address",
    )

    autocomplete_fields = (
        "address",
        "phone_number",
    )

    search_fields = ("first_name", "last_name")


@admin.register(PhoneNumber)
class PhoneNumbersAdmin(admin.ModelAdmin):
    """Phone numbers admin model"""
    list_display = (
        "number",
        "country_code",
    )

    search_fields = ("number",)


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    """Address admin model"""

    list_display = (
        "line_1",
        "line_2",
        "city",
        "post_code",
        "country",
    )

    search_fields = ("city", "post_code", "country")
