import csv
import psycopg2

conn = psycopg2.connect(#appdbCredentials)
cursor = conn.cursor()

#This function flags all the arguments who length is below 7
def flagargument():
  cursor.execute("SELECT id, argument,content_flagged FROM public.quiz_q_user_argument_debate_topic")
  result=cursor.fetchall()
  for r in result:
      print(r[0])
      print(r[1])
      print(len(r[1]))
      print(r[2])
      if(len(r[1])<8):
          cursor.execute("UPDATE public.quiz_q_user_argument_debate_topic SET content_flagged=1 WHERE id='"+str(r[0])+"'")
          conn.commit()
  
 flagargument()

