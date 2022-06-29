@user_apis_api
Feature: Users API endpoint
  description

  This feature file contain test related to Part C.1 (API Testing, Python)


@TC-1 @user_api
Scenario: Create/Get/Update/Delete(POST/PUT/GET/DELETE) for User endpoint should be successful with respective status code (Positive case)

When user tries to create a user "U1" with all the fields by using API endpoint as "createWithArray"
Then user gets "200" and can verify user details in response json of user "U1"

When user tries to get user "U1" by its name
Then user gets "200" and can verify user details in response json of user "U1" under get response

When user tries to update user "U1"
Then user gets "200" and can verify user details in response json of user "U1" under patch response

When user tries to delete user "U1"
Then user gets "200" and can verify user details in response json of user "U1" under delete response

When user tries to get user "U1" by its name
Then user gets "404" and can verify user details in response json of user "U1" under get response


@TC-2 @user_api
Scenario: Verify that user can create multiple users by using POST (/v2/user/createWithArray) in one POST call

When user tries to creates multiple user "U1,U2,U3" with all the fields by using API endpoint as "createWithArray"
Then user gets "200" and can verify user details in response json of user "U1,U2,U3"



@TC-3 @user_api
Scenario:When user tries to create user by using POST (/v2/user/createWithArray) with wrong payload or any/all field missing in payload the he should get 422

When user tries to create a user "U1" with all the fields but with field "all_the_fields" "missing" by using API endpoint as "createWithArray"
Then user gets "422" and can verify user details in response json of user "U1"

When user tries to create a user "U1" with all the fields but with field "as" "wrong_parameters" by using API endpoint as "createWithArray"
Then user gets "422" and can verify user details in response json of user "U1"

When user tries to create a user "U1" with all the fields but with field "username" "missing" by using API endpoint as "createWithArray"
Then user gets "422" and can verify user details in response json of user "U1"

When user tries to create a user "U1" with all the fields but with field "firstName" "missing" by using API endpoint as "createWithArray"
Then user gets "422" and can verify user details in response json of user "U1"

When user tries to create a user "U1" with all the fields but with field "lastName" "missing" by using API endpoint as "createWithArray"
Then user gets "422" and can verify user details in response json of user "U1"

When user tries to create a user "U1" with all the fields but with field "email" "missing" by using API endpoint as "createWithArray"
Then user gets "422" and can verify user details in response json of user "U1"

When user tries to create a user "U1" with all the fields but with field "password" "missing" by using API endpoint as "createWithArray"
Then user gets "422" and can verify user details in response json of user "U1"

When user tries to create a user "U1" with all the fields but with field "phone" "missing" by using API endpoint as "createWithArray"
Then user gets "422" and can verify user details in response json of user "U1"


@TC-4 @user_api
Scenario:When user tries to create user by using POST (/v2/user/createWithArray) with parametric value as "empty string"


When user tries to create a user "U1" with all the fields but with field "username" as "empty string" by using API endpoint as "createWithArray"
Then user gets "422" and can verify user details in response json of user "U1"

When user tries to create a user "U1" with all the fields but with field "username" with "trailing spaces" by using API endpoint as "createWithArray"
Then user gets "422" and can verify user details in response json of user "U1"

When user tries to create a user "U1" with all the fields but with field "firstName" as "leading spaces" by using API endpoint as "createWithArray"
Then user gets "422" and can verify user details in response json of user "U1"

When user tries to create a user "U1" with all the fields but with field "lastName" as "empty string" by using API endpoint as "createWithArray"
Then user gets "422" and can verify user details in response json of user "U1"

When user tries to create a user "U1" with all the fields but with field "email" as "empty string" by using API endpoint as "createWithArray"
Then user gets "422" and can verify user details in response json of user "U1"

When user tries to create a user "U1" with all the fields but with field "password" as "empty string" by using API endpoint as "createWithArray"
Then user gets "422" and can verify user details in response json of user "U1"

When user tries to create a user "U1" with all the fields but with field "phone" as "empty string" by using API endpoint as "createWithArray"
Then user gets "422" and can verify user details in response json of user "U1"


@TC-5 @user_api
Scenario: When user tries to call GET endpoint (/v2/user/<user_name>) after user is deleted from the system or try to GET invalid user then response should be 404

When user tries to create a user "U1" with all the fields by using API endpoint as "createWithArray"
Then user gets "200" and can verify user details in response json of user "U1"

When user tries to delete user "U1"
Then user gets "200" and can verify user details in response json of user "U1" under delete response

When user tries to get user "U1" by its name
Then user gets "404" and can verify user details in response json of user "U1" under get response

When user tries to get user "invalid_user_name" by "invalid_user_name"
Then user gets "404" and can verify user details in response json of user "invalid_user_name" under get response



@TC-6 @user_api
Scenario: When user tries to do PUT (/v2/user/<user_name>) operation with invalid parameters

When user tries to create a user "U1" with all the fields by using API endpoint as "createWithArray"
Then user gets "200" and can verify user details in response json of user "U1"

When user tries to update user "U1" with "invalid" parameters
Then user gets "422" and can verify user details in response json of user "U1" under patch response


