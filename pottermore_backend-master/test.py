
from flask import Flask, jsonify
import random

app = Flask(__name__)


houses = [
    { "id": 1,"Name":"Gryffindor" },
    { "id": 2,"Name":"Hufflepuff" },
    { "id": 3,"Name":"Ravenclaw" },
    { "id": 4,"Name":"Slytherin" }
]

questions =[
    { "Id": 1,"question":"Dawn or dusk?" , 
        "choice1":"Dawn",
        "choice2":"Dusk" 
    },

    { "Id": 2,
        "question":"Which road tempts you most?" ,
         "choice1":"The wide,sunny,grassy lane",
         "choice2":"The narrow,dark,latern-lit alley" 
    },

    { "Id": 3,
        "question":"What are you most looking forward to learning at Hogwarts" ,
         "choice1":"Apparition and Disapparition",
         "choice2":"All about magical creatures and how to befriend/care of them" 
    },

    { "Id": 4,
        "question":"Which of the following do you find most difficult to deal with" ,
         "choice1":"Hunger",
         "choice2":"Loniess" 
    },
    { "Id": 5,
        "question":"Given the choice,would you rather invent a potion that would gurantee you" ,
         "choice1":"Love?",
         "choice2":"Glory?"
     },

    { "Id": 6,
        "question":"Four goblets are placed before you.Which would you choose to drink?" ,
         "choice1":"The foaming, frothing, silver liquid",
         "choice2":"The goldenliquid that is so bright that it hurts the eye" 
    },
    { "Id": 7,
        "question":"If you were attending Hogwarts, which pet would you choose to take with you?" ,
         "choice1":"Black cat",
         "choice2":"Tawny owl" 
    },
    { "Id": 8,"question":"Heads or tails" , 
        "choice1":"Heads",
        "choice2":"Tails" 
    }
    ]

@app.route('/')
def hello():
    return 'Hello World'


@app.route('/houses', methods=['GET'])
def get_houses():
    return jsonify({'houses': houses})

@app.route('/randompick',methods=['GET'])
def get_randomhouse():
#check the elements in the questions
    house = list(filter(lambda h: h['id'] == random.randint(1,4), houses))
 #if true, return this element , if not return 404
    if len(houses) == 0:
        abort(404)
    return jsonify({'house': house[0]})


@app.route('/houses/<int:house_id>', methods=['GET'])
def get_house(house_id):
#check the elements in the questions
    house = list(filter(lambda h: h['id'] == house_id, houses))
 #if true, return this element , if not return 404
    if len(houses) == 0:
        abort(404)
    return jsonify({'house': house[0]})


#get all the questions 
@app.route('/questions', methods=['GET'])
def get_questions():
    return jsonify({'questions': questions})

from flask import abort

@app.route('/questions/<int:question_Id>', methods=['GET'])
def get_question(question_Id):
#check the elements in the questions
    question = list(filter(lambda q: q['Id'] == question_Id, questions))
 #if true, return this element , if not return 404
    if len(question) == 0:
        abort(404)
    return jsonify({'question': question[0]})



if __name__ == '__main__':
    app.run(debug=True)
