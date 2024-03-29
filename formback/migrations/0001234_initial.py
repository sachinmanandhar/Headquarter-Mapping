# Generated by Django 2.2.10 on 2020-08-06 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WardForm',
            fields=[
                ('Object_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('munid', models.CharField(blank=True, max_length=100, null=True)),
                ('province', models.CharField(blank=True, max_length=100, null=True)),
                ('ward_no', models.CharField(blank=True, max_length=100, null=True)),
                ('DISTRICT', models.CharField(blank=True, max_length=100, null=True)),
                ('palika_name', models.CharField(blank=True, max_length=100, null=True)),
                ('palika_type', models.CharField(blank=True, max_length=100, null=True)),
                ('Area', models.CharField(blank=True, max_length=100, null=True)),
                ('Ward_Office_Address', models.CharField(blank=True, max_length=100, null=True)),
                ('Ward_Contact_No', models.CharField(blank=True, max_length=100, null=True)),
                ('Chairperson_Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Chaiperson_Contact_No', models.CharField(blank=True, max_length=100, null=True)),
                ('Secretary_Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Secretary_Contact_No', models.CharField(blank=True, max_length=100, null=True)),
                ('Total_Households', models.CharField(blank=True, max_length=100, null=True)),
                ('Total_Population', models.CharField(blank=True, max_length=100, null=True)),
                ('Total_Male_Population', models.CharField(blank=True, max_length=100, null=True)),
                ('Total_Female_Population', models.CharField(blank=True, max_length=100, null=True)),
                ('Website', models.CharField(blank=True, max_length=100, null=True)),
                ('Email', models.CharField(blank=True, max_length=100, null=True)),
                ('X_Cords', models.CharField(blank=True, max_length=100, null=True)),
                ('Y_Cords', models.CharField(blank=True, max_length=100, null=True)),
                ('Verification', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='WardFormTemp',
            fields=[
                ('Object_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('munid', models.CharField(blank=True, max_length=100, null=True)),
                ('province', models.CharField(blank=True, max_length=100, null=True)),
                ('ward_no', models.CharField(blank=True, max_length=100, null=True)),
                ('DISTRICT', models.CharField(blank=True, max_length=100, null=True)),
                ('palika_name', models.CharField(blank=True, max_length=100, null=True)),
                ('palika_type', models.CharField(blank=True, max_length=100, null=True)),
                ('Area', models.CharField(blank=True, max_length=100, null=True)),
                ('Ward_Office_Address', models.CharField(blank=True, max_length=100, null=True)),
                ('Ward_Contact_No', models.CharField(blank=True, max_length=100, null=True)),
                ('Chairperson_Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Chaiperson_Contact_No', models.CharField(blank=True, max_length=100, null=True)),
                ('Secretary_Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Secretary_Contact_No', models.CharField(blank=True, max_length=100, null=True)),
                ('Total_Households', models.CharField(blank=True, max_length=100, null=True)),
                ('Total_Population', models.CharField(blank=True, max_length=100, null=True)),
                ('Total_Male_Population', models.CharField(blank=True, max_length=100, null=True)),
                ('Total_Female_Population', models.CharField(blank=True, max_length=100, null=True)),
                ('Website', models.CharField(blank=True, max_length=100, null=True)),
                ('Email', models.CharField(blank=True, max_length=100, null=True)),
                ('X_Cords', models.CharField(blank=True, max_length=100, null=True)),
                ('Y_Cords', models.CharField(blank=True, max_length=100, null=True)),
                ('Verification', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
