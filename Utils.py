import re
import json

# Subclase personalizada de JSONEncoder
class CustomFloatEncoder(json.JSONEncoder):
    def encode(self, obj):
        # Serializa el JSON y luego ajusta los números flotantes con dos decimales
        json_string = super().encode(obj)
        return self._format_floats(json_string)

    def _format_floats(self, json_string):
        # Expresión regular para identificar números flotantes
        import re
        pattern = r'(?<!["\'])\b\d+\.\d+\b(?!["\'])'
        # Reemplaza los números flotantes con formato de dos decimales
        return re.sub(pattern, lambda x: f"{float(x.group()):.2f}", json_string)
