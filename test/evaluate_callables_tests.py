from build import evaluate_callables


class WhenEvaluatingADictWithNoCallables:
    def when_i_evaluate_the_dict(self):
        self.result = evaluate_callables({"abc": 123, "def": 456, "xyz": 789})

    def it_should_return_the_same_dict(self):
        assert self.result == {"abc": 123, "def": 456, "xyz": 789}


class WhenEvaluatingADictWithCallables:
    def given_input_containing_lambdas(self):
        self.input = {"abc": lambda: 123, "def": lambda: 456, "xyz": 789}
        self.input_copy = self.input.copy()

    def when_i_evaluate_the_dict(self):
        self.result = evaluate_callables(self.input)

    def it_should_return_the_dict_having_called_the_functions(self):
        assert self.result == {"abc": 123, "def": 456, "xyz": 789}

    def it_should_not_change_the_original_dict(self):
        assert self.input == self.input_copy


class MyDict(dict):
    def __eq__(self, other):
        if not isinstance(other, MyDict):
            return False
        return super().__eq__(other)

    def copy(self):
        return MyDict({k: v for k, v in self.items()})


class WhenEvaluatingACustomDictWithNoCallables:
    def when_i_evaluate_the_dict(self):
        self.result = evaluate_callables(MyDict({"abc": 123, "def": 456, "xyz": 789}))

    def it_should_return_an_instance_of_the_same_class(self):
        assert self.result == MyDict({"abc": 123, "def": 456, "xyz": 789})


class WhenEvaluatingACustomDictWithCallables:
    def given_input_containing_lambdas(self):
        self.input = MyDict({"abc": lambda: 123, "def": lambda: 456, "xyz": 789})
        self.input_copy = self.input.copy()

    def when_i_evaluate_the_dict(self):
        self.result = evaluate_callables(self.input)

    def it_should_return_an_instance_of_the_same_class_having_called_the_functions(self):
        assert self.result == MyDict({"abc": 123, "def": 456, "xyz": 789})

    def it_should_not_change_the_original_dict(self):
        assert self.input == self.input_copy


# todo: make it work for other sequences
