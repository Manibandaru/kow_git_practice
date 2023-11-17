import json
#
# example=open("example_nested_dict.json", "r")
# data=example.read()
# obj=json.loads(data)
#
# a = obj['child1']
# b= obj['child2']
# c= obj['child3']
# print(a,b,c)


##or

# with open("example_nested_dict.json", "r") as example:
#     data=json.load(example)
#     print(data)


# person = '{"name": "Bob", "languages": ["English", "French"]}'
# person_dict = json.loads(person)
# print(person_dict['name'])


###### json loads function is used to read data from string
###### json load function is used to read data from file both returns python object
###### json dumps is used to convert dictionary to json
###### json dump method is used to write json to a file


"""create table shopping_trend (
Customer ID int
Age	varchar(500)
Gender	varchar(500)
Item varchar(500)
Purchased	 varchar(500)
Category	varchar(500)
Purchase Amount (USD)	varchar(500)
Location	varchar(500)
Size	varchar(500)
Color	varchar(500)
Season	varchar(500)
Review varchar(500)
Rating	varchar(500)
Subscription varchar(500)
Status	varchar(500)
Shipping Type	varchar(500)
Discount Applied	varchar(500)
Promo Code Used	varchar(500)
Previous Purchases	varchar(500)
Payment Method	varchar(500)
Frequency of Purchases varchar(500)
)"""