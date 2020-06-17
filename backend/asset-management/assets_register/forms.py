from django import forms

from django.forms import Form, ModelForm, Textarea, TextInput, HiddenInput
from django.utils.timezone import now
# atbs imports
from .models import Assets, AssetTypes, AssetModels, AssetMakes, Vendors, AssetOwners, Offices, AssetIssuanceRegister, \
    AssetUsers


class AddAssetForm(ModelForm):

    class Meta:

        model = Assets
        fields = ('serial_number', 'asset_number', 'asset_type', 'asset_model', 'components', 'vendor',
                  'date_of_purchase', 'warranty_end_date', 'purchase_value', 'purchase_currency', 'expected_life',
                  'owner',)
        widgets = {
            'components': forms.Textarea(attrs={'rows': 5, 'style': 'resize:none'}),
        }


class AddAssetTypeForm(ModelForm):

    class Meta:

        model = AssetTypes
        fields = ('asset_type',)


class AddAssetMakeForm(ModelForm):

    class Meta:

        model = AssetMakes
        fields = ('asset_make',)


class AddAssetModelForm(ModelForm):

    class Meta:

        model = AssetModels
        fields = ('asset_type', 'asset_make', 'model_number')


class AddVendorForm(ModelForm):

    class Meta:

        model = Vendors
        fields = ('name', 'address', 'tel_no', 'nature',)


class AddAssetOwnerForm(ModelForm):

    class Meta:

        model = AssetOwners
        fields = ('owner_name', 'description', 'custodian',)


class AddOfficeLocationForm(ModelForm):

    class Meta:

        model = Offices
        fields = ('location',)


class AssetIssuanceForm(ModelForm):

    class Meta:

        model = AssetIssuanceRegister
        fields = ('asset', 'user', 'date_issued', 'comment_on_issue',)
        widgets = {
            'asset': forms.HiddenInput(),
            'comment_on_issue': forms.Textarea(attrs={'rows': 5, 'style': 'resize:none'}),
        }


class AssetWithdrawalForm(ModelForm):

    class Meta:

        model = AssetIssuanceRegister
        fields = ('asset', 'date_returned', 'comment_on_return',)
        widgets = {
            'asset': forms.HiddenInput(),
            'comment_on_return': forms.Textarea(attrs={'rows': 5, 'style': 'resize:none'}),
        }


class WithdrawAssetForm(ModelForm):

    class Meta:

        model = AssetIssuanceRegister
        fields = ('asset', 'date_returned', 'comment_on_return',)
        # widgets = {}


class AddAssetUserForm(ModelForm):

    class Meta:

        model = AssetUsers
        fields = ('name', 'program', 'office_location',)


class SearchForm(Form):

    asset = forms.CharField(max_length=30, widget=TextInput(attrs={'id': 'search_query', 'required': True}))


class AssetsExcelExportForm(Form):

        serial_number = forms.BooleanField(widget=forms.CheckboxInput, required=False)
        asset_number = forms.BooleanField(widget=forms.CheckboxInput, required=False)
        status = forms.BooleanField(widget=forms.CheckboxInput, required=False)
        asset_type = forms.BooleanField(widget=forms.CheckboxInput, required=False)
        asset_model = forms.BooleanField(widget=forms.CheckboxInput, required=False)
        vendor = forms.BooleanField(widget=forms.CheckboxInput, required=False)
        date_of_purchase = forms.BooleanField(widget=forms.CheckboxInput, required=False)
        purchase_value = forms.BooleanField(widget=forms.CheckboxInput, required=False)
        purchase_currency = forms.BooleanField(widget=forms.CheckboxInput, required=False)
        expected_life = forms.BooleanField(widget=forms.CheckboxInput, required=False)
        owner = forms.BooleanField(widget=forms.CheckboxInput, required=False)
        status_of_usage = forms.BooleanField(widget=forms.CheckboxInput, required=False)
