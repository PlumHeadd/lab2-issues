TAX_RATE = 0.19


def total(price):
    return price * (1 + TAX_RATE)


def discount(price, pct):
    return price * (1 - pct / 100)
