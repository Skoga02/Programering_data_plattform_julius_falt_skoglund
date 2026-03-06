from pydantic import BaseModel, Field

# gt, descr, min/max

class ProductSchema(BaseModel):
    name: str = Field(min_length=2, max_length=50, description="Name must be between 2-50 chars")
    price: float = Field(gt=0, description="Price must be greater than 0")
    quantity: int = Field(gt=0, lt=50, description="Quantity must be greater than 0")
    sku: str = Field(
        pattern=r"^SKU-\d{4}$",
        description="Format must be SKU-1234"
    )

    # ^SKU-
    # \d [0-9]
    # {4} (amount of digits)
    # $ == end
    # TODO - Bonus material : REGEX