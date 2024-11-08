"""
Intent:
Factory Method is a creational design pattern that provides an interface for creating objects in a superclass,
but allows subclasses to alter the type of objects that will be created.

Scenario: Product Ordering System
Let's say we're building a product ordering system where we need to create different types of product orders,
such as PhysicalProduct and DigitalProduct. Each product type has unique attributes, and we want to ensure that
necessary information is validated upon creation.
The Factory Method will let us create instances of different product types without specifying the exact class in advance.
"""

from abc import ABC, abstractmethod


class Product(ABC):
    @abstractmethod
    def process_order(self):
        pass

class PhysicalProduct(Product):
    def __init__(self, shipping_address: str, weight: int):
        if not shipping_address:
            raise ValueError("Shipping address must be provided for physical products.")
        if weight <= 0:
            raise ValueError("Weight must be a positive value.")
        self.shipping_address = shipping_address
        self.weight = weight

    def process_order(self):
        print(
            f"Processing order for physical product to be shipped to {self.shipping_address} weighing {self.weight}kg.")

class DigitalProduct(Product):
    def __init__(self, email: str):
        if not email:
            raise ValueError("Email must be provided for digital products.")
        self.email = email

    def process_order(self):
        print(f"Processing order for digital product to be delivered to {self.email}.")

class ProductFactory:
    @staticmethod
    def create_product(product_type: str, **kwargs):
        if product_type == "physical":
            return PhysicalProduct(
                shipping_address=kwargs.get('shipping_address'),
                weight=kwargs.get('weight')
            )
        if product_type == "digital":
            return DigitalProduct(
                email=kwargs.get('email')
            )
        raise ValueError(f"Unknown product type: {product_type}")


if __name__ == '__main__':
    # Create and process order for physical product
    physical_product = ProductFactory.create_product(product_type="physical", shipping_address="123 Main St, Whitefield", weight=1000)
    physical_product.process_order()

    # Create and process order for digital product
    digital_product = ProductFactory.create_product(product_type="digital", email="customer@example.com")
    digital_product.process_order()
