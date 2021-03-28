from src.observer.shop import Product, Purchase

if __name__ == '__main__':
    p1 = Product()
    p2 = Product()
    p3 = Product()
    p4 = Product()
    p5 = Product()

    purchase = Purchase([p1, p2, p3, p4, p5])
    purchase.checkout()
    """we can use this without any patterns and each time call this line."""
    # EmailNotification.send('checkout is done ')
    """or write observer pattern using the decorator pattern like this"""
    purchase.cancel()
