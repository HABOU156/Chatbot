import unittest
from chatbot import ChatbotTALN
from test_scenarios import SCENARIOS_TEST

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
    
    def test_scenarios_salutations(self):
        """Test tous les scénarios de salutation"""
        for phrase in SCENARIOS_TEST["salutations"]:
            intention, _ = self.chatbot.analyser_message(phrase)
            self.assertEqual(intention, "salutation")


if __name__ == '__main__':
    unittest.main()