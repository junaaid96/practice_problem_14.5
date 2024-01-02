from django.db import models
from first_app.models import MyModel
# Create your models here.


class anotherModel(models.Model):
    auto_field = models.AutoField(primary_key=True)
    # big_auto_field = models.BigAutoField(primary_key=True)
    big_integer_field = models.BigIntegerField()
    binary_field = models.BinaryField()
    boolean_field = models.BooleanField()
    char_field = models.CharField(max_length=255)
    # comma_separated_integer_field = models.CommaSeparatedIntegerField(
    #     max_length=255)
    # comma_seprated_field= models.CharField(validators=[comma_separated_validator], max_length=255)
    date_field = models.DateField()
    date_time_field = models.DateTimeField()
    decimal_field = models.DecimalField(max_digits=10, decimal_places=2)
    duration_field = models.DurationField()
    email_field = models.EmailField()
    file_field = models.FileField(upload_to='files/')
    # file_path_field = models.FilePathField()
    float_field = models.FloatField()
    foreign_key_field = models.ForeignKey(
        MyModel, on_delete=models.CASCADE)
    generic_ip_address_field = models.GenericIPAddressField()
    image_field = models.ImageField(upload_to='images/')
    integer_field = models.IntegerField()
    json_field = models.JSONField()
    # many_to_many_field = models.ManyToManyField(MyModel)
    # null_boolean_field = models.NullBooleanField()
    boolean_field2 = models.BooleanField(null=True)
    # on_to_one_field = models.OneToOneField(
    #     MyModel, on_delete=models.CASCADE)
    positive_big_integer_field = models.PositiveBigIntegerField()
    positive_integer_field = models.PositiveIntegerField()
    positive_small_integer_field = models.PositiveSmallIntegerField()
    slug_field = models.SlugField()
    small_integer_field = models.SmallIntegerField()
    text_field = models.TextField()
    time_field = models.TimeField()
    url_field = models.URLField()
    uuid_field = models.UUIDField()

    def __str__(self):
        return self.char_field
