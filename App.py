from flask import Flask, render_template, request, redirect, url_for
import shelve, cookie, inventory
from Forms import importForm

app = Flask(__name__, static_folder="static")
cookieDict = cookie.cookie()


@app.route('/')
def home():
    return render_template("home.html", cookieDict=cookieDict)


@app.route("/about")
def about():
    return render_template("about.html", cookieDict=cookieDict)


@app.route("/inventory")
def inventory():
    invDict = {}
    db = shelve.open("inventory.db", "c")
    invDict = db["inventory"]
    db.close()

    stockList = []
    for keys in invDict:
        good = invDict.get(keys)
        stockList.append(good)
    print(stockList)
    return render_template("inventory.html", cookieDict=cookieDict, stockList=stockList, count=len(invDict))


@app.route("/importForm", methods=["GET", "POST"])
def importFormPage():
    ImportForm = importForm(request.form)

    if request.method == "POST" and ImportForm.validate():
        invDict = {}
        db = shelve.open("inventory.db", "c")
        invDict = db["inventory"]
        name = str(ImportForm.brand.data + " " + ImportForm.productName.data).split()
        name = " ".join(name).capitalize()
        good = inventory.Inventory(name, ImportForm.quantity.data, ImportForm.costPrice.data, ImportForm.sellPrice.data)
        invDict[good.get_stockID()] = good
        db["inventory"] = invDict
        return redirect(url_for("inventory"))
    return render_template("importGoods.html", cookieDict=cookieDict, form=ImportForm)


@app.route("/signup")
def signup():
    return render_template("signup.html", cookieDict=cookieDict)

if __name__ == '__main__':
    app.run()
