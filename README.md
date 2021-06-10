# flaskmongodocker

To access the api your first need to send a registration POST:
## General endpoints
http://0.0.0.0:5000/register
{
    "username": "yourname",
    "password": "anypassword"
}

You have a limited number of uses the API, to recharge use:
http://0.0.0.0:5000/refill
{
    "username": "yourname",
    "password": "abc123",           //this admin password must be used to refill
    "refill" : 6                    //recharge the number of times to use api with this user
}



