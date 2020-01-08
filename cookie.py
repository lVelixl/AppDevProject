import shelve


def cookie():
    db = {}
    cookieDb = shelve.open("cookie.db", "w")
    try:
        db = cookieDb["cookie"]
    except:
        print("ABC")

    db["cookie"] = "creatitools@creatitools.org"
    cookieDb.close()
    return db


def SIGNOUT(cookieDict):
    cookieDb = shelve.open("cookie.db", "w")
    cookieDict["cookie"] = ","
    cookieDb["cookie"] = cookieDict
    cookieDb.close()

