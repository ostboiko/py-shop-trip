import jsonimport datetimefrom app.customer import Customerfrom app.car import Carfrom app.shop import Shopdef shop_trip() -> None:    global shop    with open('app/config.json', 'r') as config_file:        config_data = json.load(config_file)    FUEL_PRICE = config_data["FUEL_PRICE"]    customers_data = config_data["customers"]    shops_data = config_data["shops"]    customers = []    cars = []    shops = []    for customer_data in customers_data:        car_data = customer_data["car"]        car = Car(car_data["brand"], car_data["fuel_consumption"])        cars.append(car)        customer = Customer(            customer_data["name"],            customer_data["product_cart"],            customer_data["location"],            car,            customer_data["money"],        )        customers.append(customer)    for shop_data in shops_data:        shop = Shop(            shop_data["name"],            shop_data["location"],            shop_data["products"]        )        shops.append(shop)    for customer in customers:        print(f"{customer.name} has {customer.money} dollars")        cheapest_shop = None        cheapest_cost = float('inf')        for shop in shops:            trip_cost = customer.calculate_trip_cost(shop, FUEL_PRICE)            print(f"{customer.name}'s trip to the {shop.name} costs {trip_cost}")            if customer.calculate_money(shop):                if trip_cost < cheapest_cost:                    cheapest_cost = trip_cost                    cheapest_shop = shop        if cheapest_shop is not None:            print(f"{customer.name} rides to {cheapest_shop.name}\n")            current_time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")            receipt = cheapest_shop.generate_receipt(customer, current_time)            print(receipt)            last_money = customer.money - cheapest_shop            print(f"{customer.name} now has {last_money} dollars\n")        else:            print(f"{customer.name} doesn't have enough money to make a purchase in any shop")