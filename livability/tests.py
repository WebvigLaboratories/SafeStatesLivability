from django.test import TestCase

from models import *

# Create your tests here.
class ModelTest(TestCase):

    def create_tool(self, name="Test tool", url="http://test.com"):
        return Tools.objects.create(name=name, url=url)

    def test_tool_get(self):
        tool = self.create_tool()
        self.assertTrue(isinstance(tool, "test"))
        self.assertEqual(tool.__unicode__(), tool.name)