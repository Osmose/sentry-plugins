from sentry.plugins.validators import URLValidator


def OptionalURLValidator(value, **kwargs):
    """
    Validates URLs, but allows for empty strings, unlike the default URL
    validator.
    """
    if not value:
        return value
    return URLValidator(value, **kwargs)
