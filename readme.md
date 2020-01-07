# project setup
1. `git clone https://github.com/xuefeng-huang/polling.git`
2. `cd polling/ && python3 -m venv ./venv`
3. `source venv/bin/activate && pip install -r requirement.txt`
4. start db container `docker-compose up db`
5. start server `python main.py`

# use curl to test it
1. to add question `curl -X POST -H "content-type: application/json" -d '{"question":"first question"}' http://localhost:5000/questions`
2. to add choices for each question `curl -X POST -H "content-type: application/json" -d '{"question_id":1, "text":"good"}' http://localhost:5000/choice`
3. to add answer to each question `curl -X POST -H "content-type: application/json" -d '{"question_id":1, "user_id":1, "answer_id":1}' http://localhost:5000/answer`
4. to add user `curl -X POST -H "content-type: application/json" -d '{"user_name":"tim"}' http://localhost:5000/user`

