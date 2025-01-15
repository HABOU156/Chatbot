import unittest
from chatbot import ChatbotTALN

class TestChatbot(unittest.TestCase):
    def setUp(self):
        self.chatbot = ChatbotTALN()
    
    def test_analyse_salutation(self):
        """Test de la détection des salutations"""
        intention, confiance = self.chatbot.analyser_message("Bonjour")
        self.assertEqual(intention, "salutation")
        self.assertEqual(confiance, 0.9)
    
    def test_analyse_au_revoir(self):
        """Test de la détection des au revoir"""
        intention, confiance = self.chatbot.analyser_message("au revoir")
        self.assertEqual(intention, "au_revoir")
        self.assertEqual(confiance, 0.9)
    
    def test_reponse_coherente(self):
        """Test de la cohérence des réponses"""
        reponse = self.chatbot.generer_reponse("salutation")
        self.assertIn(reponse, self.chatbot.reponses["salutation"])

if __name__ == '__main__':
    unittest.main()