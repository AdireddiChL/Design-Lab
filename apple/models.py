from django.db import models


# Create your models here.

class plus_sign(models.Model):
    image_id = models.IntegerField(default=-1)
    image_name = models.CharField(max_length=256)
    image_file = models.ImageField()

    def __str__(self):
        return str(self.image_id) + " - " + str(self.image_name)


class minus_sign(models.Model):
    image_id = models.IntegerField(default=-1)
    image_name = models.CharField(max_length=256)
    image_file = models.ImageField()

    def __str__(self):
        return str(self.image_id) + " - " + str(self.image_name)


class times_sign(models.Model):
    image_id = models.IntegerField(default=-1)
    image_name = models.CharField(max_length=256)
    image_file = models.ImageField()

    def __str__(self):
        return str(self.image_id) + " - " + str(self.image_name)


class division_sign(models.Model):
    image_id = models.IntegerField(default=-1)
    image_name = models.CharField(max_length=256)
    image_file = models.ImageField()

    def __str__(self):
        return str(self.image_id) + " - " + str(self.image_name)


class zero_number(models.Model):
    image_id = models.IntegerField(default=-1)
    image_name = models.CharField(max_length=256)
    image_file = models.ImageField()

    def __str__(self):
        return str(self.image_id) + " - " + str(self.image_name)


class one_number(models.Model):
    image_id = models.IntegerField(default=-1)
    image_name = models.CharField(max_length=256)
    image_file = models.ImageField()

    def __str__(self):
        return str(self.image_id) + " - " + str(self.image_name)


class two_number(models.Model):
    image_id = models.IntegerField(default=-1)
    image_name = models.CharField(max_length=256)
    image_file = models.ImageField()

    def __str__(self):
        return str(self.image_id) + " - " + str(self.image_name)


class three_number(models.Model):
    image_id = models.IntegerField(default=-1)
    image_name = models.CharField(max_length=256)
    image_file = models.ImageField()

    def __str__(self):
        return str(self.image_id) + " - " + str(self.image_name)


class four_number(models.Model):
    image_id = models.IntegerField(default=-1)
    image_name = models.CharField(max_length=256)
    image_file = models.ImageField()

    def __str__(self):
        return str(self.image_id) + " - " + str(self.image_name)


class five_number(models.Model):
    image_id = models.IntegerField(default=-1)
    image_name = models.CharField(max_length=256)
    image_file = models.ImageField()

    def __str__(self):
        return str(self.image_id) + " - " + str(self.image_name)


class six_number(models.Model):
    image_id = models.IntegerField(default=-1)
    image_name = models.CharField(max_length=256)
    image_file = models.ImageField()

    def __str__(self):
        return str(self.image_id) + " - " + str(self.image_name)


class seven_number(models.Model):
    image_id = models.IntegerField(default=-1)
    image_name = models.CharField(max_length=256)
    image_file = models.ImageField()

    def __str__(self):
        return str(self.image_id) + " - " + str(self.image_name)


class eight_number(models.Model):
    image_id = models.IntegerField(default=-1)
    image_name = models.CharField(max_length=256)
    image_file = models.ImageField()

    def __str__(self):
        return str(self.image_id) + " - " + str(self.image_name)


class nine_number(models.Model):
    image_id = models.IntegerField(default=-1)
    image_name = models.CharField(max_length=256)
    image_file = models.ImageField()

    def __str__(self):
        return str(self.image_id) + " - " + str(self.image_name)


class meta_data_table(models.Model):
    char_name = models.CharField(max_length=10)
    number_of_fields = models.IntegerField(default=0)

    def __str__(self):
        return str(self.char_name) + " : " + str(self.number_of_fields)
