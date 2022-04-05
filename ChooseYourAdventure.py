class TreeNode:
    def __init__(self, story_piece):
        self.story_piece = story_piece
        self.choices = []

    def add_child(self, node):
        self.choices.append(node)

    def traverse(self):
        # Sets the beginning story argument and the choice limits
        story_node = self
        print(story_node.story_piece)
        choice_options = [1, 2]

        # Handling end of story exception, still needs work
        try:
            # As long as there is a story argument the show goes on
            while len(story_node.story_piece) > 0:
                choice = input("Enter 1 or 2 to continue: ")
                if int(choice) in choice_options:
                    # Adjusts user input to list index, 0 or 1
                    chosen_index = int(choice) - 1
                    # Selects choice from list
                    chosen_child = story_node.choices[chosen_index]
                    # Prints next chapter
                    print(chosen_child.story_piece)
                    # replace the main story argument and its related choices
                    story_node = chosen_child
                else:
                    print("Not a valid option")
        except:
            print("End of the story. Thanks for playing! ^-^")
            return


######
# VARIABLES FOR TREE
######
####User name prompt
user_name = input("What is your name?: ")

####Still need to move these branches to another file, too much clutter
story_root = TreeNode("""
You are in a forest clearing. There is a path to the left.
A bear emerges from the trees and roars!
Do you: 
1 ) Roar back!
2 ) Run to the left...
""")

choice_a = TreeNode("""
The bear is startled and runs away.
Do you:
1 ) Shout 'Sorry bear!'
2 ) Yell 'Hooray!'
""")

choice_a_1 = TreeNode("""
The bear returns and tells you it's been a rough week. After making peace with
a talking bear, he shows you the way out of the forest.

YOU HAVE ESCAPED THE WILDERNESS.
""")

choice_a_2 = TreeNode("""
The bear returns and tells you that bullying is not okay before leaving you alone
in the wilderness.

YOU REMAIN LOST.
""")

choice_b = TreeNode("""
You come across a clearing full of flowers. 
The bear follows you and asks 'what gives?'
Do you:
1 ) Gasp 'A talking bear!'
2 ) Explain that the bear scared you.
""")

choice_b_1 = TreeNode("""
The bear is unamused. After smelling the flowers, it turns around and leaves you alone.

YOU REMAIN LOST.
""")

choice_b_2 = TreeNode("""
'I understand, I apologize for startling you, {}.' The bear says. Your new friend shows you a 
path leading out of the forest. You still don't know how it knew your name.

YOU HAVE ESCAPED THE WILDERNESS.
""".format(user_name))

####Here story branches are defined

story_root.add_child(choice_a)
story_root.add_child(choice_b)
choice_a.add_child(choice_a_1)
choice_a.add_child(choice_a_2)
choice_b.add_child(choice_b_1)
choice_b.add_child(choice_b_2)

######
# IMPLEMENTATION
######
print("Once upon a time...")
story_root.traverse()
