#notes on python's "match" statement which is switch case

#given the if else code block below, we're gonna rewrite it using match
#match case is good if you're testing a variable against many conditions

#scenario with http codes
http_status = 4650

if http_status == 200 or http_status == 201:
    print("fdfd")
elif http_status == 400:
    print("Bad Request")
elif http_status == 404:
    print("Not Found")
elif http_status == 500 or http_status == 501:
    print("Server Error")
else: 
    print("unknown")


#trying to write it in switch statement format
match http_status:
    case 200 | 201:
        print("Success!!")
    case 400:
        print("Bad Request")
    case 404:
        print("Not Found")
    case 500 | 501:
        print("Server Error")
    case _:
        print("Unknown")