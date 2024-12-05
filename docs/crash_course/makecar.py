def make_car(brand, model, **car_info):
    """Build a dictionary containing everything we know about a car."""
    car_info['brand_name'] = brand
    car_info['model_name'] = model
    print(car_info)