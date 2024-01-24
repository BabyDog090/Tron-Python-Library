class BadAddress(ValueError):
    pass


class BadKey(ValueError):
    pass


class BadSignature(ValueError):
    pass


class BadHash(ValueError):
    pass


class ValidationError(Exception):
    pass


class ApiError(Exception):
    pass


class NotFound(ValueError):
    pass


class AddressNotFound(NotFound):
    pass


class TransactionNotFound(NotFound):
    pass


class BlockNotFound(NotFound):
    pass


class AssetNotFound(NotFound):
    pass


class DoubleSpending(TransactionError):
    pass


class BugInJavaTron(Exception):
    pass
