def make_car(brand, model, **car_info):
    """Build a dictionary containing everything we know about a car."""
    car_info['brand_name'] = brand
    car_info['model_name'] = model
    return car_info

subaru_car_profile = make_car('Subaru', 'Outback', color='Red', owner='ehmiiz', climbes='mountains')
volvo_car_profile = make_car('Volvo', '240', color='Black', owner='pappo', climbes='gas bills')

print(volvo_car_profile)

print(subaru_car_profile)