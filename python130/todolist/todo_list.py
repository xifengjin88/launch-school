from python130.todolist import todo
from todo import Todo


def select(fn, items):
    return [c for c in items if fn(c)]

def foreach(fn, items):
    for item in items:
        fn(item)

class TodoList:
    def __init__(self, title):
        self._title = title
        self._todos = []

    @property
    def title(self):
        return self._title

    def add(self, todo):
        if not isinstance(todo, Todo):
            raise TypeError("Not a todo")
        self._todos.append(todo)

    def __str__(self):
        heading = f"---- {self.title} -----"
        return "\n".join([heading] + [str(todo) for todo in self._todos])

    def __len__(self):
        return len(self._todos)

    def is_empty(self):
        return len(self._todos) == 0

    def last(self):
        if self.is_empty():
            raise IndexError("Todo list is empty")
        return self._todos[-1]

    def __str__(self):
        output_lines = [f'----- {self.title} -----']
        output_lines += [str(todo) for todo in self._todos]
        return '\n'.join(output_lines)

    def first(self):
        if self.is_empty():
            raise IndexError("Todo list is empty")
        return self._todos[0]

    def to_list(self):
        return self._todos.copy()

    def todo_at(self, index):
        if index < 0 or index >= len(self._todos):
            raise IndexError("Index out of range")
        return self._todos[index]

    def mark_done_at(self, index):
        todo = self.todo_at(index)
        todo.done = True

    def mark_undone_at(self, index):
        todo = self.todo_at(index)
        todo.done = False

    def mark_all_done(self):
        def mark_done(todo):
            todo.done = True
        self.undone_todos().each(mark_done)

    def mark_all_undone(self):
        def mark_undone(todo):
            todo.done = False

        self.done_todos().each(mark_undone)

    def all_done(self):
        return all([todo.done for todo in self._todos])

    def remove_at(self, index):
        if index < 0 or index >= len(self._todos):
            raise IndexError("Index out of range")
        del self._todos[index]

    def each(self, fn):
        for todo in self._todos:
            fn(todo)

    def select(self, fn):
        new_todo_list = TodoList(self._title)
        for todo in self._todos:
            if fn(todo):
                new_todo_list.add(todo)
        return new_todo_list

    def done_todos(self):
        return self.select(lambda todo: todo.done)

    def undone_todos(self):
        return self.select(lambda todo: not todo.done)

    def find_by_title(self, title):
        selected_todos = select(lambda todo: todo.title == title, self._todos)
        if selected_todos:
            return selected_todos[0]
        raise IndexError("can't find what you are looking for")

    def mark_done(self, title):
        todo = self.find_by_title(title)
        todo.done = True


