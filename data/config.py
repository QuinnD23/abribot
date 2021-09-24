from environs import Env

env = Env()
env.read_env()

token = env.str("TOKEN")
admin_id = env.str("ADMIN_ID")
hostc = env.str("PG_HOST")
userc = env.str("PG_USER")
passc = env.str("PG_PASS")