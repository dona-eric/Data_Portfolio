from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

question_base = {
    "Bonjour": "Bonjour! Comment puis-je vous aider?",
    "Qui suis-je ?": "Je suis Eric KOULODJI, Physicien Théoricien et Data Scientist",
    "Quelles sont vos compétences ?": "Mes compétences sont bien au-dela de ce que vous pensées: J'ai acquis des compétences en Programmation (Python, HTML/CSS, et les frameworks comme Django, Numpy, scipy), en machine learning(Modelisation mathématiques et statistiques), en Deep Learning(Tensorflow/Keras), Pytorch, Git/Github",
    "Quels sont vos projets?": "J'ai travaillé sur des projets de détection de fraude et de prévision des inondations.",
    "Merci": "De rien! À bientôt."
}

def get_response(user_message):
    vectorizer = TfidfVectorizer()
    questions = list(question_base.keys())
    tfidf_matrix = vectorizer.fit_transform(questions)
    user_tfidf = vectorizer.transform([user_message])
    similarities = cosine_similarity(user_tfidf, tfidf_matrix)
    best_match = similarities.argmax()
    if questions:
        return question_base[questions[best_match]]
    else:
        return f'Désolé, Je ne comprends pas votre question'

