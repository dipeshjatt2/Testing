import os

api_id = 22118129
api_hash = os.environ.get("API_HASH", "43c66e3314921552d9330a4b05b18800")
bot_token = os.environ.get("BOT_TOKEN","6530435719:AAHAWHqESgxbjZWVfaN8eM6eqXAMA_sWVxo")
auth_users = os.environ.get("AUTH_USERS", "5203820046")
sudo_users = [int(num) for num in auth_users.split("5203820046,5203820046")]
osowner_users = os.environ.get("OWNER_USERS", "5203820046")
owner_users = [int(num) for num in osowner_users.split(",")]
