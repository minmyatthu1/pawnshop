# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class customer(models.Model):
    customer_id = models.AutoField(db_column='customer_id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    point = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    comment = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'customer'


class inventory(models.Model):
    inventory_id = models.AutoField(db_column='inventory_id', primary_key=True)  # Field name made lowercase.
    item_name = models.CharField(max_length=100, blank=True, null=True)
    item_type = models.CharField(max_length=50, blank=True, null=True)
    operation = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'inventory'


class pawn(models.Model):
    pawn_id = models.AutoField(db_column='pawn_id',primary_key=True)  # Field name made lowercase.
    customer_id = models.ForeignKey(customer, models.DO_NOTHING, db_column='customer_id')  # Field name made lowercase.
    inventory_id = models.ForeignKey(inventory, models.DO_NOTHING, db_column='inventory_id')  # Field name made lowercase.
    invoice_number = models.IntegerField(blank=True, null=True)
    pawn_amt = models.IntegerField(blank=True, null=True)
    pawn_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'pawn'
      #  unique_together = ['customer_id', 'inventory_id']


class receive(models.Model):
    receive_id = models.AutoField(db_column='receive_id',primary_key=True)  # Field name made lowercase.
    inventory_id = models.ForeignKey(inventory, models.DO_NOTHING, db_column='inventory_id')  # Field name made lowercase.
    receive_date = models.DateTimeField()
    month_different = models.IntegerField()
    interest = models.IntegerField()
    receive_total_amt = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'receive'
       # unique_together = ['receive_id', 'inventory_id']