if __name__ == "__main__":
    empty_todo_list = TodoList('Nothing Doing')


    def setup():
        todo1 = Todo('Buy milk')
        todo2 = Todo('Clean room')
        todo3 = Todo('Go to gym')

        todo2.done = True

        todo_list = TodoList("Today's Todos")
        todo_list.add(todo1)
        todo_list.add(todo2)
        todo_list.add(todo3)

        return todo_list


    def step_1():
        print('--------------------------------- Step 1')
        todo_list = setup()

        # setup() uses `todo_list.add` to add 3 todos

        try:
            todo_list.add(1)
        except TypeError:
            print('TypeError detected')  # TypeError detected

        for todo in todo_list._todos:
            print(todo)


    def step_2():
        print('--------------------------------- Step 2')
        todo_list = setup()

        print(todo_list)
        # ---- Today's Todos -----
        # [ ] Buy milk
        # [X] Clean room
        # [ ] Go to gym


    def step_3():
        print('--------------------------------- Step 3')
        todo_list = setup()

        print(len(todo_list))  # 3
        print(len(empty_todo_list))  # 0


    def step_4():
        print('--------------------------------- Step 4')
        todo_list = setup()

        print(todo_list.first())  # [ ] Buy milk
        print(todo_list.last())  # [ ] Go to gym

        try:
            empty_todo_list.first()
        except IndexError:
            print('Expected IndexError: Got it!')

        try:
            empty_todo_list.last()
        except IndexError:
            print('Expected IndexError: Got it!')


    def step_5():
        print('--------------------------------- Step 5')
        todo_list = setup()

        print(empty_todo_list.to_list())  # []

        todos = todo_list.to_list()
        print(type(todos).__name__)  # list

        for todo in todos:
            print(todo)  # [ ] Buy milk
            # [X] Clean room
            # [ ] Go to gym


    def step_6():
        print('--------------------------------- Step 6')
        todo_list = setup()

        print(todo_list.todo_at(0))  # [ ] Buy milk
        print(todo_list.todo_at(1))  # [X] Clean room
        print(todo_list.todo_at(2))  # [ ] Go to gym

        try:
            todo_list.todo_at(3)
        except IndexError:
            print('Expected IndexError: Got it!')

        # Ensure we have a reference
        print(todo_list.todo_at(1) is todo_list.todo_at(1))  # True


    def step_7():
        print('--------------------------------- Step 7')
        todo_list = setup()

        todo_list.mark_done_at(0)
        print(todo_list)
        # ---- Today's Todos -----
        # [X] Buy milk
        # [X] Clean room
        # [ ] Go to gym

        todo_list.mark_done_at(1)
        print(todo_list)
        # ---- Today's Todos -----
        # [X] Buy milk
        # [X] Clean room
        # [ ] Go to gym

        todo_list.mark_done_at(2)
        print(todo_list)
        # ---- Today's Todos -----
        # [X] Buy milk
        # [X] Clean room
        # [X] Go to gym

        try:
            todo_list.mark_done_at(3)
        except IndexError:
            print('Expected IndexError: Got it!')

        todo_list.mark_undone_at(0)
        print(todo_list)
        # ---- Today's Todos -----
        # [ ] Buy milk
        # [X] Clean room
        # [X] Go to gym

        todo_list.mark_undone_at(1)
        print(todo_list)
        # ---- Today's Todos -----
        # [ ] Buy milk
        # [ ] Clean room
        # [X] Go to gym

        todo_list.mark_undone_at(2)
        print(todo_list)
        # ---- Today's Todos -----
        # [ ] Buy milk
        # [ ] Clean room
        # [ ] Go to gym

        try:
            todo_list.mark_undone_at(3)
        except IndexError:
            print('Expected IndexError: Got it!')


    def step_8():
        print('--------------------------------- Step 8')
        todo_list = setup()

        print(todo_list)
        # ---- Today's Todos -----
        # [ ] Buy milk
        # [X] Clean room
        # [ ] Go to gym

        todo_list.mark_all_done()
        print(todo_list)
        # ---- Today's Todos -----
        # [X] Buy milk
        # [X] Clean room
        # [X] Go to gym

        todo_list.mark_all_undone()
        print(todo_list)
        # ---- Today's Todos -----
        # [ ] Buy milk
        # [ ] Clean room
        # [ ] Go to gym


    def step_9():
        print('--------------------------------- Step 9')
        todo_list = setup()

        print(todo_list.all_done())  # False

        todo_list.mark_all_done()
        print(todo_list.all_done())  # True

        todo_list.mark_undone_at(1)
        print(todo_list.all_done())  # False

        print(empty_todo_list.all_done())  # True


    def step_10():
        print('--------------------------------- Step 10')
        todo_list = setup()

        print(todo_list)
        # ---- Today's Todos -----
        # [ ] Buy milk
        # [X] Clean room
        # [ ] Go to gym

        todo_list.remove_at(1)
        print(todo_list)
        # ---- Today's Todos -----
        # [ ] Buy milk
        # [ ] Go to gym

        todo_list.remove_at(1)
        print(todo_list)
        # ---- Today's Todos -----
        # [ ] Buy milk

        try:
            todo_list.remove_at(1)
        except IndexError:
            print('Expected IndexError: Got it!')

        todo_list.remove_at(0)
        print(todo_list)
        # ---- Today's Todos -----


    def step_11():
        print('--------------------------------- Step 11')
        todo_list = setup()

        todo_list.mark_all_undone()
        print(todo_list)

        # ---- Today's Todos -----
        # [ ] Buy milk
        # [ ] Clean room
        # [ ] Go to gym

        def done_if_y_in_title(todo):
            if 'y' in todo.title:
                todo.done = True

        todo_list.each(done_if_y_in_title)
        print(todo_list)
        # ---- Today's Todos -----
        # [X] Buy milk
        # [ ] Clean room
        # [X] Go to gym

        todo_list.each(lambda todo: print('>>>', todo))
        # >>> [X] Buy milk
        # >>> [ ] Clean room
        # >>> [X] Go to gym


    def step_12():
        print('--------------------------------- Step 12')
        todo_list = setup()

        def y_in_title(todo):
            return 'y' in todo.title

        print(todo_list.select(lambda todo: y_in_title))
        # ---- Today's Todos -----
        # [ ] Buy milk
        # [ ] Go to gym

        print(todo_list.select(lambda todo: todo.done))
        # ---- Today's Todos -----
        # [X] Clean room


    def step_13():
        print('--------------------------------- Step 13')
        todo_list = setup()

        todo_list.add(Todo('Clean room'))
        print(todo_list)
        # ---- Today's Todos -----
        # [ ] Buy milk
        # [X] Clean room
        # [ ] Go to gym
        # [ ] Clean room

        found = todo_list.find_by_title('Go to gym')
        print(found)
        # [ ] Go to gym

        found = todo_list.find_by_title('Clean room')
        print(found)
        # [X] Clean room

        try:
            todo_list.find_by_title('Feed cat')
        except IndexError:
            print('Expected IndexError: Got it!')


    def step_14():
        print('--------------------------------- Step 14')
        todo_list = setup()

        done = todo_list.done_todos()
        print(done)
        # ----- Today's Todos -----
        # [X] Clean room

        undone = todo_list.undone_todos()
        print(undone)
        # ----- Today's Todos -----
        # [ ] Buy milk
        # [ ] Go to gym

        done = empty_todo_list.done_todos()
        print(done)
        # ----- Nothing Doing -----

        undone = empty_todo_list.undone_todos()
        print(undone)
        # ----- Nothing Doing -----


    def step_15():
        print('--------------------------------- Step 15')
        todo_list = setup()

        todo_list.mark_done('Go to gym')
        print(todo_list)
        # ----- Today's Todos -----
        # [ ] Buy milk
        # [X] Clean room
        # [X] Go to gym

        try:
            todo_list.mark_done('Feed cat')
        except IndexError:
            print('Expected IndexError: Got it!')



    step_1()
    step_2()
    step_3()
    step_4()
    step_5()
    step_6()
    step_7()
    step_8()
    step_9()
    step_10()
    step_11()
    step_12()
    step_13()
    step_14()
    step_15()
