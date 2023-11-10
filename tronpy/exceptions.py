class BadAddress(ValueError):
    pass


class BadKey(ValueError):
    pass


class BadSignature(ValueError):
    pass


class BadHash(ValueError):
    pass


class TaposError(ValueError):
    pass


class UnknownError(Exception):
    pass


class TransactionError(Exception):

class BlockNotFound(NotFound):
    pass


class AssetNotFound(NotFound):
    pass


class DoubleSpending(TransactionError):
    pass


class BugInJavaTron(Exception):
    pass
