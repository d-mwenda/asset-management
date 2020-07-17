from django.urls import path
# Third party imports
from rest_framework import routers
# atbs urls
from .views import ListAssets, SearchAsset, AddAsset, IssueAsset, AssetsUsers, AssetsAdministration, AddAssetType, \
    AddAssetModel, AddAssetMake, AddAssetVendor, AddOfficeLocation, AddAssetOwner, AddAssetUser, UpdateAssetType, \
    ViewAssetTypes, ViewAssetMakes, ViewVendors, ViewAssetOwners, ViewAssetModels, ViewOfficeLocations, AssetProfile,\
    UpdateAssetMake, UpdateAssetModel, UpdateAssetOwner, UpdateAssetVendor, UpdateOfficeLocation, AssetWithdrawal, \
    AssetStore, UserAssignedAssets, AssetTypesViewSet, AssetMakesViewSet, AssetModelsViewSet, VendorsViewSet, \
    OfficesViewSet, AssetOwnersViewSet, AssetUsersDetailsViewSet, NonHumanUsersViewSet, AssetsViewSet, \
    AssetIssuanceRegisterViewSet

urlpatterns = [
    # Day-to-day asset management tasks
    path(r'list', ListAssets.as_view(), name='u_list_assets'),
    path(r'asset-store', AssetStore.as_view(), name='u_asset_store'),
    path(r'user-assigned-assets/user=<user_id>', UserAssignedAssets.as_view(), name='u_user_assigned_assets'),
    path(r'search', SearchAsset.as_view(), name='u_search_asset'),
    path(r'add-asset', AddAsset.as_view(), name='u_add_asset'),
    path(r'issue-asset/asset=<asset>', IssueAsset.as_view(), name='u_issue_asset'),
    path(r'withdraw-asset/asset=<asset>', AssetWithdrawal.as_view(), name='u_withdraw_asset'),
    # Todo consider adding a variable of the asset being issued in the above path
    path(r'asset-users', AssetsUsers.as_view(), name='u_asset_users'),
    path(r'asset-profile/asset=<asset_id>', AssetProfile.as_view(), name='u_asset_profile'),

    # list asset metadata
    path(r'asset-types', ViewAssetTypes.as_view(), name='u_view_asset_types'),
    path(r'asset-makes', ViewAssetMakes.as_view(), name='u_view_asset_makes'),
    path(r'asset-models', ViewAssetModels.as_view(), name='u_view_asset_models'),
    path(r'asset-owners', ViewAssetOwners.as_view(), name='u_view_asset_owners'),
    path(r'asset-vendors', ViewVendors.as_view(), name='u_view_asset_vendors'),
    path(r'offices', ViewOfficeLocations.as_view(), name='u_view_offices'),

    # This url will be redundant when all metadata add, view and update functionality have their own views
    path(r'assets-administration', AssetsAdministration.as_view(), name='u_assets_administration'),

    # add asset metadata
    path(r'add-asset-type', AddAssetType.as_view(), name='u_add_asset_type'),
    path(r'add-asset-model', AddAssetModel.as_view(), name='u_add_asset_model'),
    path(r'add-asset-make', AddAssetMake.as_view(), name='u_add_asset_make'),
    path(r'add-asset-vendor', AddAssetVendor.as_view(), name='u_add_asset_vendor'),
    path(r'add-office', AddOfficeLocation.as_view(), name='u_add_office'),
    path(r'add-asset-owner', AddAssetOwner.as_view(), name='u_add_asset_owner'),
    path(r'add-asset-user', AddAssetUser.as_view(), name='u_add_asset_user'),

    # Edit/update asset metadata
    path(r'edit-asset-type/asset-type=<asset_type>', UpdateAssetType.as_view(), name='u_edit_asset_type'),
    path(r'edit-asset-make/asset-make=<asset_make>', UpdateAssetMake.as_view(), name='u_edit_asset_make'),
    path(r'edit-asset-model/asset-model=<asset_model>', UpdateAssetModel.as_view(), name='u_edit_asset_model'),
    path(r'edit-asset-owner/asset-owner=<asset_owner>', UpdateAssetOwner.as_view(), name='u_edit_asset_owner'),
    path(r'edit-asset-vendor/asset-vendor=<asset_vendor>', UpdateAssetVendor.as_view(), name='u_edit_vendor'),
    path(r'edit-asset-office/office=<office>', UpdateOfficeLocation.as_view(), name='u_edit_office_location'),
]

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'asset-types/api/', AssetTypesViewSet)
router.register(r'asset-makes/api/', AssetMakesViewSet)
router.register(r'asset-models/api/', AssetModelsViewSet)
router.register(r'vendors/api/', VendorsViewSet)
router.register(r'offices/api/', OfficesViewSet)
router.register(r'asset-owners/api/', AssetOwnersViewSet)
router.register(r'asset-users-details/api/', AssetUsersDetailsViewSet)
router.register(r'non-human-users/api/', NonHumanUsersViewSet)
router.register(r'assets/api/', AssetsViewSet)
router.register(r'asset-issuance-register/api/', AssetIssuanceRegisterViewSet)
urlpatterns += router.urls
