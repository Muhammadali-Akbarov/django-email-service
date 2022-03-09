import logging

from django.core.cache import cache
from django.conf import settings
from email_api.models import SysParams

cache_model = SysParams
cache_obj = cache
logger = logging.getLogger(__name__)


class SysParams(object):
    key_title = 'sys_params'
    key_lifetime = settings.CACHE_TTL

    def __init__(self):
        try:
            self.model = cache_model
            self.cache = cache_obj
        except NameError:
            pass

    def as_dict(self):
        result = self.__get_cache()
        if not result:
            result = {}
            params = self.model.objects.all()
            for param in params:
                result[param.param.upper()] = param.value
            self.__set_cache(result)
        return result

    def get_extra(self, parameter):
        parameter = parameter.lower()
        key_title = 'extra_sys_params:' + parameter
        result = self.cache.get(key_title)
        if not result:
            try:
                param = self.model.objects.get(param=parameter)
                result = param.value
            except Exception as ex:
                logger.error("Error while get system param {}. Details ex={}".format(parameter, ex))
                return 0
            self.cache.set(key_title, result, 60)  # сохраняю на 1 минуту

        return result

    def __get_cache(self):
        return self.cache.get(self.key_title)

    def __set_cache(self, data):
        lifetime = self.key_lifetime
        return self.cache.set(self.key_title, data, lifetime)

    def clear_cache(self):
        self.cache.delete(self.key_title)


sys_params = SysParams()
