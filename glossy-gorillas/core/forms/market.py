from django import forms
from django.utils.translation import gettext as _
from core.models import Listing


class ListInventoryRecord(forms.ModelForm):
    NO_BARTER_METHOD = "no_barter_method"
    NO_BARTER_PRODUCT_QTY = "no_barter_product_qty"

    class Meta:
        model = Listing
        fields = (
            "silver_price",
            "barter_product",
            "barter_product_quantity",
            "allow_offers",
        )

    def __init__(self, item_id: int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.item_id = item_id
        self.fields["silver_price"].required = False
        self.fields["barter_product"].required = False
        self.fields["barter_product_quantity"].required = False

    def save(self, *args, **kwargs):
        instance = super().save(commit=False, *args, **kwargs)
        instance.item_id = self.item_id
        instance.save()
        return instance

    def clean(self, *args, **kwargs):
        """Validate that at least one barter method is specified"""
        data = super().clean(*args, **kwargs)
        conditions = [
            data.get("silver_price") is not None,
            data.get("barter_product") is not None,
            data.get("allow_offers") is True,
        ]
        if any(conditions):
            return data
        else:
            raise forms.ValidationError(
                message=_("Specify at least one barter method"),
                code=ListInventoryRecord.NO_BARTER_METHOD,
            )

    def clean_barter_product_quantity(self):
        if self.cleaned_data.get("barter_product") and not self.cleaned_data.get(
            "barter_product_quantity"
        ):
            raise forms.ValidationError(
                message=_("Specify a quantity of products you want"),
                code=ListInventoryRecord.NO_BARTER_PRODUCT_QTY,
            )