@TC-7 @user_api
Scenario: When user tries to do PUT (/v2/user/<user_name>) operation with user after it is deleted from the system, then PUT should return 404

When user tries to create a user "U1" with all the fields by using API endpoint as "createWithArray"
Then user gets "200" and can verify user details in response json of user "U1"

When user tries to get user "U1" by its name
Then user gets "200" and can verify user details in response json of user "U1" under get response

When user tries to delete user "U1"
Then user gets "200" and can verify user details in response json of user "U1" under delete response

When user tries to update user "U1"
Then user gets "404" and can verify user details in response json of user "U1" under patch response



@TC-8 @user_api
Scenario: When user tries to do PUT (/v2/user/<user_name>) operation with no data in payload

When user tries to create a user "U1" with all the fields by using API endpoint as "createWithArray"
Then user gets "200" and can verify user details in response json of user "U1"

When user tries to update user "U1" with "no_payload" parameters
Then user gets "422" and can verify user details in response json of user "U1" under patch response


@TC-9 @user_api
Scenario: When user tries to delete the User (/v2/user/<user_name>) again after it was deleted first, then user should get 404

When user tries to create a user "U1" with all the fields by using API endpoint as "createWithArray"
Then user gets "200" and can verify user details in response json of user "U1"

When user tries to delete user "U1"
Then user gets "200" and can verify user details in response json of user "U1" under delete response

When user tries to delete user "U1"
Then user gets "404" and can verify user details in response json of user "U1" under delete response


@TC-10 @user_api
Scenario: When user tries to delete (/v2/user/<user_name>) the invalid user/non existent user in the system, then user should get 404

When user tries to delete user "invalid_user"
Then user gets "404" and can verify user details in response json of user "invalid_user" under delete response

################################### v2/user  ,v2/user/createWithList and v2/user/createWithArray  since all of them are similar in term of payload##############
################################## So we can reuse same set of old test for this endpoiint "v2/user/createWithList" which we have written for "v2/user/createWithArray"#####


@TC-11 @user_api
Scenario: Create/Get/Update/Delete(POST/PUT/GET/DELETE) for User endpoint should be successful with respective status code (Positive case)

When user tries to create a user "U1" with all the fields by using API endpoint as "createWithList"
Then user gets "200" and can verify user details in response json of user "U1"

When user tries to get user "U1" by its name
Then user gets "200" and can verify user details in response json of user "U1" under get response

When user tries to update user "U1"
Then user gets "200" and can verify user details in response json of user "U1" under patch response

When user tries to delete user "U1"
Then user gets "200" and can verify user details in response json of user "U1" under delete response

When user tries to get user "U1" by its name
Then user gets "404" and can verify user details in response json of user "U1" under get response


@TC-12 @user_api
Scenario: Verify that user can create multiple users by using POST (/v2/user/createWithList) in one POST call

When user tries to creates multiple user "U1,U2,U3" with all the fields by using API endpoint as "createWithList"
Then user gets "200" and can verify user details in response json of user "U1,U2,U3"

@TC-13 @user_api
Scenario:When user tries to create user by using POST (/v2/user/createWithList) with wrong payload or any/all field missing in payload the he should get 422

When user tries to create a user "U1" with all the fields but with field "all_the_fields" "missing" by using API endpoint as "createWithList"
Then user gets "422" and can verify user details in response json of user "U1"

When user tries to create a user "U1" with all the fields but with field "as" "wrong_parameters" by using API endpoint as "createWithList"
Then user gets "422" and can verify user details in response json of user "U1"

When user tries to create a user "U1" with all the fields but with field "username" "missing" by using API endpoint as "createWithList"
Then user gets "422" and can verify user details in response json of user "U1"

When user tries to create a user "U1" with all the fields but with field "firstName" "missing" by using API endpoint as "createWithList"
Then user gets "422" and can verify user details in response json of user "U1"

When user tries to create a user "U1" with all the fields but with field "lastName" "missing" by using API endpoint as "createWithList"
Then user gets "422" and can verify user details in response json of user "U1"

When user tries to create a user "U1" with all the fields but with field "email" "missing" by using API endpoint as "createWithList"
Then user gets "422" and can verify user details in response json of user "U1"

When user tries to create a user "U1" with all the fields but with field "password" "missing" by using API endpoint as "createWithList"
Then user gets "422" and can verify user details in response json of user "U1"

When user tries to create a user "U1" with all the fields but with field "phone" "missing" by using API endpoint as "createWithList"
Then user gets "422" and can verify user details in response json of user "U1"


@TC-14 @user_api
Scenario:When user tries to create user by using POST (/v2/user/createWithArray) with parametric value as "empty string"


When user tries to create a user "U1" with all the fields but with field "username" as "empty string" by using API endpoint as "createWithList"
Then user gets "422" and can verify user details in response json of user "U1"

When user tries to create a user "U1" with all the fields but with field "username" with "trailing spaces" by using API endpoint as "createWithList"
Then user gets "422" and can verify user details in response json of user "U1"

When user tries to create a user "U1" with all the fields but with field "firstName" as "leading spaces" by using API endpoint as "createWithList"
Then user gets "422" and can verify user details in response json of user "U1"

