from enum import Enum
from toloka.client.primitives.base import BaseTolokaObject
from typing import (
    Any,
    Dict,
    List,
    Optional
)

class FieldType(Enum):
    """An enumeration.
    """

    BOOLEAN = 'boolean'
    STRING = 'string'
    FLOAT = 'float'
    INTEGER = 'integer'
    URL = 'url'
    FILE = 'file'
    COORDINATES = 'coordinates'
    JSON = 'json'
    ARRAY_BOOLEAN = 'array_boolean'
    ARRAY_STRING = 'array_string'
    ARRAY_INTEGER = 'array_integer'
    ARRAY_FLOAT = 'array_float'
    ARRAY_URL = 'array_url'
    ARRAY_FILE = 'array_file'
    ARRAY_COORDINATES = 'array_coordinates'
    ARRAY_JSON = 'array_json'


class FieldSpec(BaseTolokaObject):
    """A base class for field specifications used in project's `input_spec` and `output_spec`
    for input and respose data validation specification respectively. Use subclasses of this
    class defined below to define the data type (string, integer, URL, etc.) and specify
    validation parameters (such as string length).

    Attributes:
        required: Whether the object or input field is required
        hidden: Whether or not to hide the input value field from the user
    """

    def __init__(
        self,
        *,
        required: Optional[bool] = True,
        hidden: Optional[bool] = False
    ) -> None:
        """Method generated by attrs for class FieldSpec.
        """
        ...

    _unexpected: Optional[Dict[str, Any]]
    required: Optional[bool]
    hidden: Optional[bool]


class BooleanSpec(FieldSpec):
    """A boolean field specification

    Attributes:
        required: Whether the object or input field is required
        hidden: Whether or not to hide the input value field from the user
        allowed_values: Allowed values
    """

    def __init__(
        self,
        *,
        required: Optional[bool] = True,
        hidden: Optional[bool] = False,
        allowed_values: Optional[List[bool]] = None
    ) -> None:
        """Method generated by attrs for class BooleanSpec.
        """
        ...

    _unexpected: Optional[Dict[str, Any]]
    required: Optional[bool]
    hidden: Optional[bool]
    allowed_values: Optional[List[bool]]


class StringSpec(FieldSpec):
    """A string field specification

    Attributes:
        required: Whether the object or input field is required
        hidden: Whether or not to hide the input value field from the user
        min_length: Minimum length of the string
        max_length: Maximum length of the string
        allowed_values: Allowed values
    """

    def __init__(
        self,
        *,
        required: Optional[bool] = True,
        hidden: Optional[bool] = False,
        min_length: Optional[int] = None,
        max_length: Optional[int] = None,
        allowed_values: Optional[List[str]] = None
    ) -> None:
        """Method generated by attrs for class StringSpec.
        """
        ...

    _unexpected: Optional[Dict[str, Any]]
    required: Optional[bool]
    hidden: Optional[bool]
    min_length: Optional[int]
    max_length: Optional[int]
    allowed_values: Optional[List[str]]


class IntegerSpec(FieldSpec):
    """An integer field specification

    Attributes:
        required: Whether the object or input field is required
        hidden: Whether or not to hide the input value field from the user
        min_value: Minimum value of the number
        max_value: Maximum value of the number
        allowed_values: Allowed values
    """

    def __init__(
        self,
        *,
        required: Optional[bool] = True,
        hidden: Optional[bool] = False,
        min_value: Optional[int] = None,
        max_value: Optional[int] = None,
        allowed_values: Optional[List[int]] = None
    ) -> None:
        """Method generated by attrs for class IntegerSpec.
        """
        ...

    _unexpected: Optional[Dict[str, Any]]
    required: Optional[bool]
    hidden: Optional[bool]
    min_value: Optional[int]
    max_value: Optional[int]
    allowed_values: Optional[List[int]]


class FloatSpec(FieldSpec):
    """An floating point field specification

    Attributes:
        required: Whether the object or input field is required
        hidden: Whether or not to hide the input value field from the user
        min_value: Minimum value of the number
        max_value: Maximum value of the number
    """

    def __init__(
        self,
        *,
        required: Optional[bool] = True,
        hidden: Optional[bool] = False,
        min_value: Optional[float] = None,
        max_value: Optional[float] = None
    ) -> None:
        """Method generated by attrs for class FloatSpec.
        """
        ...

    _unexpected: Optional[Dict[str, Any]]
    required: Optional[bool]
    hidden: Optional[bool]
    min_value: Optional[float]
    max_value: Optional[float]


