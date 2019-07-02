# main.py
import json_key_remover

remove = json_key_remover.JSON_KEY_REMOVER
remove.import_json("./user.json")
remove.del_daily_zero_coordinates()