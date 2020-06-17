from django.db import models
from django.utils.timezone import now

# these currency values are imported in other apps
# consider importing them from the toolbox
currency = (
        ('KES', 'Kenya Shillings'),
        ('USD', 'US Dollars'),
        ('GBP', 'Great Britain Pounds'),
    )


class AssetTypes(models.Model):

    asset_type = models.CharField(max_length=30, null=False, blank=False, db_index=True, unique=True)

    def __str__(self):
        return self.asset_type


class AssetMakes(models.Model):

    asset_make = models.CharField(max_length=30, null=False, blank=False, db_index=True)

    def __str__(self):
        return self.asset_make


class AssetModels(models.Model):

    asset_type = models.ForeignKey(AssetTypes, on_delete=models.CASCADE, blank=False, null=False)
    asset_make = models.ForeignKey(AssetMakes, on_delete=models.CASCADE, blank=False, null=False)
    model_number = models.CharField(max_length=20, null=False,blank=False, db_index=True)

    def __str__(self):
        return self.model_number


class Vendors(models.Model):

    vendor_nature = (
        ('loc', 'Local'),
        ('int', 'International'),
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

    location = models.CharField(max_length=20, db_index=True, null=False, blank=True)

    def __str__(self):
        return self.location


class AssetOwners(models.Model):

    owner_name = models.CharField(max_length=30, null=False, blank=False)
    description = models.CharField(max_length=300, null=True)
    custodian = models.ForeignKey('AssetUsers', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.owner_name


class AssetUsers(models.Model):
    # Todo add an email field to support sending of emails to users issued out with assets and when they return

    name = models.CharField(max_length=40, null=False, blank=False, db_index=True)
    program = models.ForeignKey(AssetOwners, on_delete=models.CASCADE, null=False, blank=False)
    office_location = models.ForeignKey(Offices, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Assets(models.Model):
    # todo: add a usage_type for ease of management between single-user and shared-resource usage types assets
    asset_status = (
        ('fnc', 'Functional'),
        ('fty', 'Faulty'),
        ('dps', 'Disposed'),
        ('emk', 'Earmarked for Disposal'),
    )

    usage_status = (
        ('iss', 'In Use'),
        ('uis', 'In Store'),
        ('dsp', 'Disposed'),
    )

    serial_number = models.CharField(max_length=30, null=True, blank=True, unique=True, db_index=True)
    asset_number = models.CharField(max_length=30, null=False, blank=False, unique=True, db_index=True)
    status = models.CharField(max_length=3, choices=asset_status, null=False, blank=True, default='fnc')
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
    status_of_usage = models.CharField(max_length=3, choices=usage_status, null=False, default='uis', db_index=True)

    '''def __int__(self):
        return self.id'''

    def __str__(self):
        return self.asset_number


class AssetIssuanceRegister(models.Model):

    asset = models.ForeignKey(Assets, on_delete=models.CASCADE, null=False, db_index=True)
    user = models.ForeignKey(AssetUsers, on_delete=models.CASCADE, null=False, db_index=True)
    date_issued = models.DateField(null=False, blank=True, default=now)
    comment_on_issue = models.CharField(max_length=500, null=True, blank=True)
    returned = models.BooleanField(null=False, blank=True, default=False)
    date_returned = models.DateField(null=True)
    comment_on_return = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.asset
