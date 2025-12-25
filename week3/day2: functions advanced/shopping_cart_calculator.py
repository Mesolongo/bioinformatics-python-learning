def calculate_total(*args, **kwargs):
    # Your code here
    total_price = 0
    discount = kwargs.get('discount',0)
    tax_rate = kwargs.get('tax_rate',0.10)

    for cost in args:
        total_price += cost
    discounted_total = total_price * (1-discount)
    total_after_tax = discounted_total * (1+tax_rate)

    return total_after_tax

# Test cases
print(calculate_total(10, 20, 30))
print(calculate_total(100, 50, discount=0.2))
print(calculate_total(50, 50, tax_rate=0.15, discount=0.1))