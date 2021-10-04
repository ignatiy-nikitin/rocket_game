from collections import OrderedDict

from drf_yasg.inspectors import SwaggerAutoSchema
from drf_yasg.utils import no_body
from rest_framework.exceptions import ErrorDetail
from rest_framework.views import exception_handler


class ReadOnly:
    def get_fields(self):
        new_fields = OrderedDict()
        for fieldName, field in super().get_fields().items():
            if not field.write_only:
                new_fields[fieldName] = field
        return new_fields


class WriteOnly:
    def get_fields(self):
        new_fields = OrderedDict()
        for fieldName, field in super().get_fields().items():
            if not field.read_only:
                new_fields[fieldName] = field
        return new_fields


class BlankMeta:
    pass


class ReadWriteAutoSchema(SwaggerAutoSchema):
    def get_view_serializer(self):
        return self._convert_serializer(WriteOnly)

    def get_default_response_serializer(self):
        body_override = self._get_request_body_override()
        if body_override and body_override is not no_body:
            return body_override

        return self._convert_serializer(ReadOnly)

    def _convert_serializer(self, new_class):
        serializer = super().get_view_serializer()
        if not serializer:
            return serializer

        class CustomSerializer(new_class, serializer.__class__):
            class Meta(getattr(serializer.__class__, 'Meta', BlankMeta)):
                ref_name = new_class.__name__ + serializer.__class__.__name__
                # ref_name = serializer.__class__.__name__

        new_serializer = CustomSerializer(data=serializer.data)
        return new_serializer


ERROR_MESSAGES = {
    'not_authenticated': 'Пользователь не авторизован.',
    'authorization': 'Неверный логин или пароль.',
}


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    print('REPONSE', response)

    if response is None:
        return response

    customized_response = {
        'errors': []
    }

    if response is not None:
        for key, value in response.data.items():
            code = value.code if isinstance(value, ErrorDetail) else value[0].code
            message = value if isinstance(value, str) else value[0]
            if ERROR_MESSAGES.get(code):
                message = ERROR_MESSAGES[code]
            error = {
                'message': message,
                'type': code
            }

            if key not in ('detail', 'non_field_errors'):
                print('KEY_', key)
                error['field'] = {
                    'key': key
                }

                if len(value) > 1:
                    error['field']['label'] = value[1]
            customized_response['errors'].append(error)

    response.data = customized_response
    return response


def verbose_errors(obj, super_):
    errors = super_.errors
    verbose_errors = {}
    # errors = super().errors
    # verbose_errors = {}

    fields = {field.name: field.verbose_name for field in
              obj.Meta.model._meta.get_fields() if hasattr(field, 'verbose_name')}

    for field_name, error in errors.items():
        if field_name in fields:
            error.append(str(fields[field_name]))
        verbose_errors[field_name] = error

    return verbose_errors


# -

class CurrentUserCompanyDefault:
    requires_context = True

    def __call__(self, serializer_field):
        return serializer_field.context['request'].user.company

    def __repr__(self):
        return '%s()' % self.__class__.__name__
