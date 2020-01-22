from django.db import models
from django.contrib.auth.models import User


class Organization(models.Model):

    name = models.CharField(max_length=50)
    street_address = models.CharField(max_length=50, default=None)
    city = models.CharField(max_length=50, default=None)
    state = models.CharField(max_length=50, default=None)
    zip_code = models.IntegerField(default=None)
    contact_name = models.CharField(max_length=50, default=None)
    area_code = models.SmallIntegerField(default=None)
    prefix = models.SmallIntegerField(default=None)
    line_number = models.SmallIntegerField(default=None)

    def __str__(self):
        return self.name

    def address(self):
        """ Returns the complete address formatted in a string. """
        return f"{self.street_address} {self.city}, {self.state} {self.real_zip_code()}"

    def phone_number(self):
        """ Returns the complete phone number formatted in a string. """
        return f"{self.area_code}-{self.prefix}-{self.line_number}"

    def real_zip_code(self):
        """ Makes sure return zip code is 5 digits by adding a leading zero. """

        if len(str(self.zip_code)) == 4:
            return f"0{self.zip_code}"
        else:
            return self.zip_code



class Site(models.Model):

    name = models.CharField(max_length=50)
    street_address = models.CharField(max_length=50, default=None)
    city = models.CharField(max_length=50, default=None)
    state = models.CharField(max_length=50, default=None)
    zip_code = models.IntegerField(default=None)
    contact_name = models.CharField(max_length=50, default=None)
    area_code = models.SmallIntegerField(default=None)
    prefix = models.SmallIntegerField(default=None)
    line_number = models.SmallIntegerField(default=None)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.name

    def address(self):
        """ Returns the complete address formatted in a string. """
        return f"{self.street_address} {self.city}, {self.state} {self.real_zip_code()}"

    def phone_number(self):
        """ Returns the complete phone number formatted in a string. """
        return f"{self.area_code}-{self.prefix}-{self.line_number}"

    def real_zip_code(self):
        """ Makes sure return zip code is 5 digits by adding a leading zero. """

        if len(str(self.zip_code)) == 4:
            return f"0{self.zip_code}"
        else:
            return self.zip_code


class Note(models.Model):

    date = models.DateField()
    body = models.TextField(max_length=200)
    site = models.ForeignKey(Site, on_delete=models.CASCADE, default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.site.name
