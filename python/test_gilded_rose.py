# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]#Name,sell_in,quality
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("fixme", items[0].name)
    def test_equal_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("foo", items[0].name)
    def test_equal_quality(self):
        items = [Item("No Aged Brie", -1, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        #print(items[0].quality)
        self.assertEquals(8, items[0].quality)

        
if __name__ == '__main__':
    unittest.main()
