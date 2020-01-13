from wtforms import Form, StringField, SelectField, validators, FloatField, IntegerField, ValidationError


class importForm(Form):
    brand = SelectField("Brand Name", [validators.DataRequired()], choices=[("","Select"), ("pilot","Pilot"), ("uni-ball", "Uni-ball")], default="")
    productName = StringField("Product Name", [validators.DataRequired(), validators.Length(max=70)])
    quantity = IntegerField("Quantity", [validators.DataRequired(), validators.NumberRange(max=1000)])
    costPrice = FloatField("Cost Price", [validators.DataRequired(), validators.NumberRange(min=0.01)])
    sellPrice = FloatField("Selling Price", [validators.DataRequired(), validators.NumberRange(min=0.01)])


class updateForm(Form):
    productName = StringField("Product Name", [validators.DataRequired(), validators.Length(min=1, max=70)])
    currentStock = IntegerField("Current Stock", [validators.InputRequired()])
    costPrice = FloatField("Cost Price", [validators.DataRequired(), validators.NumberRange(min=0.01)])
    sellPrice = FloatField("Selling Price", [validators.DataRequired(), validators.NumberRange(min=0.01)])
