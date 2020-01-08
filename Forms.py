from wtforms import Form, StringField, SelectField, validators, FloatField, IntegerField, ValidationError, Field


class importForm(Form):

    def validate_float(form, field):
        if field.data <= 0:
            raise ValidationError("Price must be a valid value!")

    brand = SelectField("Brand Name", [validators.DataRequired()], choices=[("","Select"), ("pilot","Pilot"), ("uni-ball", "Uni-ball")])
    productName = StringField("Product Name", [validators.DataRequired(), validators.Length(min=1, max=70)])
    quantity = IntegerField("Quantity", [validators.DataRequired(), validators.NumberRange(min=1, max=200)])
    costPrice = FloatField("Cost Price", [validators.DataRequired(), validators.NumberRange(min=0.01)])
    sellPrice = FloatField("Selling Price", [validators.DataRequired(), validators.NumberRange(min=0.01)])


