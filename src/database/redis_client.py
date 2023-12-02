import redis
from decouple import config

redis_client = redis.Redis(
    host=config("REDIS_HOSTNAME"),
    port=16552,
    password=config("REDIS_PASSWORD"),
    db=0
)