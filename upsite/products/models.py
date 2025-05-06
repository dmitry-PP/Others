from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse


class Farmer(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя фермера")
    contact = models.CharField(max_length=20, verbose_name="Контактный телефон")
    address = models.TextField(verbose_name="Адрес фермы")
    description = models.TextField(verbose_name="Описание хозяйства")
    photo = models.ImageField(upload_to='farmers/', default="farmers/unknown.jpg", verbose_name="Фото фермера", null=True, blank=True)
    registration_number = models.CharField(
        max_length=50,
        verbose_name="Регистрационный номер",
        unique=True,
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата регистрации")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('farmer_detail', kwargs={"pk": self.pk})

    class Meta:
        verbose_name = "Фермер"
        verbose_name_plural = "Фермеры"

class Category(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Название категории")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={"pk": self.pk})

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

class UnitOfMeasurement(models.Model):
    name = models.CharField(max_length=10, unique=True, verbose_name="Единица измерения")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('unit_detail', kwargs={"pk": self.pk})

    class Meta:
        verbose_name = "Единица измерения"
        verbose_name_plural = "Единицы измерения"

class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0.01)],
        verbose_name="Цена"
    )
    quantity = models.PositiveIntegerField(verbose_name="Количество")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    image = models.ImageField(upload_to='products/', verbose_name="Изображение")
    squirrels = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Белки")
    fats = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Жиры")
    carbohydrates = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Углеводы")
    calorie_content = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Калорийность")
    composition = models.TextField(verbose_name="Состав")
    additional_info = models.TextField(verbose_name="Дополнительная информация", blank=True, null=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name="Категория"
    )
    unit_of_measurement = models.ForeignKey(
        UnitOfMeasurement,
        on_delete=models.CASCADE,
        verbose_name="Единица измерения"
    )

    farmer = models.ForeignKey(
        Farmer,
        on_delete=models.CASCADE,
        verbose_name="Фермер", null=True
    )

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.name} ({self.category.name})"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

class Status(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Название статуса")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('status_detail', kwargs={"pk": self.pk})

    class Meta:
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"

class OrderItem(models.Model):
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0.01)],
        verbose_name="Цена"
    )
    quantity = models.PositiveIntegerField(
        validators=[MinValueValidator(1)],
        verbose_name="Количество"
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name="Продукт"
    )

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

    class Meta:
        verbose_name = "Элемент заказа"
        verbose_name_plural = "Элементы заказа"

class Order(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        verbose_name="Пользователь"
    )
    order_item = models.ForeignKey(
        OrderItem,
        on_delete=models.CASCADE,
        verbose_name="Элемент заказа"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    comment = models.TextField(null=True, blank=True, verbose_name="Комментарий")
    fio = models.CharField(max_length=100, verbose_name="ФИО")
    delivery_date = models.DateTimeField(verbose_name="Дата доставки")
    address = models.TextField(verbose_name="Адрес доставки")
    status = models.ForeignKey(
        Status,
        on_delete=models.CASCADE,
        verbose_name="Статус заказа"
    )
    total_sum = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Общая сумма")


    def __str__(self):
        return f"Заказ #{self.id}"

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

class Cart(models.Model):
    quantity = models.PositiveIntegerField(
        validators=[MinValueValidator(1)],
        verbose_name="Количество"
    )
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        verbose_name="Пользователь"
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name="Продукт"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")



    def __str__(self):
        return f"{self.quantity} x {self.product.name} (пользователь: {self.user.username})"

    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Корзины"

class Review(models.Model):
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        verbose_name="Рейтинг"
    )
    comment = models.TextField(verbose_name="Комментарий", blank=True, default='')
    created_at = models.DateField(auto_now_add=True, verbose_name="Дата создания")
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        verbose_name="Пользователь"
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name="Продукт"
    )

    def __str__(self):
        return f"Отзыв на {self.product.name} от {self.user.username}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
