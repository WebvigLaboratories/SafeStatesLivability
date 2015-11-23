from django.test import TestCase

from models import *

# Create your tests here.
class ModelTest(TestCase):
    def get_tool(self, name="Active Community Schools Workbook"):
        return Tools.objects.get(name=name)

    def test_tool_get(self):
        tool = self.get_tool()
        self.assertTrue(isinstance(tool, Tools))
        self.asserEqual(tool.__unicode__(), tool.name)