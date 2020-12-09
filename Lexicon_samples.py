import checklist
from checklist.editor import Editor
from checklist.perturb import Perturb

editor = Editor()

print(list(editor.lexicons['male_from']['United_States']))
print(list(editor.lexicons['religion']))
print(list(editor.lexicons['sexual_adj']))
print(list(editor.lexicons['first_pronoun']))

