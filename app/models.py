from django.db import models


class Breed(models.Model):
    name = models.CharField(max_length=250, null=False, blank=False)

    class Meta:
        verbose_name = 'Raza'
        verbose_name_plural = 'Razas'

    def __unicode__(self):
        return self.name


class BaseBull(models.Model):
    code = models.CharField(max_length=15, null=False, blank=False)
    name = models.CharField(max_length=250, null=False, blank=False)
    register_number = models.CharField(max_length=250, null=False, blank=False)
    breed = models.ForeignKey(Breed)

    class Meta:
        abstract = True


class PhotoBull(models.Model):
    bull = models.ForeignKey(BaseBull, default=None)
    image = models.ImageField(upload_to="bull_images/",
                              verbose_name='Image', )


class BullMeat(BaseBull):
    father = models.CharField(max_length=250, null=True, blank=True)
    mother = models.CharField(max_length=250, null=True, blank=True)
    comment = models.TextField()
    pedigree = models.FileField(upload_to = "pedigree/pdf", null=True, blank=True)
    weight = models.CharField(max_length=50, null=True, blank=True)
    birth_weight = models.CharField(max_length=50, null=True, blank=True)
    weaning_weight = models.CharField(max_length=50, null=True, blank=True)
    one_yo_weight = models.CharField(max_length=50, null=True, blank=True)
    adult_weight = models.CharField(max_length=50, null=True, blank=True)
    scrotal_circumference = models.CharField(max_length=50, null=True, blank=True)
    long_rump = models.CharField(max_length=50, null=True, blank=True)
    rump_width = models.CharField(max_length=50, null=True, blank=True)
    rump_height = models.CharField(max_length=50, null=True, blank=True)
    body_length = models.CharField(max_length=50, null=True, blank=True)
    tatoo = models.CharField(max_length=50, null=True, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    breeder = models.CharField(max_length=250, null=True, blank=True)
    number_offspring = models.CharField(max_length=50, null=True, blank=True)
    stables = models.CharField(max_length=50, null=True, blank=True)
    PN = models.CharField(max_length=50, null=True, blank=True)
    prec_PN = models.CharField(max_length=50, null=True, blank=True)
    AM = models.CharField(max_length=50, null=True, blank=True)
    prec_AM = models.CharField(max_length=50, null=True, blank=True)
    LYC = models.CharField(max_length=50, null=True, blank=True)
    prec_LYC = models.CharField(max_length=50, null=True, blank=True)
    PF = models.CharField(max_length=50, null=True, blank=True)
    prec_PF = models.CharField(max_length=50, null=True, blank=True)
    CE =models.CharField(max_length=50, null=True, blank=True)
    prec_CE = models.CharField(max_length=50, null=True, blank=True)
    AOB = models.CharField(max_length=50, null=True, blank=True)
    prec_AOB = models.CharField(max_length=50, null=True, blank=True)
    EGD = models.CharField(max_length=50, null=True, blank=True)
    prec_EGD = models.CharField(max_length=50, null=True, blank=True)
    EGC = models.CharField(max_length=50, null=True, blank=True)
    prec_EGC = models.CharField(max_length=50, null=True, blank=True)
    GI = models.CharField(max_length=50, null=True, blank=True)
    prec_GI = models.CharField(max_length=50, null=True, blank=True)

class BreedMilk(BaseBull):
    nickname = models.CharField(max_length=250, null=True, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    PTAT = models.CharField(max_length=50, null=True, blank=True)
    JUI = models.CharField(max_length=50, null=True, blank=True)
    #Production
    milk = models.CharField(max_length=50, null=True, blank=True)
    protein = models.CharField(max_length=50, null=True, blank=True)
    fat = models.CharField(max_length=50, null=True, blank=True)
    cheese_merit = models.CharField(max_length=50, null=True, blank=True)
    #health_traits
    productive_life = models.CharField(max_length=50, null=True, blank=True)
    prize_rate_daughters = models.CharField(max_length=50, null=True, blank=True)
    somatic_cell_evaluation = models.CharField(max_length=50, null=True, blank=True)
    conception_rate_heifers = models.CharField(max_length=50, null=True, blank=True)
    conception_rate_adults = models.CharField(max_length=50, null=True, blank=True)
    fertility_index = models.CharField(max_length=50, null=True, blank=True)
    ease_birth_bull = models.CharField(max_length=50, null=True, blank=True)
    ease_birth_daughters = models.CharField(max_length=50, null=True, blank=True)


class BullDoublePurpose(BaseBull):
    father = models.CharField(max_length=250, null=True, blank=True)
    mother = models.CharField(max_length=250, null=True, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    comment = models.TextField()
    #Produccion
    pedigree = models.FileField(upload_to="pedigree/pdf", null=True, blank=True)
    ISU = models.CharField(max_length=50, null=True, blank=True)
    dairy_economic_index = models.CharField(max_length=50, null=True, blank=True)
    protein = models.CharField(max_length=50, null=True, blank=True)
    fat = models.CharField(max_length=50, null=True, blank=True)
    protein_percentage = models.CharField(max_length=50, null=True, blank=True)
    fat_percentage = models.CharField(max_length=50, null=True, blank=True)
    milk_KG = models.CharField(max_length=50, null=True, blank=True)
    #end_production
    udder_health = models.CharField(max_length=50, null=True, blank=True)
    somatic_cells = models.CharField(max_length=50, null=True, blank=True)
    clinical_mastitis = models.CharField(max_length=50, null=True, blank=True)
    reproduction = models.CharField(max_length=50, null=True, blank=True)
    fertility_cows = models.CharField(max_length=50, null=True, blank=True)
    fertility_heifers = models.CharField(max_length=50, null=True, blank=True)
    longevity = models.CharField(max_length=50, null=True, blank=True)
    fertility_cows = models.CharField(max_length=50, null=True, blank=True)
    fac_birthday = models.CharField(max_length=50, null=True, blank=True)
    fac_birth_daughters = models.CharField(max_length=50, null=True, blank=True)
    paternal_mortality = models.CharField(max_length=50, null=True, blank=True)
    maternal_mortality = models.CharField(max_length=50, null=True, blank=True)


class BullEembryo(BaseBull):
    father = models.CharField(max_length=250, null=True, blank=True)
    father_registry = models.CharField(max_length=250, null=True, blank=True)
    origin = models.CharField(max_length=50, null=True, blank=True)
    mother = models.CharField(max_length=250, null=True, blank=True)
    mother_registry = models.CharField(max_length=250, null=True, blank=True)
    type_of_obtaining = models.CharField(max_length=250, null=True, blank=True)
    breed_percentage = models.CharField(max_length=250, null=True, blank=True)
    TPI = models.CharField(max_length=50, null=True, blank=True)
    NM = models.CharField(max_length=50, null=True, blank=True)
    M = models.CharField(max_length=50, null=True, blank=True)
    F = models.CharField(max_length=50, null=True, blank=True)
    P = models.CharField(max_length=50, null=True, blank=True)
    PL = models.CharField(max_length=50, null=True, blank=True)
    DPR = models.CharField(max_length=50, null=True, blank=True)
    SCS = models.CharField(max_length=50, null=True, blank=True)
    T = models.CharField(max_length=50, null=True, blank=True)
    UDC = models.CharField(max_length=50, null=True, blank=True)
    FLC = models.CharField(max_length=50, null=True, blank=True)
    SCE = models.CharField(max_length=50, null=True, blank=True)
    LPI = models.CharField(max_length=50, null=True, blank=True)
    GEBV = models.CharField(max_length=50, null=True, blank=True)
    pro_GEBV = models.CharField(max_length=50, null=True, blank=True)