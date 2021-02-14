from flask import Flask, request, jsonify

app = Flask(__name__)

pet_list = [{
		"id": 0,
		"name": "Macy",
		"animal": "dog",
		"gender": "female",
		"age": 2
	},
	{
		"id": 1,
		"name": "Henry",
		"animal": "dog",
		"gender": "male",
		"age": 8
	},
	{
		"id": 2,
		"name": "Reedus",
		"animal": "dog",
		"gender": "male",
		"age": 4
	},
	{
		"id": 3,
		"name": "Mocca",
		"animal": "cat",
		"gender": "female",
		"age": 3
	},
	{
		"id": 4,
		"name": "Lorna",
		"animal": "gold fish",
		"gender": "female",
		"age": 1
	},
	{
		"id": 5,
		"name": "Peter",
		"animal": "hamster",
		"gender": "male",
		"age": 3
	},
	{
		"id": 6,
		"name": "Coal",
		"animal": "dog",
		"gender": "male",
		"age": 1
	},
	{
		"id": 7,
		"name": "Johnson",
		"animal": "cat",
		"gender": "male",
		"age": 4
	},
	{
		"id": 8,
		"name": "Betty",
		"animal": "iguana",
		"gender": "female",
		"age": 4
	}
]

@app.route('/pets', methods=['GET', 'POST'])
def pets():
    if request.method == 'GET':
        if len(pet_list) > 0 :
            return jsonify(pet_list)
        else :
            'Success', 200
    
    if request.method == 'POST':
        new_name = request.form['name']
        new_animal = request.form['animal']
        new_gender = request.form['gender']
        new_age = request.form['age']
        new_id = pet_list[-1]['id']+1

        new_pet_obj = {
            'id': new_id,
            'name': new_name,
            'animal': new_animal,
            'gender': new_gender ,
            'age': new_age 
        }

        pet_list.append(new_pet_obj)
        return jsonify(pet_list), 201



if __name__ == '__main__':
     app.run()

