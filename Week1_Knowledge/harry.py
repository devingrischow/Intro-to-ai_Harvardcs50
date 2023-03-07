# from logic import *

# rain = Symbol("rain")
# hagrid = Symbol("hagrid")
# dumbledore = Symbol("dumbledore")

# knowledge = And(
#     Implication(Not(rain), hagrid),
#     Or(hagrid, dumbledore),
#     Not(And(hagrid, dumbledore)),
#     dumbledore
# )

# print(model_check(knowledge, rain))
from logic import *
rain = Symbol("rain") # It is Raining
hagrid = Symbol("hagrid") #harry visited hagrid
dumbledore = Symbol("dumbledore") #Harry Visited Dumbledore


sentance = And(rain, hagrid)
print(sentance.formula()) #takes a sentance and returns the logical sentance equivolent of it

#create a way to store telling the computer that if it is not raining, harry will visit hagrid
knowledge = Implication(Not(rain), hagrid)
print(knowledge.formula()) 

deeperKnowledge = And(
    Implication(Not(rain), hagrid),
    Or(hagrid, dumbledore),
    Not(And(hagrid, dumbledore)),
    dumbledore

)
print(deeperKnowledge.formula())
print(model_check(deeperKnowledge, rain))