class UrlSpec(FieldSpec):
    """A url field specification

    Attributes:
        required: Whether the object or input field is required
        hidden: Whether or not to hide the input value field from the user
    """

    def __init__(
        self,
        *,
        required: Optional[bool] = True,
        hidden: Optional[bool] = False
    ) -> None:
        """Method generated by attrs for class UrlSpec.
        """
        ...

    _unexpected: Optional[Dict[str, Any]]
    required: Optional[bool]
    hidden: Optional[bool]


class FileSpec(FieldSpec):
    """A file field specification (only for output data)

    Attributes:
        required: Whether the object or input field is required
        hidden: Whether or not to hide the input value field from the user
    """

    def __init__(
        self,
        *,
        required: Optional[bool] = True,
        hidden: Optional[bool] = False
    ) -> None:
        """Method generated by attrs for class FileSpec.
        """
        ...

    _unexpected: Optional[Dict[str, Any]]
    required: Optional[bool]
    hidden: Optional[bool]


class CoordinatesSpec(FieldSpec):
    """Geographical coordinates field specification, such as “53.910236,27.531110

    Attributes:
        required: Whether the object or input field is required
        hidden: Whether or not to hide the input value field from the user
        current_location: put the user's current coordinates in the field (true/false).
            Used in tasks for the mobile app.
    """

    def __init__(
        self,
        *,
        required: Optional[bool] = True,
        hidden: Optional[bool] = False,
        current_location: Optional[bool] = None
    ) -> None:
        """Method generated by attrs for class CoordinatesSpec.
        """
        ...

    _unexpected: Optional[Dict[str, Any]]
    required: Optional[bool]
    hidden: Optional[bool]
    current_location: Optional[bool]


class JsonSpec(FieldSpec):
    """A JSON object field specification

    Attributes:
        required: Whether the object or input field is required
        hidden: Whether or not to hide the input value field from the user
    """

    def __init__(
        self,
        *,
        required: Optional[bool] = True,
        hidden: Optional[bool] = False
    ) -> None:
        """Method generated by attrs for class JsonSpec.
        """
        ...

    _unexpected: Optional[Dict[str, Any]]
    required: Optional[bool]
    hidden: Optional[bool]


class ArrayBooleanSpec(BooleanSpec):
    """A boolean array field specification

    Attributes:
        required: Whether the object or input field is required
        hidden: Whether or not to hide the input value field from the user
        allowed_values: Allowed values
        min_size: Minimum number of elements in the array
        max_size: Maximum number of elements in the array
    """

    def __init__(
        self,
        *,
        required: Optional[bool] = True,
        hidden: Optional[bool] = False,
        allowed_values: Optional[List[bool]] = None,
        min_size: Optional[int] = None,
        max_size: Optional[int] = None
    ) -> None:
        """Method generated by attrs for class ArrayBooleanSpec.
        """
        ...

    _unexpected: Optional[Dict[str, Any]]
    required: Optional[bool]
    hidden: Optional[bool]
    allowed_values: Optional[List[bool]]
    min_size: Optional[int]
    max_size: Optional[int]


class ArrayStringSpec(StringSpec):
    """A string array field specification

    Attributes:
        required: Whether the object or input field is required
        hidden: Whether or not to hide the input value field from the user
        min_length: Minimum length of the string
        max_length: Maximum length of the string
        allowed_values: Allowed values
        min_size: Minimum number of elements in the array
        max_size: Maximum number of elements in the array
    """

    def __init__(
        self,
        *,
        required: Optional[bool] = True,
        hidden: Optional[bool] = False,
        min_length: Optional[int] = None,
        max_length: Optional[int] = None,
        allowed_values: Optional[List[str]] = None,
        min_size: Optional[int] = None,
        max_size: Optional[int] = None
    ) -> None:
        """Method generated by attrs for class ArrayStringSpec.
        """
        ...

    _unexpected: Optional[Dict[str, Any]]
    required: Optional[bool]
    hidden: Optional[bool]
    min_length: Optional[int]
    max_length: Optional[int]
    allowed_values: Optional[List[str]]
    min_size: Optional[int]
    max_size: Optional[int]


