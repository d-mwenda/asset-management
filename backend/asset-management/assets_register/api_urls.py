from rest_framework import routers
from .views import AssetTypesViewSet, AssetMakesViewSet, AssetModelsViewSet, VendorsViewSet, OfficesViewSet, \
    AssetOwnersViewSet, AssetUsersDetailsViewSet, NonHumanUsersViewSet, AssetsViewSet, AssetIssuanceRegisterViewSet

router = routers.DefaultRouter()
router.register(r'asset-types', AssetTypesViewSet)
router.register(r'asset-makes', AssetMakesViewSet)
router.register(r'asset-models', AssetModelsViewSet)
router.register(r'vendors', VendorsViewSet)
router.register(r'offices', OfficesViewSet)
router.register(r'asset-owners', AssetOwnersViewSet)
router.register(r'asset-users-details', AssetUsersDetailsViewSet)
router.register(r'non-human-users', NonHumanUsersViewSet)
router.register(r'assets', AssetsViewSet)
router.register(r'asset-issuance-register', AssetIssuanceRegisterViewSet)
urlpatterns = router.urls
