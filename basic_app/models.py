from django.db import models


# Create your models here.
class Viloyat(models.Model):
    viloyat = models.CharField(max_length=250)

    def __str__(self):
        return self.viloyat


class Tuman(models.Model):
    viloyat = models.ForeignKey(Viloyat, on_delete=models.CASCADE)
    tuman = models.CharField(max_length=250)

    def __str__(self):
        return self.tuman


class Stansiya(models.Model):
    tuman = models.ForeignKey(Tuman, on_delete=models.CASCADE)
    stansiya_nomi = models.CharField(max_length=250)

    def __str__(self):
        return self.stansiya_nomi


class Osimlik(models.Model):
    stansiya = models.ForeignKey(Stansiya, on_delete=models.CASCADE)
    osimlik_nomi = models.CharField(max_length=250)

    def __str__(self):
        return self.osimlik_nomi


class Hashorot(models.Model):
    osimlik_nomi = models.ForeignKey(Osimlik, on_delete=models.CASCADE)
    hashorot_nomi = models.CharField(max_length=250)
    about = models.TextField()

    def __str__(self):
        return self.hashorot_nomi


class DataHashorot(models.Model):
    viloyat = models.ForeignKey(Viloyat, on_delete=models.CASCADE)
    tuman = models.ForeignKey(Tuman, on_delete=models.CASCADE)
    stansiya = models.ForeignKey(Stansiya, on_delete=models.CASCADE)
    osimlik_nomi = models.ForeignKey(Osimlik, on_delete=models.CASCADE)
    hashorot = models.ForeignKey(Hashorot, on_delete=models.CASCADE, null=True)
    vaqt = models.CharField(max_length=250, null=True)
    statistica = models.CharField(max_length=250, null=True)
    vlajnost = models.CharField(max_length=250, null=True)

    def __str__(self):
        return f"{self.viloyat} {self.tuman} {self.stansiya} {self.osimlik_nomi} {self.hashorot} {self.stansiya}"


class data(models.Model):
    summa = models.CharField(max_length=250)
    eggs = models.CharField(max_length=250)
    lichinka = models.CharField(max_length=250)
    dlyazrelix = models.CharField(max_length=250)
    letat = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.summa
