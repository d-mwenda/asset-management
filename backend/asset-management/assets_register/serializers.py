from .models import AssetTypes, AssetMakes, AssetModels, Vendors, Offices, AssetOwners, AssetUsersDetails, Assets,\
    NonHumanUsers, AssetIssuanceRegister
from rest_framework import serializers


class AssetTypesSerializer(serializers.ModelSerializer):
    """
    This serializer class serializes the AssetTypes model of the assets-register app.
    """
    class Meta:
        model = AssetTypes
        fields = ['asset_type', 'type_description']


class AssetMakesSerializer(serializers.ModelSerializer):
    """
    This serializer class serializes the AssetMakes model of the assets-register app
    """
    class Meta:
        model = AssetMakes
        fields = ['asset_make']


class AssetModelsSerializer(serializers.ModelSerializer):
    """
    This serializer class serializes the AssetModels model of the assets-register app
    """
    asset_make_name = serializers.CharField(source='asset_make.asset_make', read_only=True)
    asset_type_name = serializers.CharField(source='asset_type.asset_type', read_only=True)

    class Meta:
        model = AssetModels
        fields = ['asset_make', 'asset_make_name', 'asset_type','asset_type_name', 'model_number', 'model_description']
        # depth = 2


class VendorsSerializer(serializers.ModelSerializer):
    """
    This serializer class serializes the Vendors Model of the assets-register app
    """
    class Meta:
        model = Vendors
        fields = ['name', 'address', 'tel_no', 'nature']


class OfficesSerializer(serializers.ModelSerializer):
    """
    This serializer class serializes the Offices Model of the assets-register app
    """
    class Meta:
        model = Offices
        fields = ['id', 'location']


class AssetOwnersSerializer(serializers.ModelSerializer):
    """
    This serializer class serializes the AssetOwners Model of the assets-register app
    """
    custodian_first_name = serializers.CharField(source='custodian.first_name', read_only=True)
    custodian_last_name = serializers.CharField(source='custodian.last_name', read_only=True)

    class Meta:
        model = AssetOwners
        fields = ['id', 'owner_name', 'description', 'custodian', 'custodian_first_name', 'custodian_last_name']


class AssetUsersDetailsSerializer(serializers.ModelSerializer):
    """
    This serializer class serializes the AssetUsersDetails Model of the assets-register app
    """
    class Meta:
        model = AssetUsersDetails
        fields = ['user', 'department', 'office_location', 'is_still_staff']


class NonHumanUsersSerializer(serializers.ModelSerializer):
    """
    This serializer class serializes the NonHumanUsers Model of the assets-register app
    """
    class Meta:
        model = NonHumanUsers
        fields = ['name', 'office']


class AssetsSerializer(serializers.ModelSerializer):
    """
    This serializer class serializes the Assets Model of the assets-register app
    """
    class Meta:
        model = Assets
        fields = ['serial_number', 'asset_number', 'status', 'asset_type', 'asset_model', 'components', 'vendor',
                  'date_of_purchase', 'warranty_end_date', 'purchase_value', 'purchase_currency', 'expected_life',
                  'owner', 'status_of_usage']


class AssetIssuanceRegisterSerializer(serializers.ModelSerializer):
    """
    This serializer class serializes the AssetsIssuanceRegister Model of the assets-register app
    """
    class Meta:
        model = AssetIssuanceRegister
        fields = ['asset', 'user', 'date_issued', 'comment_on_issue', 'returned', 'date_returned', 'comment_on_return']
