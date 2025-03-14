from dotenv import dotenv_values

config=dotenv_values(".envv")

print(config["api"])