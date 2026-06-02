import os
import json
import session
from todo import config as todo_config
import config as root_config
from util import util_time 





class TodoService:
    def __init__(self):
        self.todos = {}
        self.init_database()

    def init_database(self):
        # 현재 파일 위치 # abspath : 절대값
        BASE_PATH = os.path.dirname(os.path.abspath(__file__))
        print(f'BASE_PATH: {BASE_PATH}')       

        # 프로젝트 루트 경로
        ROOT_DIR = os.path.dirname(BASE_PATH)
        print(f'ROOT_DIR: {ROOT_DIR}')

        # db/todos.json
        self.dbFile = os.path.join(ROOT_DIR, 'db', 'todos.json')
        print(f'self.dbFile: {self.dbFile}')

        # 파일 존재 여부 확인
        if not os.path.exists(self.dbFile):
            self.save_todos(self.todos)

        else:
            self.todos = self.load_todos()

    # json 파일 저장
    def save_todos(self, todos): # {}
        with open(self.dbFile, 'w', encoding = 'utf-8') as f:
            json.dump(todos, f, ensure_ascii=False, indent = 4)

    def load_todos(self):
        with open(self.dbFile, 'r', encoding='utf-8') as f:
            return json.load(f)
        
    def isMyTodos(self):
        allTodos = self.load_todos()
        if session.getSignInedMemberId() in allTodos:
            return True
        
        return False

    def run(self):
        # 로그인 되지 않았을경우
        if session.getSignInedMemberId() == '':
            print('Please SIGN-IN!!')
            return
        

        flag = True
        while flag:
            if not self.isMyTodos():
                self.todos[session.getSignInedMemberId()] = []
                self.save_todos(self.todos)

            menuNum = int(input('1.WRITE   2.READ   3.UPDATE    4.DELETE    5.COMPLETE-CHANGE   99.SERVICE-OUT '))
            if menuNum == todo_config.WRITE:
                self.todos = self.load_todos()
                myTodos = self.todos[session.getSignInedMemberId()]

                tText = input('Input new todo text: ')
                tExpDate = input('Input todo experation date(2026-08-05 06:09:09)')

                todo = {
                    'tTxt': tText,
                    'tExpDate': tExpDate,
                    'tRegDate': util_time.getCurrentDateTime(),
                    'tModDate': util_time.getCurrentDateTime(),
                    'tComplete': False
                }
                
                myTodos.insert(0, todo)
                self.save_todos(self.todos)
                print('WRITE SUCCESS!!')

                if root_config.DEV_MOD:
                    print(f'self.load_todos(): {self.load_todos()}')


            elif menuNum == todo_config.READ:
                self.todos = self.load_todos()
                myTodos = self.todos[session.getSignInedMemberId()]
                for idx, myTodos in enumerate(myTodos):
                    print('-' * 50)
                    print(f'[{idx + 1}]')
                    print(f'TEXT: {myTodos["tTxt"]}')
                    print(f'EXPIRATIONDATE: {myTodos["tExpDate"]}')
                    print(f'REGISTE DATE: {myTodos["tRegDate"]}')
                    print(f'MODIFY DATE: {myTodos["tModDate"]}')
                    print(f'COMPLETE: {myTodos["tComplete"]}')
                    print('-' * 50)
                    print(f'[{idx + 1}]')

            elif menuNum == todo_config.UPDATE:
                self.tods = self.load_todos()
                myTodos = self.todos[session.getSignInedMemberId()]
                for idx, myTodo in enumerate(myTodos):
                    print('-' *100)
                    print(f"[{idx + 1}] {myTodo['tTxt']} [{myTodo['tExpDate']}] [{myTodo['tComplete']}]")
                    print('-' *100)

                todoNumber = int(input('Enter the todo number: '))

                tText = input('Input todo text: ')
                tExpDate = input('Input todo experation date(2026-08-05 06:09:09)')

                todo = {
                    'tTxt': tText,
                    'tExpDate': tExpDate,
                    'tRegDate': myTodos[todoNumber-1]['tRegDate'],
                    # 원본이 가지고 있는 작성시간
                    'tModDate': util_time.getCurrentDateTime(),
                    'tComplete': myTodos[todoNumber-1]['tComplete']
                }

                myTodos[todoNumber-1] = todo
                self.save_todos(self.todos)
                print('UPDATE SUCCESS!!')

                if root_config.DEV_MOD:
                    print(f'self.load_todos(): {self.load_todos()}')

            elif menuNum == todo_config.DELETE:
                self.tods = self.load_todos()
                myTodos = self.todos[session.getSignInedMemberId()]
                for idx, myTodo in enumerate(myTodos):
                    print('-' *100)
                    print(f"[{idx + 1}] {myTodo['tTxt']} [{myTodo['tExpDate']}] [{myTodo['tComplete']}]")
                    print('-' *100)

                todoNumber = int(input('Enter the todo number: '))
                del myTodos[todoNumber-1]
                self.save_todos(self.todos)
                print('DELETE SUCCESS!!')

                if root_config.DEV_MOD:
                    print(f'self.load_todos(): {self.load_todos()}')

            elif menuNum == todo_config.COMPLETE_CHANGE:
                self.todos = self.load_todos()
                myTodos = self.todos[session.getSignInedMemberId()]
                for idx, myTodo in enumerate(myTodos):
                    print('-' *100)
                    print(f"[{idx + 1}] {myTodo['tTxt']} [{myTodo['tExpDate']}] [{myTodo['tComplete']}]")
                    print('-' *100)

                todoNumber = int(input('Enter the todo number: '))
                # if myTodos[todoNumber-1]['tComplete'] == True:
                #     myTodos[todoNumber-1]['tComplete'] == False

                # else:
                #     myTodos[todoNumber-1]['tComplete'] == True
                myTodos[todoNumber-1]['tComplete'] = not myTodos[todoNumber-1]['tComplete']
                self.save_todos(self.todos)
                print('COMPLETE CHANGE SUCCESS!!')

                if root_config.DEV_MOD:
                    print(f'self.load_todos(): {self.load_todos()}')
                    


            elif menuNum == todo_config.SERVICE_OUT:
                flag = False




if __name__ == '__main__':
    todoService = TodoService()
    todoService.run()