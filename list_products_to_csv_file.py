# product_file = "products.csv"
import csv
from woocommerce import API

wcapi = API(
    url="http://localhost:8888/localstore/",
    consumer_key="ck_1f85ae2d2bdf68d790036e1b00408bfdb2554d15",
    consumer_secret="cs_54af5850f024d8ca6153462e921fac4c082fd575",
    version="wc/v3"
)


rs_api = wcapi.get("products", params={"per_page": 50})
status_code = rs_api.status_code
# assert status_code == 200, f"Expected a '200' status code but got {status_code}"
# above code does exactly what below code does
if status_code != 200:
    raise Exception(f"Expected a '200' status code but got {status_code}")

all_products = rs_api.json()
filename = "all_products.csv"

with open(filename, "w", newline="") as csvfile:
    fieldnames = ["name", "price"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for product in all_products:
        name = product["name"]
        price = product["price"]

        writer.writerow({"name": name, "price": price})


# for i in all_products:
#     print(i['name'],i['price'])

# breakpoint()