
from elearnerapp.models import Questionnaire,Question,UserAnswer
import csv
t1=Questionnaire(topic="BM1")
t1.save()
# q=Questionnaire.objects.get(topic="BM")
# q.id
# with open('/home/lenovo/Dev/venv/src/elearnerapp/Diagnostic Questions/BM_diagnostic.csv',encoding='utf-8') as csvfile:
#          reader = csv.DictReader(csvfile)
#          for row in reader:
#             p=Question(questionnaire=q,q_text=row['Question'],option_a=row['Option1'],option_b=row['Option2'],option_c=row['Option3'],option_d=row['Option4'],correct=row['Answer'])
#             p.save()
# Question.objects.filter(questionnaire=q)

# qset=Question.objects.filter(questionnaire=q)
# qset.filter(correct="Answer A").update(correct="A")
# qset.filter(correct="Answer B").update(correct="B")
# qset.filter(correct="Answer C").update(correct="C")
# qset.filter(correct="Answer D").update(correct="D")
# print([p.correct for p in qset])
