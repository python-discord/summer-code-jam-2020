#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import nltk
import gpt_2_simple as gpt2

os.environ['NLTK_DATA'] = os.path.join(os.getcwd())
nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')

model_name = "124M"
if not os.path.isdir(os.path.join("models", model_name)):
    print("Model not found... Downloading new")
    print(f"Downloading {model_name} model...")
    gpt2.download_gpt2(model_name=model_name)


def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "spydirweb.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
