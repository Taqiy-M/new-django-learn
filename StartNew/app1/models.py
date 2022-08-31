from django.db import models

# Create your models here.
# class Student1(models.Model):
#     #max_length required
#     ism = models.CharField(max_length=50)
#     #istalgancha yozish mumkin Textfieldda
#
#     #sonlar uchun
#     #models.IntegerField
#     #models.SmallIntegerField
#     #models.PositiveIntegerField
#     #models.AutoField
#
#     #bu son 32ming gacha berilishi mumkin
#     st_raqam = models.PositiveIntegerField()
#
#     # models.NullBooleanField
#     # models.BooleanField
#     bitiruvchi = models.BooleanField()
#     email = models.EmailField()
#     rasm = models.FileField()
#     def __str__(self):
#         return f"{self.ism}"
#
#
# class Teacher(models.Model):
#     JINS = (
#         ["Erkak", "Erkak"],
#         ["Ayol", "Ayol"]
#     )
#     #blank, null, default, unique parametrlari bor
#     #choice parametri bor. U tuple ichida tuple yoki tuple ichida list bo'lishi mumkin
#
#     ism = models.CharField(max_length=40, blank=True)
#     yosh = models.PositiveIntegerField(null=True)
#     jins = models.CharField(max_length=20,choices=JINS)
#     #datetimefield ham bor
#     #hozirgi vaqtni yozib qo'yadi. Bunda admin panelda ham chiqmaydi, avtomatik ishlaydi
#
#     birth_date = models.DateField(auto_now_add=True)
#     #musiqa vahokazo davomiylik uchun
#     ish_duration = models.DurationField()
#     def __str__(self):
#         return self.ism
#
# class Subject(models.Model):
#     nom = models.CharField(max_length=30)
#     asosiy = models.BooleanField()
#     yonalish = models.CharField(max_length=30)
#     #CASCADE: Teacher o'chib ketsa bu ham o'chib ketadi
#     # ustoz = models.ForeignKey(Teacher, on_delete=models.CASCADE)
#     ustoz = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
#     #assistant = models.OneToOneField(Teacher, on_delete=models.CASCADE)
#     talaba = models.ManyToManyField(Student1)
#     def __str__(self):
#         return self.nom

    #Meta class ni ham ko'rib chiq


class Student(models.Model):
    ism = models.CharField(max_length=30)
    st_raqam = models.IntegerField()
    bitiruvchi = models.BooleanField(default=True)
    kitoblar_soni = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.ism

class Yozuvchi(models.Model):
    MILLAT = (
        ["O'zbek", "O'zbek"],
        ["Turk", "Turk"],
        ["Ingliz", "Ingliz"],
        ["Arab", "Arab"],
        ["Hind", "Hind"]
    )
    ism = models.CharField(max_length=30)
    tirik = models.BooleanField()
    birth_year = models.PositiveIntegerField(default=0)
    millat = models.CharField(max_length=15, choices=MILLAT)
    def __str__(self):
        return self.ism

class Kitob(models.Model):
    JANR = (
        ["Detektiv", "Detektiv"],
        ["Drama", "Drama"],
        ["Fantastika", "Fantastika"],
        ["Ilmiy", "Ilmiy"],
        ["Diniy", "Diniy"],
        ["Tragediya", "Tragediya"]
    )

    nom = models.CharField(max_length=50)
    sahifa = models.PositiveIntegerField()
    yil = models.PositiveIntegerField()
    janr = models.CharField(max_length=20, choices=JANR)
    yozuvchi = models.ForeignKey(Yozuvchi, on_delete=models.CASCADE)
    aaa = models.CharField(max_length=150, null=True)

    def __str__(self):
        return self.nom


class Record(models.Model):
    JAVOB = (
        ["Ha", "Ha"],
        ["Yo'q", "Yo'q"]
    )
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    kitob = models.ForeignKey(Kitob, on_delete=models.CASCADE)
    sana = models.DateField()
    qaytardi = models.CharField(max_length=5, choices=JAVOB)
    qaytarilgan_sana = models.DateField()
    def __str__(self):
        return self.student.ism
















