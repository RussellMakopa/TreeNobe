class TreeNode:
    def __init__(self, question, choices=None, answer=None):
        self.question = question
        self.choices = choices if choices else []
        self.answer = answer

    def add_choice(self, choice, node):
        self.choices.append((choice, node))

    def is_leaf(self):
        return not self.choices

    def display_question(self):
        print(self.question)

        if self.choices:
            for i, (choice, _) in enumerate(self.choices):
                print(f"{i+1}. {choice}")

    def get_answer(self, choice_index):
        if self.choices:
            if 0 <= choice_index < len(self.choices):
                _, node = self.choices[choice_index]
                return node
            else:
                return None
        else:
            return self.answer


# Example usage
# Create the tree structure
question1 = TreeNode("What is the capital of France?")
question1.add_choice("Paris", TreeNode("Correct answer!"))
question1.add_choice("London", TreeNode("Incorrect answer."))
question1.add_choice("Berlin", TreeNode("Incorrect answer."))

question2 = TreeNode("What is the largest planet in our solar system?")
question2.add_choice("Mars", TreeNode("Incorrect answer."))
question2.add_choice("Jupiter", TreeNode("Correct answer!"))
question2.add_choice("Earth", TreeNode("Incorrect answer."))

# Interact with the user
current_node = question1  # Start with the first question

while not current_node.is_leaf():
    current_node.display_question()
    choice = int(input("Enter your choice (number): ")) - 1
    current_node = current_node.get_answer(choice)

print(current_node.question)
