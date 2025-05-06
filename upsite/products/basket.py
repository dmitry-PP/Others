from decimal import Decimal  # Используем Decimal для точных вычислений с десятичными числами
from upsite import settings  # Импортируем настройки Django
from .models import Product  # Импортируем модель Clothes из приложения shop


class Basket:
    """Класс Basket для управления корзиной товаров"""

    def __init__(self, request):
        """Конструктор класса, принимает объект запроса"""
        self.session = request.session  # Получаем сессию из запроса
        basket = self.session.get(settings.BASKET_SESSION_ID)  # Получаем корзину из сессии по ключу из настроек

        if not basket:  # Если корзины нет в сессии
            basket = self.session[settings.BASKET_SESSION_ID] = {}  # Создаем новую пустую корзину и сохраняем в сессии

        self.basket = basket  # Сохраняем ссылку на корзину в атрибуте экземпляра

    def __iter__(self):
        """Метод итерации, позволяет перебирать товары в корзине"""
        product_ids = self.basket.keys()  # Получаем список ID продуктов в корзине
        product_list = Product.objects.filter(pk__in=product_ids)  # Получаем queryset продуктов по их ID
        basket = self.basket.copy()  # Создаем копию корзины для итерации

        for product in product_list:  # Перебираем каждый продукт в queryset
            basket[str(product.pk)]['product'] = product  # Добавляем объект продукта в элемент корзины по его ID

        for item in basket.values():  # Перебираем каждый элемент корзины
            item['total_price'] = float(item['price']) * int(
                item['count'])  # Вычисляем общую стоимость элемента (цена * количество)
            yield item  # Возвращаем элемент корзины

    def __len__(self):
        """Метод, который возвращает количество товаров в корзине"""
        return sum(item['count'] for item in self.basket.values())  # Суммируем количество всех товаров в корзине

    def save(self):
        """Метод для сохранения текущего состояния корзины в сессии"""
        self.session[settings.BASKET_SESSION_ID] = self.basket  # Обновляем корзину в сессии
        self.session.modified = True  # Устанавливаем флаг модификации сессии

    def get(self, product):
        return self.basket.get(str(product.id), None)

    def add(self, product, count=1, update_count=False):
        """Метод для добавления товара в корзину"""
        product_id = str(product.id)  # Получаем ID продукта как строку

        if product_id not in self.basket:  # Если продукта еще нет в корзине
            self.basket[product_id] = {
                'count': 0,  # Создаем новый элемент корзины для продукта с количеством 0
                'price': str(product.price)  # и ценой продукта
            }

        if update_count:  # Если нужно обновить количество продукта
            self.basket[product_id]['count'] = count  # Устанавливаем новое количество
        else:  # Если нужно просто добавить количество
            self.basket[product_id]['count'] += count  # Увеличиваем текущее количество на указанное

        self.save()  # Сохраняем изменения в корзине

    def remove(self, product):
        """Метод для удаления товара из корзины"""
        product_id = str(product.id)  # Получаем ID продукта как строку

        if product_id in self.basket:  # Если продукт есть в корзине
            del self.basket[product_id]  # Удаляем продукт из корзины
            self.save()  # Сохраняем изменения в корзине

    def get_total_price(self):
        """Метод для получения общей стоимости с использованием Decimal"""
        return sum(Decimal(item['price']) * int(item['count']) for item in self.basket.values())

    def clear(self):
        """Метод для очистки корзины"""
        del self.session[settings.BASKET_SESSION_ID]  # Удаляем корзину из сессии
        self.session.modified = True  # Устанавливаем флаг модификации сессии