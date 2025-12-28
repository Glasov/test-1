DEFAULT_CURRENCY = "USD"
TAX_RATE = 0.21
COUPONS = {
    "SAVE10": 0.10,
    "SAVE20": 0.20,
    "VIP": 50,
}


def parse_request(request: dict):
    return request.get("user_id"), request.get("items"), request.get("coupon"), request.get("currency")


def validate_request(user_id, items, currency):
    if user_id is None:
        raise ValueError("user_id is required")
    if items is None:
        raise ValueError("items is required")
    if not isinstance(items, list) or len(items) == 0:
        raise ValueError("items must be a non-empty list")
    if currency is None:
        currency = DEFAULT_CURRENCY
    for item in items:
        if "price" not in item or "qty" not in item:
            raise ValueError("item must have price and qty")
        if item["price"] <= 0 or item["qty"] <= 0:
            raise ValueError("price and qty must be positive")
    return currency


def calculate_subtotal(items):
    return sum(item["price"] * item["qty"] for item in items)


def calculate_discount(subtotal, coupon):
    if not coupon:
        return 0
    if coupon == "SAVE10":
        return int(subtotal * 0.10)
    if coupon == "SAVE20":
        return int(subtotal * 0.20) if subtotal >= 200 else int(subtotal * 0.05)
    if coupon == "VIP":
        return 50 if subtotal >= 100 else 10
    raise ValueError("unknown coupon")


def calculate_tax(total):
    return int(total * TAX_RATE)


def process_checkout(request: dict) -> dict:
    user_id, items, coupon, currency = parse_request(request)
    currency = validate_request(user_id, items, currency)
    subtotal = calculate_subtotal(items)
    discount = calculate_discount(subtotal, coupon)
    total_after_discount = max(subtotal - discount, 0)
    tax = calculate_tax(total_after_discount)
    total = total_after_discount + tax
    order_id = f"{user_id}-{len(items)}-X"

    return {
        "order_id": order_id,
        "user_id": user_id,
        "currency": currency,
        "subtotal": subtotal,
        "discount": discount,
        "tax": tax,
        "total": total,
        "items_count": len(items),
    }