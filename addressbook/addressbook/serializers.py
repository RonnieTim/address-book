from rest_framework import serializers

from .models import PhoneNumber, Address, Contacts


class PhoneNumberSerializer(serializers.ModelSerializer):

    class Meta:
        model = PhoneNumber

        fields = (
            "number",
            "country_code",
        )


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address

        fields = (
            "line_1",
            "line_2",
            "city",
            "post_code",
            "country",
        )


class ContactsSerializer(serializers.ModelSerializer):

    phone_number = PhoneNumberSerializer()
    address = AddressSerializer()

    class Meta:
        model = Contacts

        fields = (
            "first_name",
            "last_name",
            "phone_number",
            "address",
        )

    def create(self, validated_data):
        """Create address and phone number."""
        # phone number creation
        phone_number_data = validated_data.pop("phone_number")
        phone_number = PhoneNumber.objects.create(**phone_number_data)
        validated_data["phone_number"] = phone_number

        # address creation
        address_data = validated_data.pop('address')
        address = Address.objects.create(**address_data)
        validated_data["address"] = address

        contacts = Contacts.objects.create(**validated_data)
        return contacts
