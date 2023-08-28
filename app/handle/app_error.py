
class AppError(Exception):
    def __init__(self, message, status_code):
        super().__init__(message)
        self.status_code = status_code


class InvalidImageError(AppError):
    def __init__(self, message="Invalid image file format"):
        super().__init__(message, 400)


class NoImageError(AppError):
    def __init__(self, message="No image file uploaded"):
        super().__init__(message, 400)