class ArrayIntegerSpec(IntegerSpec):
    """An integer array field specification

    Attributes:
        required: Whether the object or input field is required
        hidden: Whether or not to hide the input value field from the user
        min_value: Minimum value of the number
        max_value: Maximum value of the number
        allowed_values: Allowed values
        min_size: Minimum number of elements in the array
        max_size: Maximum number of elements in the array
    """

    def __init__(
        self,
        *,
        required: Optional[bool] = True,
        hidden: Optional[bool] = False,
        min_value: Optional[int] = None,
        max_value: Optional[int] = None,
        allowed_values: Optional[List[int]] = None,
        min_size: Optional[int] = None,
        max_size: Optional[int] = None
    ) -> None:
        """Method generated by attrs for class ArrayIntegerSpec.
        """
        ...

    _unexpected: Optional[Dict[str, Any]]
    required: Optional[bool]
    hidden: Optional[bool]
    min_value: Optional[int]
    max_value: Optional[int]
    allowed_values: Optional[List[int]]
    min_size: Optional[int]
    max_size: Optional[int]


class ArrayFloatSpec(FloatSpec):
    """An floating point array field specification

    Attributes:
        required: Whether the object or input field is required
        hidden: Whether or not to hide the input value field from the user
        min_value: Minimum value of the number
        max_value: Maximum value of the number
        min_size: Minimum number of elements in the array
        max_size: Maximum number of elements in the array
    """

    def __init__(
        self,
        *,
        required: Optional[bool] = True,
        hidden: Optional[bool] = False,
        min_value: Optional[float] = None,
        max_value: Optional[float] = None,
        min_size: Optional[int] = None,
        max_size: Optional[int] = None
    ) -> None:
        """Method generated by attrs for class ArrayFloatSpec.
        """
        ...

    _unexpected: Optional[Dict[str, Any]]
    required: Optional[bool]
    hidden: Optional[bool]
    min_value: Optional[float]
    max_value: Optional[float]
    min_size: Optional[int]
    max_size: Optional[int]


class ArrayUrlSpec(UrlSpec):
    """A url array field specification

    Attributes:
        required: Whether the object or input field is required
        hidden: Whether or not to hide the input value field from the user
        min_size: Minimum number of elements in the array
        max_size: Maximum number of elements in the array
    """

    def __init__(
        self,
        *,
        required: Optional[bool] = True,
        hidden: Optional[bool] = False,
        min_size: Optional[int] = None,
        max_size: Optional[int] = None
    ) -> None:
        """Method generated by attrs for class ArrayUrlSpec.
        """
        ...

    _unexpected: Optional[Dict[str, Any]]
    required: Optional[bool]
    hidden: Optional[bool]
    min_size: Optional[int]
    max_size: Optional[int]


class ArrayFileSpec(FileSpec):
    """A file array field specification (only for output data)

    Attributes:
        required: Whether the object or input field is required
        hidden: Whether or not to hide the input value field from the user
        min_size: Minimum number of elements in the array
        max_size: Maximum number of elements in the array
    """

    def __init__(
        self,
        *,
        required: Optional[bool] = True,
        hidden: Optional[bool] = False,
        min_size: Optional[int] = None,
        max_size: Optional[int] = None
    ) -> None:
        """Method generated by attrs for class ArrayFileSpec.
        """
        ...

    _unexpected: Optional[Dict[str, Any]]
    required: Optional[bool]
    hidden: Optional[bool]
    min_size: Optional[int]
    max_size: Optional[int]


class ArrayCoordinatesSpec(CoordinatesSpec):
    """Geographical coordinates array field specification

    Attributes:
        required: Whether the object or input field is required
        hidden: Whether or not to hide the input value field from the user
        current_location: put the user's current coordinates in the field (true/false).
            Used in tasks for the mobile app
        min_size: Minimum number of elements in the array
        max_size: Maximum number of elements in the array
    """

    def __init__(
        self,
        *,
        required: Optional[bool] = True,
        hidden: Optional[bool] = False,
        current_location: Optional[bool] = None,
        min_size: Optional[int] = None,
        max_size: Optional[int] = None
    ) -> None:
        """Method generated by attrs for class ArrayCoordinatesSpec.
        """
        ...

    _unexpected: Optional[Dict[str, Any]]
    required: Optional[bool]
    hidden: Optional[bool]
    current_location: Optional[bool]
    min_size: Optional[int]
    max_size: Optional[int]
