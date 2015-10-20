from flask_cache import Cache
cache = Cache(config={'CACHE_TYPE': 'filesystem', 'CACHE_DIR': '/tmp'})
