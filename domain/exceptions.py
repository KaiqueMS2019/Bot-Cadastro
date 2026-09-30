class AutomationError(Exception):
    pass


class WebAutomationError(AutomationError):
    pass


class IdentityExtractionError(WebAutomationError):
    pass


class CatalogExtractionError(WebAutomationError):
    pass


class DataValidationError(AutomationError):
    pass