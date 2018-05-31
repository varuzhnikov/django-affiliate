# -*- coding: utf-8 -*-
def is_new_ip(c_key, cache, ip):
    aid_ip_pool = cache.get(c_key)
    ip_new = True
    if aid_ip_pool:
        if isinstance(aid_ip_pool, set):
            ip_new = ip not in aid_ip_pool
    if not aid_ip_pool:
        aid_ip_pool = set()
    return ip_new, aid_ip_pool
