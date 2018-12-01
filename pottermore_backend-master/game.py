
from flask import Flask, jsonify
import random

app = Flask(__name__)

gameSteps = [
    #{ "id": 1,"question":"Welcome to your house, little one! You’re going to live here in Hogwarts for the next 7 years and for that.. you need to get access to the common room. In order to gain the access, you’re going to have to go on a small quest yourself to attain the Password. " ,"commands":"NULL"},
    #{ "id": 2,"question":"Are you ready to do it?","commands":"Yes" },
    { "id": 1,"question":"Start?", "commands1":"Yes" ,"commands2":"NULL"},
    { "id": 2,"question":"There’s no light here. Do you want to light it up?", "commands1":"Yes","commands2":"NULL" },
    { "id": 3,"question":"The light has uncovered a room full of objects. There’s a Box you see.. What do you do with that?","commands1":"Open","commands2":"Ignore"},
    { "id": 4,"question":"Oh, good stuff, rookie! You found a letter!","commands1":"Keep","commands2":"Ignore"},
    { "id": 5,"question":"Let’s continue, Where do you want to go next?","commands1":"Go Left","commands2":"NULL"},
    { "id": 6,"question":"There’s a painting here. Inspect or ignore?","commands1":"Inspect","commands2":"NULL"},
    { "id": 7,"question":"The painting is a horse running away in the field. Nothing unusual. Just Hogwarts stuff. Go somewhere else maybe?","commands1":"Go Right","commands2":"NULL"},
    { "id": 8,"question":".Hmmm.. I see something shining. Inspect or ignore?", "commands1":"Inspect" ,"commands2":"NULL"},
    { "id": 9,"question":"That’s a shiney bowl with transparent liquid. Looks very pretty. I suggest let it be. What do you think? Inspect or ignore?", "commands1":"Inspect" ,"commands2":"NULL"},
    { "id": 10,"question":"You are smart, arent you? We see that the liquid is transparent and at the bottom of the bowl there’s a letter. Keep or ignore?", "commands1":"Keep(E)" ,"commands2":"NULL"},
    { "id": 11,"question":"Well Well, halfway through. Soon you’ll be able to get to the common room. What to do next? ", "commands1":"Inventory" ,"commands2":"Go back/left/right"},
    { "id": 12,"question":"Continue or ignore?", "commands1":"Continue" ,"commands2":"NULL"},
    { "id": 13,"question":"Wait a second. You kicked something by mistake. Did that sound like metal? You want to look for it?", "commands1":"Yes" ,"commands2":"NULL"},
    { "id": 14,"question":"Oh, that’s a key. Wonder what it opens. Keep or ignore?", "commands1":"Keep" ,"commands2":"Ignore"},
    { "id": 15,"question":"Ooh, you see a scroll. Wonder what’s in it. Inspect or ignore?", "commands1":"Inspect" ,"commands2":"Ignore"},
    #{ "id": 15,"question":"Hoorah! One more letter. Keep or ignore?", "commands1":"Keep(A)" ,"commands2":"Ignore"},

]

@app.route('/gamesteps', methods=['GET'])
def get_gamesteps():
    return jsonify({'gameSteps': gameSteps})

# @app.route('/gamesteps/<int:id>', methods=['GET'])
# def get_gamesteps(id):
# #check the elements in the questions
#     gamstep = list(filter(lambda gs: gs['id'] == id, gameSteps))
#  #if true, return this element , if not return 404
#     if len(gameSteps) == 0:
#         abort(404)
#     return jsonify({'gameStep': gameSteps[0]})





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
