from django.forms.widgets import ClearableFileInput

# taken from django and modified 
class CustomClearableFileInput(ClearableFileInput):
    clear_checkbox_label = ('Remove')
    initial_text = ('Current Image')
    input_text = ('')
    template_name = 'shop/custom_widgets/custom_clearable_file_input.html'