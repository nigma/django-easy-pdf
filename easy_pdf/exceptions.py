class EasyPDFError(BaseException):
    """Base error class
    """


class UnsupportedMediaPathException(EasyPDFError):
    """Resource not found or unavailable"""


class PDFRenderingError(EasyPDFError):
    """PDF Rendering error. Check HTML template for errors"""

    def __init__(self, message, content, log, *args, **kwargs):
        super().__init__(message, *args, **kwargs)
        self.content = content
        self.log = log
