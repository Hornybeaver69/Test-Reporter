from ._anvil_designer import Form1Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import json

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.repeating_panel_1.items = app_tables.tabela1.search()
    # Set up event handler for file upload
    self.file_loader_1.set_event_handler('change', self.file_loaded)
    # Update the Data Grid to show the new data
    self.repeating_panel_1.items = app_tables.tabela1.search()

  def file_loaded(self, file, **event_args):
    # Read the uploaded JSON file
    json_content = file.get_bytes().decode('utf-8')

    # Clear the existing data in 'Tabela1'
    app_tables.tabela1.delete_all_rows()

    data = []
    #file_path = file.
    lines = json_content.split('\n')
    for json_object_line in lines:
      try:
        json_object = json.loads(json_object_line)
      except:
        print("Json parsing error")
        return
      else:
         data.append(json_object)

    # # Parse the JSON content
    # try:
    #   data = json.loads(json_content)
    #   print(data)
    # except ValueError as e:
    #   # Handle JSON parsing error if necessary
    #   #self.label_error.text = f"Error parsing JSON: {str(e)}"
    #   print("Json parsing error")
    #   return
      
    # Insert new data from the JSON into 'Tabela1'
    for item in data:
      print(item.get("test-case"))
      app_tables.tabela1.add_row(
        test_case=item.get("test-case"),
        status=item.get("status"),
        error_type=item.get("error-type")
        )
