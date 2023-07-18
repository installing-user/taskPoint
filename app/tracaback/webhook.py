class WebhookSetError(Exception):
    @staticmethod
    def print_error(text_error) -> str:
        return f"Webhook not created: {text_error}"


class WebhookNotDelete(Exception):
    @staticmethod
    def print_error(text_error) -> str:
        return f"Webhook not deleted: {text_error}"


class WebhookGetError(Exception):
    @staticmethod
    def print_error(text_error) -> str:
        return f"Webhook get error: {text_error}"
