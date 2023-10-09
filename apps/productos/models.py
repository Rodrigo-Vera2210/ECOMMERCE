from django.db import models
from apps.base.models import BaseModel
from simple_history.models import HistoricalRecords

class MeasureUnit(BaseModel):

    description = models.CharField('Descripción', max_length=50, blank=False, null=False, unique=True)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = 'Unidad de Medida'
        verbose_name_plural = 'Unidad de Medidas'

    def __str__(self):
        return self.description
    
class CategoryProduct(BaseModel):

    description = models.CharField('Descripción', max_length=50, blank=False, null=False, unique=True)
    measure_unit = models.ForeignKey(MeasureUnit, on_delete=models.CASCADE, verbose_name='Unidad de Medida')
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Categoría de Producto'
        verbose_name_plural = 'Categoría de Productos'

class Indicador(models.Model):
    """Model definition for Indicador."""

    # TODO: Define fields here
    descount_value = models.PositiveSmallIntegerField(default =   0)
    category_product = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE, verbose_name='Indicador de Oferta')
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        """Meta definition for Indicador."""

        verbose_name = 'Indicador de Oferta'
        verbose_name_plural = 'Indicadores de Ofertas'

    def __str__(self):
        """Unicode representation of Indicador."""
        return f'Oferta de la categoría {self.category_product} : {self.descount_value}%'

class Product(BaseModel):
    """Model definition for Product."""

    # TODO: Define fields here
    name =models.CharField('Nombre de Producto', max_length=150, unique = True, blank = False, null = False)
    description = models.TextField('Descripción de Producto', blank=False, null=False)
    image = models.ImageField('Imagen del Producto', upload_to='products/', blank=True, null=True)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        """Meta definition for Product."""

        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        """Unicode representation of Product."""
        pass
