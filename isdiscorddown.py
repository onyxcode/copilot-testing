# find out if discord is down
def isonline():
    import requests
    try:
        requests.get("https://discordapp.com/api/v6/users/@me", timeout=5)
        return True
    except:
        return False

# if discord is down, print a message, otherwise, print a message
if isonline():
    print("Discord is up")
else:
    print("Discord is down")
