from django.db import models


# Create your models here.

class Street(models.Model):
    StreetName = models.CharField(max_length=50)

    def __str__(self):
        return self.StreetName


class Abonent(models.Model):
    FIO = models.CharField(max_length=20)
    Phone = models.CharField(max_length=15)
    FlatNumber = models.IntegerField()
    CountPerson = models.IntegerField()
    HouseNo = models.SmallIntegerField()
    SizeFlat = models.FloatField()
    StreetCD = models.ForeignKey(Street, on_delete=models.CASCADE)


class Disrepair(models.Model):
    FailureName = models.CharField(max_length=50)


class Executor(models.Model):
    FIO = models.CharField(max_length=20)


class Request(models.Model):
    IncomingDate = models.DateTimeField
    ExecutorDate = models.DateTimeField
    Executed = models.BooleanField
    AccountCD = models.ForeignKey(Abonent, on_delete=models.CASCADE)
    FailureCD = models.ForeignKey(Disrepair, on_delete=models.CASCADE)
    ExecutorCD = models.ForeignKey(Executor, on_delete=models.CASCADE)


class Services(models.Model):
    ServiceName = models.CharField(max_length=20)


class Mode(models.Model):
    ModeName = models.CharField(max_length=120)
    Norma = models.FloatField()
    ServiceCD = models.ForeignKey(Services, on_delete=models.CASCADE)


class AbonMode(models.Model):
    Counter = models.BooleanField()
    AccountCD = models.ForeignKey(Abonent, on_delete=models.CASCADE)
    ModeCD = models.ForeignKey(Mode, on_delete=models.CASCADE)


class Pricing(models.Model):
    Price = models.FloatField()
    ModeCD = models.ForeignKey(Mode, on_delete=models.CASCADE)


class RecepPoint(models.Model):
    RecepName = models.CharField(max_length=30)


class NachislSum(models.Model):
    NachislMonth = models.SmallIntegerField()
    NachislYear = models.SmallIntegerField()
    NachislDate = models.DateField()
    CountMD = models.FloatField()
    Nachislsum = models.FloatField()
    AbonentMode = models.ForeignKey(AbonMode, on_delete=models.CASCADE)
    AccountCD = models.ForeignKey(Abonent, on_delete=models.CASCADE)


class PaySum(models.Model):
    CountMD = models.FloatField()
    PayDate = models.DateField()
    PayMonth = models.SmallIntegerField()
    PayYear = models.SmallIntegerField()
    ReceptionPoint = models.ForeignKey(RecepPoint, on_delete=models.CASCADE)
    PaySum = models.FloatField()
    AbonentMode = models.ForeignKey(AbonMode, on_delete=models.CASCADE)
    AccountCD = models.ForeignKey(Abonent, on_delete=models.CASCADE)
