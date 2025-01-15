import spacy
from typing import Dict, List, Tuple

class ChatbotTALN:
    def __init__(self):
        # Chargement du modèle français de spaCy
        self.nlp = spacy.load('fr_core_news_md')
        
        # Dictionnaire des réponses prédéfinies
        self.reponses = {
            'salutation': ['Bonjour!', 'Salut!', 'Bienvenue!'],
            'au_revoir': ['Au revoir!', 'À bientôt!', 'Bonne journée!'],
            'default': ['Je ne comprends pas.', 'Pourriez-vous reformuler?']
        }
        
    def analyser_message(self, message: str) -> Tuple[str, float]:
        """
        Analyse le message de l'utilisateur et détermine l'intention
        """
        doc = self.nlp(message.lower())
        
        # Analyse des mots-clés pour déterminer l'intention
        if any(token.text in ['bonjour', 'salut', 'hey'] for token in doc):
            return 'salutation', 0.9
        elif any(token.text in ['aurevoir', 'revoir', 'bye'] for token in doc):
            return 'au_revoir', 0.9
            
        return 'default', 0.5
        
    def generer_reponse(self, intention: str) -> str:
        """
        Génère une réponse en fonction de l'intention détectée
        """
        import random
        return random.choice(self.reponses[intention])
        
    def discuter(self):
        """
        Démarre une conversation avec l'utilisateur
        """
        print("Chatbot: Bonjour! Comment puis-je vous aider?")
        
        while True:
            message = input("Vous: ")
            if message.lower() in ['quit', 'exit', 'bye']:
                print("Chatbot: Au revoir!")
                break
                
            intention, confiance = self.analyser_message(message)
            reponse = self.generer_reponse(intention)
            print(f"Chatbot: {reponse}")

if __name__ == "__main__":
    chatbot = ChatbotTALN()
    chatbot.discuter()