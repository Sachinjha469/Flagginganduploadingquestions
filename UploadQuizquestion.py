import csv
import psycopg2

conn = psycopg2.connect(#appdbcred)
cursor = conn.cursor()
count=0

def upload_quizquestions():
  with open('Untitled spreadsheet - Sheet1.csv', encoding ='latin1') as csv_file:
      csv_reader = csv.reader(csv_file, delimiter=',')
      # print(csv_reader)
      for row in csv_reader:
          count=count+1
          if(count>1):

              category=1
              question_cat=row[6]
              image_url=''
              question_para=''
              quiz_list_id=row[7]
              question_main_text=str(row[0])
              choice1=str(row[1])
              choice2=str(row[2])
              choice3=str(row[3])
              choice4=str(row[4])
              actual_answer=str(row[5])
              sql=("INSERT INTO public.quiz_general_quiz_question(category, question_cat, image_url, question_main_text, question_para, choice1, choice2, choice3, choice4, actual_answer, quiz_list_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
              tuple=(category, question_cat, image_url, question_main_text, question_para, choice1, choice2, choice3, choice4, actual_answer, quiz_list_id )
              cursor.execute(sql,tuple)
              conn.commit()

count=0
def upload_olympiadquizquestion():
  with open('Learning Space report - Sheet9 (7).csv', encoding ='latin1') as csv_file:
      csv_reader = csv.reader(csv_file, delimiter=',')
      # print(csv_reader)
      for row in csv_reader:
          count=count+1
          if(count>1):

              category=row[0]
              section=row[1]
              sub_section=row[2]
              question_cat=row[3]
              exam_mode=row[4]
              image_url=''
              question_main_text=row[5]
              question_para=''
              choice1=row[6]
              choice2=row[7]
              choice3=row[8]
              choice4=row[9]
              actual_answer=row[10]
              sql=("INSERT INTO quiz_olympiad_question(category, section, sub_section, question_cat, exam_mode, image_url, question_main_text, question_para, choice1, choice2, choice3, choice4, actual_answer) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s)")
              tuple=(category, section, sub_section, question_cat, exam_mode, image_url, question_main_text, question_para, choice1, choice2, choice3, choice4, actual_answer)
              cursor.execute(sql,tuple)
              conn.commit()
