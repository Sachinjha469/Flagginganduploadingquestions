import csv
import psycopg2

conn = psycopg2.connect(#appdbcred)
cursor = conn.cursor()

def upload_useraskedquestions():
  user_id=str(3460)
  # id=976+1
  approve_status=1
  with open('Question_asked - Sheet8.csv', encoding ='latin1') as csv_file:
      csv_reader = csv.reader(csv_file, delimiter=',')
      count=0
      for row in csv_reader:
          count=count+1
          if(count>1):
                  question_id=str(row[3])
                  answer=str(row[5])
                  date='2021-07-06'
                  sql=("INSERT INTO public.reading_useransweronquestion( answer, question_id, user_id, date, time, approve_status, mode_status) VALUES ( %s, %s, %s, %s, %s, %s, %s)")
                  tuple=(answer, question_id, user_id, date, "", approve_status,0 )
                  cursor.execute(sql,tuple)
                  conn.commit()
