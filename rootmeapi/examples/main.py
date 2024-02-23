import rootmeapi
api_object=rootmeapi.RootMeAPI()
api_object.login('your_login')
result=api_object.search_author_by_name('name_to_search')
json_response=api_object.get_author_by_id(result[0].id)
number_challs=len(json_response.validations)
print(number_challs)
print('Titre,Score,Date')
# Get list of challenges validated, points and date
for id_chall in range(number_challs):
    chall_info=api_object.get_challenge_by_id(int(json_response.validations[id_chall]['id_challenge']))
    print(chall_info['titre'] + ',' + chall_info['score'] + ',' + json_response.validations[id_chall]['date'])