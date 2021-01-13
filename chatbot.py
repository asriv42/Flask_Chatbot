from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import os

# Creating ChatBot Instance
# chatbot = ChatBot('CAT')
chatbot = ChatBot(
    'CoronaBot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.BestMatch',
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand. I am still learning.',
            'maximum_similarity_threshold': 0.90
        }
    ],
    database_uri='sqlite:///database.sqlite3'
)

 # Training with Personal Ques & Ans
# conversation = [
#     "Hello",
#     "Hi there!",
#     "How are you doing?",
#     "I'm doing great.",
#     "That is good to hear",
#     "Thank you.",
#     "You're welcome.",
#     "Bye Bye.",
#     "Thanks for Using CAT. Have a nice Day!"
# ]
#
# trainer = ListTrainer(chatbot)
# trainer.train(conversation)

# training_data_quesans = open('training_data\ques_ans.txt').read().splitlines()
# training_data_personal = open('training_data\personal_ques.txt').read().splitlines()
training_data_quesans = open('C:/Users/asriv42/Desktop/ChatterBot/venv/training_data/ques_ans.txt').read().splitlines()
training_data_personal = open('C:/Users/asriv42/Desktop/ChatterBot/venv/training_data/personal_ques.txt').read().splitlines()

training_data = training_data_quesans + training_data_personal

trainer = ListTrainer(chatbot)
trainer.train(training_data)
# Training with English Corpus Data
trainer_corpus = ChatterBotCorpusTrainer(chatbot)
trainer_corpus.train('chatterbot.corpus.english')

