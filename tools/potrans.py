#!/usr/bin/env python3
import polib
from googletrans import Translator

def translate_po_file(po_file_path, target_language, max_retries=5):
    translator = Translator()

    # Load the PO file
    po = polib.pofile(po_file_path)

    # Translate each untranslated entry
    # for entry in po.untranslated_entries():
    entries = po.untranslated_entries()
    for entry in entries:
        for attempt in range(max_retries + 1):
            try:
                original_text = entry.msgid
                translation = translator.translate(original_text, dest=target_language)
                entry.msgstr = translation.text
                print("翻译:[" + entry.msgid + "], 翻译结果:[" + entry.msgstr + "]")
                break
            except Exception as e:
                print("Translation error: "+ e +": " + entry.msgid)
    # Save the translated PO file
    po.save(po_file_path.replace('.po', f'.{target_language}.po'))

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 3:
        print("Usage: translate_po.py <po_file_path> <target_language>")
        sys.exit(1)

    po_file_path = sys.argv[1]
    target_language = sys.argv[2]

    translate_po_file(po_file_path, target_language)

