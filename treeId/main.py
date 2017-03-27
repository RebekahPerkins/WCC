import random
import kivy
kivy.require('1.8.0')

from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
#from kivy.properties import ObjectProperty

class ScreenOne(Screen):

    def __init__ (self,**kwargs):
        super (ScreenOne, self).__init__(**kwargs)

        my_box1 = BoxLayout(orientation='vertical')
        my_label1 = Label(text="The Pacific Northwest has many beautiful conifers. Identify the one you found!", font_size='16dp')
        my_button1 = Button(text="I'll answer questions",size_hint_y=None, size_y=100)
        my_button1.bind(on_press=self.start_answering)
        my_box1.add_widget(my_label1)
        my_box1.add_widget(my_button1)
        self.add_widget(my_box1)

    def start_answering(self,*args):
        remove_screens = []
        for each in self.manager.screens:
            if each.name != 'success' and each.name != 'screen1':
                remove_screens.append(each)
        for each_remove in remove_screens:
            self.manager.remove_widget(each_remove)
            
        answers = Answers(name='answers1')
        self.manager.add_widget(answers)
        self.manager.current = 'answers1'

class Success(Screen):

    def __init__ (self, tree, **kwargs):
        super (Success, self).__init__(**kwargs)
        
        my_box1 = BoxLayout(orientation='vertical')
        my_label1 = Label(text=("You identified a %s!" % tree.name), font_size='16dp')
        my_button1 = Button(text="Start over",size_hint_y=None, size_y=100)
        my_button1.bind(on_press=self.start_over)
        my_box1.add_widget(my_label1)
        my_box1.add_widget(my_button1)
        self.add_widget(my_box1)

    def start_over(self, *args):
        self.manager.current = 'screen1'

class Answers(Screen):
    '''
    attributes:
    answers_order int, known_data dict, remaining_q list, remaining_trees list, curr_q Question
    '''

    def __init__(self, answers_order=1, known_data=None, remaining_trees=None, remaining_q=None, **kwargs):
        super (Answers,self).__init__(**kwargs)
        
        self.answers_order = answers_order
        self.known_data = {} if known_data is None else known_data
        self.remaining_trees = self.generate_all_trees() if remaining_trees is None else remaining_trees
        self.remaining_q = self.generate_all_questions() if remaining_q is None else remaining_q
        self.curr_q = self.calculate_curr_q_alg1(self.remaining_q)

        self.init_widgets()

    def init_widgets(self):
        my_box1 = BoxLayout(orientation='vertical')
        my_label1 = Label(text=self.curr_q.label,font_size='24dp')
        
        answer_button_a = Button(text="True",size_hint_y=None, size_y=100)
        answer_button_b = Button(text="False",size_hint_y=None, size_y=100)
        answer_button_a.bind(on_press=self.answer_true)
        answer_button_b.bind(on_press=self.answer_false)
        
        my_box1.add_widget(my_label1)
        my_box1.add_widget(answer_button_a)
        my_box1.add_widget(answer_button_b)
        self.add_widget(my_box1)

    def success(self,tree):
        for each in self.manager.screens:
            if each.name == 'success':
                self.manager.remove_widget(each)
        success = Success(tree, name='success')
        self.manager.add_widget(success)
        self.manager.current = 'success'

    def answer_false(self, *args):
        self.next_question(self.curr_q.data_key, False)

    def answer_true(self, *args):
        self.next_question(self.curr_q.data_key, True)

    def next_question(self, data_key, users_bool):
        self.known_data[data_key] = users_bool
        'TODO encapsulate bc remaining_q is more complicated, depends on remaining_trees. Like if I already said is_maple I dont want to be asked is_true_fir'
        self.remaining_q.remove(self.curr_q)
        
        self.calculate_remaining_trees()
        
        if len(self.remaining_trees) == 1:
            self.success(self.remaining_trees[0])
        else:            
            next_name = "answers" + str(self.answers_order + 1)
            next_screen = Answers(self.answers_order + 1, self.known_data, self.remaining_trees, self.remaining_q, name=next_name)
            self.manager.add_widget(next_screen)
            self.manager.current = next_name 
        
    def calculate_remaining_trees(self):
        '''calculate remaining trees based on known_data'''
        remaining_trees = self.remaining_trees[:]
        for tree in remaining_trees:
            for k, v in self.known_data.items():
                if tree.data[k] != v:
                    self.remaining_trees.remove(tree)
        print 'Remaining trees are %s' % ', '.join(str(t) for t in self.remaining_trees)
        
    def calculate_curr_q_alg1(self, remaining_q):
        '''a stateless, fruitful, pure function'''
        curr_q = random.choice(remaining_q) 
        print 'Calculating curr_q ... %s' % str(curr_q) 
        return curr_q
    
    def generate_all_trees(self):
        '''a stateless, fruitful, pure function'''
        'TODO: hit the database to populate some objects'
        bigleaf_tree = Tree('Bigleaf Maple', {'is_maple':True, 'has_big_leaves':True, 'is_true_fir':False})
        vine_tree = Tree('Vine Maple', {'is_maple':True, 'has_big_leaves':False, 'is_true_fir':False})
        doug_tree = Tree('Douglas Fir', {'is_true_fir':False, 'is_maple':False, 'has_big_leaves':False})
        silver_tree = Tree('Silver Fir', {'is_true_fir':True, 'is_maple':False, 'has_big_leaves':False})
        return [bigleaf_tree, vine_tree, doug_tree, silver_tree]
        
    def generate_all_questions(self):
        '''a stateless, fruitful, pure function'''
        q1 = Question('is_maple', 'Is it a maple?')
        q2 = Question('has_big_leaves', 'Does it have big leaves?')
        q3 = Question('is_true_fir', 'Is it a true fir?')
        return [q1, q2, q3]
        
            
class Tree():
    '''
    attributes: name str, data dict
    '''
    def __init__(self, name, data):
        self.name = name
        self.data = data        
    
    def __str__(self):
        return self.name
                    
class Question():
    '''
    attributes: data_key str corresponding to a trees' data key, label str
    '''
    def __init__(self, data_key, label):
        self.data_key = data_key
        self.label = label
        
    def __str__(self):
        return self.data_key
        


class TestApp(App):

    def build(self):
        my_screenmanager = ScreenManager()
        screen1 = ScreenOne(name='screen1')
        my_screenmanager.add_widget(screen1)
        return my_screenmanager
            
if __name__ == '__main__':
    TestApp().run()