from utils.mapping import print_error


from core.entities.config.types import T_ENTITY


def _invalid_conf(conf: T_ENTITY) -> bool:
    if \
    not isinstance(conf, dict) \
    or not isinstance(conf['method'], str) \
    or not isinstance(conf['params'], dict) \
    or not isinstance(conf['delivered_fields'], list):
        print_error('Некорректно задан entity')
        return True
    return False