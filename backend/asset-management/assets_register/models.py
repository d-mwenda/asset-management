from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# these currency values are imported in other apps
# consider importing them from the toolbox
currency = (
        ('KES', 'Kenya Shillings'),
        ('USD', 'US Dollars'),
        ('GBP', 'Great Britain Pounds'),
    )


class AssetTypes(models.Model):
    """
    This model stores all the possible types/classes of assets.
    """
    asset_type = models.CharField(max_length=30, null=False, blank=False, db_index=True, unique=True)
    type_description = models.CharField(max_length=1000, null=True, blank=True, verbose_name="asset type description")

    def __str__(self):
        return self.asset_type


class AssetMakes(models.Model):
    """
    This class stores all asset makes.
    """
    asset_make = models.CharField(max_length=30, null=False, blank=False, db_index=True)

    def __str__(self):
        return self.asset_make


class AssetModels(models.Model):
    """
    This class stores asset models. A model must have a corresponding make.
    """
    asset_type = models.ForeignKey(AssetTypes, on_delete=models.CASCADE, blank=False, null=False)
    asset_make = models.ForeignKey(AssetMakes, on_delete=models.CASCADE, blank=False, null=False)
    model_number = models.CharField(max_length=20, null=False,blank=False, db_index=True)
    model_description = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.model_number


class Vendors(models.Model):
    """
    This model takes care of all possible sources of assets an organization can have.
    """
    vendor_nature = (
        ('local', 'Local'),
        ('international', 'International'),
        ('donor', 'Donor'),
    )

    name = models.CharField(max_length=30, null=False, blank=False)
    address = models.CharField(max_length=50)
    tel_no = models.CharField(max_length=15)
    nature = models.CharField(max_length=3, choices=vendor_nature, null=False, default='loc')

    def __str__(self):
        return self.name

    def nature_verbose(self):
        return dict(Vendors.vendor_nature)[self.nature]


class Offices(models.Model):
    """
    All offices that an organization has or where its users reside and use assets from.
    """
    location = models.CharField(max_length=20, db_index=True, null=False, blank=True)

    def __str__(self):
        return self.location


class AssetOwners(models.Model):
    """
    Department, organizational unit or project that owns assets
    """
    owner_name = models.CharField(max_length=30, null=False, blank=False,
                                  verbose_name="Which department owns the asset")
    description = models.CharField(max_length=300, null=True)
    custodian = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.owner_name

class AssetUsersDetails(models.Model):
    """
    This model maintains the more details of users beyond those django's users' model supports by default.
     These are all human users, and non-human users such as conference rooms, vehicles, offices, etc are maintained
     in the NonHumanUsers model
    """

    user = models.OneToOneField(User, db_index=True, on_delete=models.CASCADE)
    department = models.ForeignKey(AssetOwners, on_delete=models.CASCADE, null=False, blank=False)
    office_location = models.ForeignKey(Offices, on_delete=models.CASCADE)
    is_still_staff = models.BooleanField(verbose_name="Still in the organization?",
                                         default=True, null=False)

    def __str__(self):
        return self.name


class NonHumanUsers(models.Model):
    """
    This model maintains those users of an asset that are non-human e.g. a conference room that can be assigned a
    projector, table and chairs.
    """
    name = models.CharField(max_length=100, null=False, blank=False)
    office = models.ForeignKey(Offices, on_delete=models.PROTECT)

    def __str__(self):
        return '-'.join(self.name, self.office.location)


class Assets(models.Model):
    """
    This model stores and manipulates actions on the asset instances. These actions are the various transactions and
    changes of state of an asset.
    """
    # todo: add a usage_type for ease of management between single-user and shared-resource usage types assets
    asset_status = (
        ('functional', 'Functional'),
        ('faulty', 'Faulty'),
        ('disposed', 'Disposed'),
        ('to be disposed', 'Earmarked for Disposal'),
    )

    usage_status = (
        ('issued', 'In Use'),
        ('in store', 'In Store'),
        ('disposed', 'Disposed'),
    )

    serial_number = models.CharField(max_length=30, null=True, blank=True, unique=True, db_index=True)
    asset_number = models.CharField(max_length=30, null=False, blank=False, unique=True, db_index=True)
    status = models.CharField(max_length=30, choices=asset_status, null=False, blank=True, default='fnc')
    asset_type = models.ForeignKey(AssetTypes, on_delete=models.CASCADE, null=False, blank=False)
    asset_model = models.ForeignKey(AssetModels, on_delete=models.CASCADE, null=False, blank=False)
    components = models.CharField(max_length=500, null=True, blank=True)
    vendor = models.ForeignKey(Vendors, on_delete=models.CASCADE, null=False, blank=False)
    date_of_purchase = models.DateField(null=False, default=now)
    warranty_end_date = models.DateField(null=True, blank=True)
    purchase_value = models.FloatField(null=False, default=0.00)
    purchase_currency = models.CharField(max_length=5, null=False, blank=True, default='KES', choices=currency)
    expected_life = models.DecimalField(decimal_places=2, max_digits=4, null=False, default=5)
    owner = models.ForeignKey(AssetOwners, on_delete=models.CASCADE, null=False, blank=False)
    status_of_usage = models.CharField(max_length=10, choices=usage_status, null=False, default='uis', db_index=True)

    '''def __int__(self):
        return self.id'''

    def __str__(self):
        return self.asset_number


class AssetIssuanceRegister(models.Model):
    """
    This model keeps a log of how assets are issued and returned to users.
    """
    # Todo. Modify the save method to send an email to the user once an asset is issued to them or when they return
    # Todo. Modify the save method to check that either the user or non-human user being assigned is selected. otherwise
    # return an error

    asset = models.ForeignKey(Assets, on_delete=models.CASCADE, null=False, db_index=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, db_index=True)
    date_issued = models.DateField(null=False, blank=True, default=now())
    comment_on_issue = models.CharField(max_length=500, null=True, blank=True)
    returned = models.BooleanField(null=False, blank=True, default=False)
    date_returned = models.DateField(null=True)
    comment_on_return = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.asset
