from marshmallow import fields
from marshmallow_dataclass import _native_to_marshmallow

from raiden.storage.serialization.fields import AddressField, BytesField, IntegerToStringField
from raiden.utils.typing import (
    AdditionalHash,
    Address,
    Any,
    BalanceHash,
    BlockExpiration,
    BlockGasLimit,
    BlockHash,
    BlockNumber,
    ChainID,
    ChannelID,
    EncodedData,
    FeeAmount,
    InitiatorAddress,
    LockedAmount,
    LockHash,
    Locksroot,
    MessageID,
    Nonce,
    Optional,
    PaymentAmount,
    PaymentID,
    PaymentNetworkID,
    PaymentWithFeeAmount,
    Secret,
    SecretHash,
    SecretRegistryAddress,
    Signature,
    TargetAddress,
    TokenAddress,
    TokenNetworkAddress,
    TokenNetworkID,
    TransactionHash,
    TransferID,
    Type,
    Union,
)


def determine_union_types(*args) -> Optional[Type[Any]]:
    """
    Handle case where the type is a Union of:
    1. [X, X] (example TokenNetworkID, TokenNetworkAddress),
       in this case we use the same field.
    2. [X, None] for Optional types, we use the field
       of X type.
    """
    first_type = type(args[0])

    for arg in args:
        if type(arg) != first_type:
            return None
    return args[0]


_native_to_marshmallow.update(
    {
        # Addresses
        Address: AddressField,
        InitiatorAddress: AddressField,
        PaymentNetworkID: AddressField,
        SecretRegistryAddress: AddressField,
        TargetAddress: AddressField,
        TokenAddress: AddressField,
        TokenNetworkAddress: AddressField,
        TokenNetworkID: AddressField,
        # Bytes
        EncodedData: BytesField,
        AdditionalHash: BytesField,
        BalanceHash: BytesField,
        BlockHash: BytesField,
        Locksroot: BytesField,
        LockHash: BytesField,
        Secret: BytesField,
        SecretHash: BytesField,
        Signature: BytesField,
        TransactionHash: BytesField,
        # Ints
        BlockExpiration: fields.Int,
        BlockNumber: fields.Int,
        FeeAmount: fields.Int,
        LockedAmount: fields.Int,
        BlockGasLimit: fields.Int,
        MessageID: fields.Int,
        Nonce: fields.Int,
        PaymentAmount: fields.Int,
        PaymentID: fields.Int,
        PaymentWithFeeAmount: fields.Int,
        TransferID: fields.Int,
        # Integers which should be converted to strings
        # This is done for querying purposes as sqlite
        # integer type is smaller than python's.
        ChainID: IntegerToStringField,
        ChannelID: IntegerToStringField,
        # Union
        # Union: determine_union_types,
        Union[TokenNetworkAddress, TokenNetworkID]: AddressField,
    }
)