from typing import List
from .models import Products, ProductImage
from category.models import Category
from django.contrib.auth import get_user_model

User = get_user_model()


def create_product_image(*, product: Products, image, label: str = None) -> ProductImage:
    product_image = ProductImage.objects.create(
        product=product,
        image=image,
        label=label,
    )
    print('ll', product_image)
    return product_image



def create_product(
    *,
    name: str,
    description: str,
    price: float,
    created_by: str,
    stock: int,
    category: str,
    images: List[dict],
) -> Products:
    """
    Service to create a product along with its images.

    Args:
        name (str): Name of the product.
        description (str): Description of the product.
        price (float): Price of the product.
        created_by (str): Email of the user who creates the product.
        stock (int): Available stock for the product.
        category (sting): ID of the category the product belongs to.
        images (list): List of images with "image" and "label" fields.

    Returns:
        Products: The created product instance.
    """
    # Fetch related objects

    print(created_by)
    category_obj = Category.objects.get(id=category)

    # Create the product
    product = Products.objects.create(
        name=name,
        description=description,
        price=price,
        created_by=created_by,
        category=category_obj,
        stock=stock,
    )

    # Create associated product images
    print("i",images)

    for img_data in images:
        print("iii",img_data["image"])
        create_product_image(product=product, image=img_data["image"], label=img_data.get("label"))

    return product


def update_product(
    *,
    name: str,
    description: str,
    price: float,
    stock: int,
    category: str,
    images: List[dict],  # List of image objects with 'image' and 'label'
    product_id: str  # The ID of the product to update
) -> Products:
    # Fetch the existing product by ID
    try:
        product = Products.objects.get(id=product_id)
    except Products.DoesNotExist:
        raise ValueError(f"Product with ID {product_id} does not exist.")

    # Update the fields of the existing product
    category_obj = Category.objects.get(id=category)
    product.name = name
    product.description = description
    product.price = price
    product.stock = stock
    product.category = category_obj

    # Save the updated product
    product.save()

    # Update or create ProductImage instances for the images
    for image_data in images:
        # Check if image already exists for this product, and update it if necessary
        if 'id' in image_data:  # Image update logic
            try:
                product_image = ProductImage.objects.get(id=image_data['id'], product=product)
                product_image.image = image_data['image']
                product_image.label = image_data.get('label', product_image.label)  # Preserve old label if not updated
                product_image.save()
            except ProductImage.DoesNotExist:
                # If image doesn't exist, create a new one
                ProductImage.objects.create(
                    product=product,
                    image=image_data['image'],
                    label=image_data.get('label', '')
                )
        else:
            # Create new images if no image id is provided
            ProductImage.objects.create(
                product=product,
                image=image_data['image'],
                label=image_data.get('label', '')
            )

    return product

def reduce_stock(product: Products, quantity: int) -> int:
    """
    Service to reduce the stock of a product.

    Args:
        product (Products): The product to reduce stock for.
        quantity (int): Quantity to reduce.

    Returns:
        int: The remaining stock of the product.

    Raises:
        ValueError: If the stock is insufficient.
    """
    if product.stock < quantity:
        raise ValueError("Insufficient Product Stock")

    product.stock -= quantity
    product.save(update_fields=["stock"])

    return product.stock


