import phonenumbers
from phonenumbers import geocoder, carrier, timezone


def lookup_phone(number):
    try:
        parsed = phonenumbers.parse(number, None)

        print("\n" + "=" * 45)
        print("       PHONE NUMBER OSINT")
        print("=" * 45)

        print(
            "Formatted:",
            phonenumbers.format_number(
                parsed,
                phonenumbers.PhoneNumberFormat.INTERNATIONAL
            )
        )

        print("Country Code:", parsed.country_code)
        print("National Number:", parsed.national_number)

        print(
            "Valid:",
            phonenumbers.is_valid_number(parsed)
        )

        print(
            "Possible:",
            phonenumbers.is_possible_number(parsed)
        )

        print(
            "Region:",
            geocoder.description_for_number(parsed, "en") or "Unknown"
        )

        print(
            "Carrier:",
            carrier.name_for_number(parsed, "en") or "Unknown"
        )

        zones = timezone.time_zones_for_number(parsed)

        print(
            "Time Zone:",
            ", ".join(zones) if zones else "Unknown"
        )

        print("=" * 45)

    except phonenumbers.NumberParseException as e:
        print("\nInvalid phone number:")
        print(e)


number = input("Enter phone number with country code: ")

lookup_phone(number)