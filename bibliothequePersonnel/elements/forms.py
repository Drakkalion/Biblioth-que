from django.forms import ModelForm
from .models import Element

class ElementForm(ModelForm):
    class Meta:
        model = Element
        # champs qu'on veut afficher
        fields = ['titre','remarque','note','type_element','image','url','favori','decouvrir','revoir','acheter']
