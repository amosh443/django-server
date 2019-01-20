from django.db import models


class User(models.Model):
    name = models.CharField(
        max_length=222,
        null=False,
        blank=False,
    )

    surname = models.CharField(
        max_length=222,
        null=False,
        blank=False,
    )

    phone = models.CharField(
        max_length=222,
        null=False,
        blank=False,
    )

    password = models.CharField(
        max_length=222,
        null=False,
        blank=False,
    )

    card = models.CharField(
        max_length=222,
        null=True,
        blank=True,
    )


class Cafe(models.Model):
    name = models.CharField(
        max_length=222,
        null=False,
        blank=False,
    )

    description = models.CharField(
        max_length=222,
        null=False,
        blank=False,
    )

    password = models.CharField(
        max_length=222,
        null=False,
        blank=False,
    )

    photoURL = models.CharField(
        max_length=222,
        null=True,
        blank=False,
    )

    phone = models.CharField(
        max_length=22,
        null=True,
        blank=False,
    )

    coordX = models.DecimalField(
        null=False,
        decimal_places=10,
        max_digits=10,
    )

    coordY = models.DecimalField(
        null=False,
        decimal_places=10,
        max_digits=10,
    )


class Order(models.Model):
    user_id = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING(),
        null=False,
    )

    cafe_id = models.ForeignKey(
        Cafe,
        on_delete=models.DO_NOTHING(),
        null=False,
    )

    time = models.DateTimeField(
        null=False,
    )

    giving = models.BooleanField(
        null=False,
        default=True,
    )

    comment = models.CharField(
        max_length=222,
        null=True,
        blank=False,
    )

    count = models.IntegerField(
        null=True,
    )


class Dish(models.Model):
    name = models.CharField(
        max_length=222,
        null=True,
        blank=False,
    )

    photo_url = models.CharField(
        max_length=22,
        null=True,
        blank=False,
    )

    description = models.CharField(
        max_length=22,
        null=True,
        blank=False,
    )
