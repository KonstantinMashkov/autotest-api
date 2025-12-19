from clients.public_http_builder import get_public_http_client
from clients.private_http_builder import AuthentificationUserDict
from clients.user.public_users_client import UserRequestDict, get_public_users_client
from clients.user.private_users_client import get_private_users_client
from tools.fakers import get_random_email


public_users_client = get_public_users_client()

create_user_request = UserRequestDict(
    email=get_random_email(),
    password="string",
    lastName="string",
    firstName="string",
    middleName="string"
)

create_user_response = public_users_client.create_user_api(create_user_request)
create_user_response_data = create_user_response.json()
print(create_user_response_data)


authentication_user = AuthentificationUserDict(
    email=create_user_request["email"],
    password=create_user_request["password"]
)

private_users_client = get_private_users_client(authentication_user)
get_user_response = private_users_client.get_users_view_api(create_user_response_data['user']['id'])
get_user_response_data = get_user_response.json()
print(get_user_response_data)