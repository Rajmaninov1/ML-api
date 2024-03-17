from abc import ABC, abstractmethod

from fastapi import status


class BaseAPIException(ABC, Exception):
    """Base class for all API exceptions"""

    @property
    @abstractmethod
    def default_message(self) -> str:
        pass

    @property
    @abstractmethod
    def example_message(self) -> str:
        pass

    @property
    @abstractmethod
    def http_status_code(self) -> int:
        pass

    @classmethod
    def get_openapi_response(cls) -> dict:
        return {cls.http_status_code: {'description': cls.example_message}}

    def __init__(self, *args) -> None:
        if args:
            super().__init__(self.default_message.format(*args))
        else:
            super().__init__(self.default_message)


class ExampleHTTPException(BaseAPIException):
    http_status_code = status.HTTP_404_NOT_FOUND
    default_message = 'Example of exception'
    example_message = default_message


class AnotherExampleHTTPException(BaseAPIException):
    http_status_code = status.HTTP_404_NOT_FOUND
    default_message = 'Another example of exception'
    example_message = default_message


class GenericNotFoundHTTPException(BaseAPIException):
    http_status_code = status.HTTP_404_NOT_FOUND
    default_message = '{} not found'
    example_message = default_message


class Generic400HTTPException(BaseAPIException):
    http_status_code = status.HTTP_400_BAD_REQUEST
    default_message = '{}'
    example_message = default_message


class Generic422HTTPException(BaseAPIException):
    http_status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
    default_message = '{}'
    example_message = default_message


class NotSupportedVersion(BaseAPIException):
    http_status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
    default_message = 'Requested quoting parameters version currently is not supported'
    example_message = default_message


class NotCompaniesFound(BaseAPIException):
    http_status_code = status.HTTP_404_NOT_FOUND
    default_message = 'No companies found'
    example_message = default_message


class CompanyNotHaveCustomers(BaseAPIException):
    http_status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
    default_message = 'Company not have any Customer'
    example_message = default_message


class NotUsersFound(BaseAPIException):
    http_status_code = status.HTTP_404_NOT_FOUND
    default_message = 'No users found'
    example_message = default_message


class FavoriteNotFound(BaseAPIException):
    http_status_code = status.HTTP_404_NOT_FOUND
    default_message = 'No favorite found'
    example_message = default_message


class NotCustomersFound(BaseAPIException):
    http_status_code = status.HTTP_404_NOT_FOUND
    default_message = 'No customers found'
    example_message = default_message


class UserNotFound(BaseAPIException):
    http_status_code = status.HTTP_404_NOT_FOUND
    default_message = 'User not found'
    example_message = default_message


class ReportNotFound(BaseAPIException):
    http_status_code = status.HTTP_404_NOT_FOUND
    default_message = 'Report not found'
    example_message = default_message


class OrderEntryNotFound(BaseAPIException):
    http_status_code = status.HTTP_404_NOT_FOUND
    default_message = 'Order entry not found'
    example_message = default_message


class InvoiceNotFound(BaseAPIException):
    http_status_code = status.HTTP_404_NOT_FOUND
    default_message = 'Invoice not found'
    example_message = default_message


class InvoiceFileNotFound(BaseAPIException):
    http_status_code = status.HTTP_404_NOT_FOUND
    default_message = 'Invoice file not found'
    example_message = default_message


class CustomerNotFound(BaseAPIException):
    http_status_code = status.HTTP_404_NOT_FOUND
    default_message = 'Customer not found'
    example_message = default_message


class ParametersNotFound(BaseAPIException):
    http_status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
    default_message = 'parameters not configured in tabi connect'
    example_message = default_message


class CustomerNotHaveUser(BaseAPIException):
    http_status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
    default_message = 'Customer does not have an associated user'
    example_message = default_message


class CustomerNotHaveVersion(BaseAPIException):
    http_status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
    default_message = 'Customer do not have a quoting version'
    example_message = default_message


class UserNotHaveCustomers(BaseAPIException):
    http_status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
    default_message = 'User not have any Customer'
    example_message = default_message


class ObjectIDIsNotValid(BaseAPIException):
    http_status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
    default_message = 'The ObjectId is not a 12-byte BSON type hexadecimal string.'
    example_message = default_message


class BadJSONParameter(BaseAPIException):
    http_status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
    default_message = 'One or more parameters stored in the database is not a valid JSON string'
    example_message = default_message


class DuplicatedUser(BaseAPIException):
    http_status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
    default_message = 'User already exists'
    example_message = default_message


class NoFieldsModified(BaseAPIException):
    http_status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
    default_message = 'No fields to modify were sent'
    example_message = default_message
