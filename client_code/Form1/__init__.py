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

    # Clear the existing data in 'Tabela1'
    app_tables.tabela1.delete_all_rows()
    # Any code you write here will run before the form opens.
    self.repeating_panel_1.items = app_tables.tabela1.search()
    # Set up event handler for file upload
    self.file_loader_1.set_event_handler('change', self.file_loaded)


  def file_loaded(self, file, **event_args):
    # Read the uploaded JSON file
    json_content = file.get_bytes().decode('utf-8')

    # Clear the existing data in 'Tabela1'
    app_tables.tabela1.delete_all_rows()

    # JSON object example
    # {"test-case":"glupi test 6", "status":true, "error-type":null}
    # In JSON report file, each line is a new JSON object.
    data = []
    lines = json_content.split('\n')
    for json_object_line in lines:
      try:
        json_object = json.loads(json_object_line)
      except:
        print("Json parsing error")
        return
      else:
         data.append(json_object)
      
    # Insert new data from the JSON into 'Tabela1'
    for item in data:
      app_tables.tabela1.add_row(
        test_case=item.get("test-case"),
        status=item.get("status"),
        error_type=item.get("error-type")
        )

    # Update the Data Grid to show the new data
    self.repeating_panel_1.items = app_tables.tabela1.search()
    self.repeating_panel_1.items = app_tables.tabela1.search()
    self.file_loader_1.clear()

