from flask import Flask, render_template, request, redirect, url_for
import shelve, cookie, Forms
import inventory as inv
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
    return render_template("inventory.html", cookieDict=cookieDict, stockList=stockList, count=len(invDict))


@app.route("/importForm", methods=["GET", "POST"])
def importFormPage():
    ImportForm = Forms.importForm(request.form)

    if request.method == "POST" and ImportForm.validate():
        invDict = {}
        db = shelve.open("inventory.db", "c")
        invDict = db["inventory"]
        good = inv.Inventory(ImportForm.brand.data, ImportForm.productName.data, ImportForm.quantity.data, ImportForm.costPrice.data, ImportForm.sellPrice.data)
        invDict[good.get_stockID()] = good
        db["inventory"] = invDict
        db.close()
        return redirect(url_for("inventory"))
    return render_template("importGoods.html", cookieDict=cookieDict, form=ImportForm)


@app.route("/updateStockInfo/<int:id>", methods=["GET", "POST"])
def updateStockInfo(id):
    updateStockInfoForm = Forms.updateForm(request.form)

    if request.method == "POST" and updateStockInfoForm.validate():
        invDict = {}
        db = shelve.open("inventory.db", "w")
        invDict = db["inventory"]
        stock = invDict.get(id)
        brand = stock.get_name().split(" ", 1)[0]
        stock.set_name(brand, updateStockInfoForm.productName.data)
        stock.set_currentStock(updateStockInfoForm.currentStock.data)
        stock.set_soldStock(updateStockInfoForm.soldStock.data)
        stock.set_costPrice(updateStockInfoForm.costPrice.data)
        stock.set_sellingPrice(updateStockInfoForm.sellPrice.data)
        db["inventory"] = invDict
        db.close()
        return redirect(url_for("inventory"))
    else:
        invDict = {}
        db = shelve.open("inventory.db", "r")
        invDict = db["inventory"]
        db.close()
        stock = invDict.get(id)
        name = stock.get_name().split(" ", 1)[1]
        updateStockInfoForm.productName.data = name
        updateStockInfoForm.currentStock.data = stock.get_currentStock()
        updateStockInfoForm.soldStock.data = stock.get_soldStock()
        updateStockInfoForm.costPrice.data = stock.get_costPrice()
        updateStockInfoForm.sellPrice.data = stock.get_sellingPrice()
        return render_template("updateStockInfo.html", cookieDict=cookieDict, form=updateStockInfoForm)


@app.route("/deleteStock/<int:id>", methods=["POST"])
def deleteStock(id):
    invDict = {}
    db = shelve.open("inventory.db", "w")
    invDict = db["inventory"]
    invDict.pop(id)
    db["inventory"] = invDict
    db.close()
    return redirect(url_for("inventory"))


@app.route("/signup")
def signup():
    return render_template("signup.html", cookieDict=cookieDict)

if __name__ == '__main__':
    app.run()
