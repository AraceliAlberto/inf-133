from zeep import Client

client = Client(
    "https://www.dataaccess.com/webservicesserver/NumberConversion.wso?WSDL"
)

result = client.service.NumberToWords(7)
print(result)

# --> Tarea Soap
result2 = client.service.NumberToDollars(5)
print(result2)