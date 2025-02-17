from decimal import Decimal
from toloka.client.primitives.base import BaseTolokaObject
from typing import (
    Any,
    Dict,
    Optional
)

class Requester(BaseTolokaObject):
    """Contains information about the customer and the account balance

    Attributes:
        id: Requester ID.
        balance: Account balance in dollars.
        public_name: The requester's name in Toloka.
        company:
    """

    class Company(BaseTolokaObject):
        def __init__(
            self,
            *,
            id: Optional[str] = None,
            superintendent_id: Optional[str] = None
        ) -> None:
            """Method generated by attrs for class Requester.Company.
            """
            ...

        _unexpected: Optional[Dict[str, Any]]
        id: Optional[str]
        superintendent_id: Optional[str]

    def __init__(
        self,
        *,
        id: Optional[str] = None,
        balance: Optional[Decimal] = None,
        public_name: Optional[Dict[str, str]] = None,
        company: Optional[Company] = None
    ) -> None:
        """Method generated by attrs for class Requester.
        """
        ...

    _unexpected: Optional[Dict[str, Any]]
    id: Optional[str]
    balance: Optional[Decimal]
    public_name: Optional[Dict[str, str]]
    company: Optional[Company]
