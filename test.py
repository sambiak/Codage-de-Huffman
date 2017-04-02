import unittest
from v2 import *
import queue as q
import random


class TestHuffman(unittest.TestCase):
    """classe de tests pour verifier les fonctions nécessaires a huffman"""

    def test_paire(self):
        p_plus_grande = Paire("N'importe", 5)
        p_plus_petite = Paire(342, 1)
        p_identique_a_petie = Paire(None, 1)
        self.assertTrue(p_plus_grande >= p_plus_petite)
        self.assertTrue(p_plus_grande > p_plus_petite)
        self.assertTrue(p_plus_petite >= p_identique_a_petie)
        self.assertFalse(p_plus_petite > p_identique_a_petie)
        self.assertEqual(p_plus_grande.element, "N'importe")

    def test_fileprio(self):
        """La file de priorité doit avoir le même comportemment que Priority queue de python"""
        queue_c = File_de_prio()
        queue_p = q.PriorityQueue()
        nombres_ale = [random.randrange(3000) for _ in range(1000)]
        nombres = [4, 3, 7, 8, 1, 2]
        for n in nombres:
            p = Paire(None, n)
            queue_c.put(p)
            queue_p.put(p)
        for i in range(6):
            self.assertEqual(queue_c.get(), queue_p.get())
            self.assertEqual(queue_c.qsize(), queue_p.qsize())
        for n in nombres_ale:
            p = Paire(None, n)
            queue_c.put(p)
            queue_p.put(p)
        for i in range(1000):
            self.assertEqual(queue_c.get(), queue_p.get())
            self.assertEqual(queue_c.qsize(), queue_p.qsize())

    def test_frequence_lettre(self):
        """test pour uen fréquence sous la forme de dictionaire"""
        freq = creer_densite("")
        self.assertEqual(freq, {})
        texte = "j'aime bien les patates et les carottes"
        freq = creer_densite(texte)
        self.assertEqual(1, freq["'"])
        self.assertEqual(2, freq["i"])

        with self.assertRaises(KeyError):
            freq["w"]





if __name__ == '__main__':
    unittest.main()