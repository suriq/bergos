from django.db import models





class Company(models.Model):
    name = models.CharField(max_length=255)
    tax_id = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)


    def __str__(self):
        return self.name


    class Meta:
        verbose_name_plural = "Companies"





class Location(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE,related_name='locations')
    name = models.CharField(max_length=25)
    address = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} ({self.company})"


    class Meta:
        verbose_name_plural = "Locations"





class Person(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='persons')
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.location})"
    

    class Meta:
        verbose_name_plural = "People"