When user tries to create a user "U1" with all the fields but with field "lastName" as "empty string" by using API endpoint as "createWithList"
Then user gets "422" and can verify user details in response json of user "U1"

When user tries to create a user "U1" with all the fields but with field "email" as "empty string" by using API endpoint as "createWithList"
Then user gets "422" and can verify user details in response json of user "U1"

When user tries to create a user "U1" with all the fields but with field "password" as "empty string" by using API endpoint as "createWithList"
Then user gets "422" and can verify user details in response json of user "U1"

When user tries to create a user "U1" with all the fields but with field "phone" as "empty string" by using API endpoint as "createWithList"
Then user gets "422" and can verify user details in response json of user "U1"

################################### v2/user  ,v2/user/createWithList and v2/user/createWithArray  since all of them are similar in term of payload##############
################################## So we can reuse same set of old test for this endpoiint "v2/user" which we have written for "v2/user/createWithArray"#####


@TC-15 @user_api
Scenario: Create/Get/Update/Delete(POST/PUT/GET/DELETE) for User endpoint should be successful with respective status code (Positive case)

When user tries to create a user "U1" with all the fields by using API endpoint as "standalone_user_endpoint"
Then user gets "200" and can verify user details in response json of user "U1"

When user tries to get user "U1" by its name
Then user gets "200" and can verify user details in response json of user "U1" under get response

When user tries to update user "U1"
Then user gets "200" and can verify user details in response json of user "U1" under patch response

When user tries to delete user "U1"
Then user gets "200" and can verify user details in response json of user "U1" under delete response

When user tries to get user "U1" by its name
Then user gets "404" and can verify user details in response json of user "U1" under get response



@TC-16 @user_api
Scenario:When user tries to create user by using POST (/v2/user) with wrong payload or any/all field missing in payload the he should get 422

When user tries to create a user "U1" with all the fields but with field "all_the_fields" "missing" by using API endpoint as "standalone_user_endpoint"
Then user gets "422" and can verify user details in response json of user "U1"

When user tries to create a user "U1" with all the fields but with field "as" "wrong_parameters" by using API endpoint as "standalone_user_endpoint"
Then user gets "422" and can verify user details in response json of user "U1"

When user tries to create a user "U1" with all the fields but with field "username" "missing" by using API endpoint as "standalone_user_endpoint"
Then user gets "422" and can verify user details in response json of user "U1"

When user tries to create a user "U1" with all the fields but with field "firstName" "missing" by using API endpoint as "standalone_user_endpoint"
Then user gets "422" and can verify user details in response json of user "U1"

When user tries to create a user "U1" with all the fields but with field "lastName" "missing" by using API endpoint as "standalone_user_endpoint"
Then user gets "422" and can verify user details in response json of user "U1"

When user tries to create a user "U1" with all the fields but with field "email" "missing" by using API endpoint as "standalone_user_endpoint"
Then user gets "422" and can verify user details in response json of user "U1"

When user tries to create a user "U1" with all the fields but with field "password" "missing" by using API endpoint as "standalone_user_endpoint"
Then user gets "422" and can verify user details in response json of user "U1"

When user tries to create a user "U1" with all the fields but with field "phone" "missing" by using API endpoint as "standalone_user_endpoint"
Then user gets "422" and can verify user details in response json of user "U1"


@TC-17 @user_api
Scenario:When user tries to create user by using POST (/v2/user) with parametric value as "empty string"



When user tries to create a user "U1" with all the fields but with field "username" as "empty string" by using API endpoint as "standalone_user_endpoint"
Then user gets "422" and can verify user details in response json of user "U1"

When user tries to create a user "U1" with all the fields but with field "username" with "trailing spaces" by using API endpoint as "standalone_user_endpoint"
Then user gets "422" and can verify user details in response json of user "U1"

When user tries to create a user "U1" with all the fields but with field "firstName" as "leading spaces" by using API endpoint as "standalone_user_endpoint"
Then user gets "422" and can verify user details in response json of user "U1"

When user tries to create a user "U1" with all the fields but with field "lastName" as "empty string" by using API endpoint as "standalone_user_endpoint"
Then user gets "422" and can verify user details in response json of user "U1"

When user tries to create a user "U1" with all the fields but with field "email" as "empty string" by using API endpoint as "standalone_user_endpoint"
Then user gets "422" and can verify user details in response json of user "U1"

When user tries to create a user "U1" with all the fields but with field "password" as "empty string" by using API endpoint as "standalone_user_endpoint"
Then user gets "422" and can verify user details in response json of user "U1"

When user tries to create a user "U1" with all the fields but with field "phone" as "empty string" by using API endpoint as "standalone_user_endpoint"
Then user gets "422" and can verify user details in response json of user "U1"




###########################Other test which can be verified are below #####################
#Below 3 point also we can validate but due to time constraint I am not adding

#We can also validate the length of the accepted characters in each parameter
#We can also validate whether the parameter value can accept value with some special characters or not.
#We can also validate that the POST/PUT request shoudl not accept payload containing non-string data.
  #GET call with filter query,pagination,sorting

