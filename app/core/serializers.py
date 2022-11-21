# DRF
from rest_framework import serializers


class UUIDSerializer(serializers.Serializer):
    """This serializer is used wherever we need to validate/input a UUID."""

    id = serializers.UUIDField()


class OptionalUUIDSerializer(serializers.Serializer):
    """This serializer is used wherever we need to validate/input \
        a UUID which is optional."""

    id = serializers.UUIDField(required=False)


class RequiredNameSerializer(serializers.Serializer):
    """This serializer is used wherever we need to validate/input a name."""

    name = serializers.CharField()


class BulkResponseSerializer(serializers.Serializer):
    """This serializer is used for mostly all the bulk APIs."""

    operation_success = serializers.BooleanField()
    reason = serializers.CharField()


class BulkIDResponseSerializer(UUIDSerializer, BulkResponseSerializer):
    """This serializer combines the BulkResponseSerializer and UUIDSerializer.\
         This common when we need to return id in\
    response to a bulk API as well."""

    pass


class RequiredIDNameSerializer(UUIDSerializer, RequiredNameSerializer):
    """This serializer combines the NameSerializer and UUIDSerializer."""

    pass


class ManyInitSerializer(serializers.Serializer):
    """This serializer is a generic serializer which is used wherever we\
         define a list serializer inside a normal \
        serializer."""

    @classmethod
    def many_init(cls, *args, **kwargs):
        kwargs["child"] = cls()
        return cls.ListSerializer(*args, **kwargs)


class ReturnNoneSerializer(serializers.Serializer):
    """This serializer is used where create/update functions return None."""

    def save(self, **kwargs):
        assert hasattr(
            self, "_errors"
        ), "You must call `.is_valid()` \
            before calling `.save()`."

        assert (
            not self.errors
        ), "You cannot call `.save()` \
            on a serializer with invalid db_data"

        # Guard against incorrect use of `serializer.save(commit=False)`
        assert "commit" not in kwargs, (
            "'commit' is not a valid keyword argument to the 'save()' method. "
            "If you need to access data\
                 before committing to the database then "
            "inspect 'serializer.validated_data' instead. "
            "You can also pass additional\
                 keyword arguments to 'save()' if you "
            "need to set extra attributes on the saved model instance. "
            "For example: 'serializer.save(owner=request.user)'.'"
        )

        assert not hasattr(self, "_data"), (
            "You cannot call `.save()` after accessing `serializer.data`."
            "If you need to access data before\
                 committing to the database then "
            "inspect 'serializer.validated_data' instead. "
        )

        validated_data = {**self.validated_data, **kwargs}

        if self.instance is not None:
            self.instance = self.update(self.instance, validated_data)
        else:
            self.instance = self.create(validated_data)

        return self.instance
