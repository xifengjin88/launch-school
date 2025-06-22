import unittest
from todo import Todo
from todo_list import TodoList


class TestTodoList(unittest.TestCase):
    def setUp(self):
        self.todo1 = Todo("Buy milk")
        self.todo2 = Todo("Clean room")
        self.todo3 = Todo("Go to the gym")

        self.todos = TodoList("Today's Todos")
        self.todos.add(self.todo1)
        self.todos.add(self.todo2)
        self.todos.add(self.todo3)

    # your tests go here

    def test_length(self):
        self.assertEqual(len(self.todos), 3)

    def test_to_list(self):
        self.assertEqual([self.todo1, self.todo2, self.todo3], self.todos.to_list())

    def test_first(self):
        self.assertEqual(self.todos.to_list()[0], self.todo1)

    def test_last(self):
        self.assertEqual(self.todos.last(), self.todo3)


    def test_all_done(self):
        self.todo1.done = True
        self.todo2.done = True
        self.todo3.done = True
        self.assertEqual(self.todos.all_done(), True)

    def test_add_invalid(self):
        with self.assertRaises(TypeError):
            self.todos.add("")
            
    def test_todo_at(self):
        with self.assertRaises(IndexError):
            self.todos.todo_at(10)
            
    def test_mark_done_at(self):
        with self.assertRaises(IndexError):
            self.todos.mark_done_at(10)
            
        self.todos.mark_done_at(0)
        self.assertEqual(self.todo1.done, True)
        
    def test_mark_undone(self):
        self.assertFalse(self.todo1.done)
        
    def test_remove_at(self):
        with self.assertRaises(IndexError):
            self.todos.remove_at(10)
        
        self.todos.remove_at(0)
        self.assertEqual([self.todo2, self.todo3], self.todos.to_list())

    def test_str(self):
        string = (
            "----- Today's Todos -----\n"
            "[ ] Buy milk\n"
            "[ ] Clean room\n"
            "[ ] Go to the gym"
        )
        self.assertEqual(string, str(self.todos))
        
    def test_str_done_todo(self):
        string = (
            "----- Today's Todos -----\n"
            "[X] Buy milk\n"
            "[X] Clean room\n"
            "[ ] Go to the gym"
        )
        
        self.todo1.done = True
        self.todo2.done = True

        self.assertEqual(string, str(self.todos))
        
    def test_str_all_done_todos(self):
        string = (
            "----- Today's Todos -----\n"
            "[X] Buy milk\n"
            "[X] Clean room\n"
            "[X] Go to the gym"
        )
        
        self.todos.mark_all_done()
        self.assertEqual(string, str(self.todos))
        
    def test_each(self):
        self.todos.each(lambda todo: self.assertIsInstance(todo, Todo))
            
    def test_select(self):
        todos = []
        todos = self.todos.select(lambda todo: todo.title == "Go to the gym")
        self.assertEqual([self.todo3], todos.to_list())

if __name__ == "__main__":
    unittest.main()