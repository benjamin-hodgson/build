from build import Builder
from contexts import catch


class MyBuilder(Builder):
    defaults = [
        ('abc', 123),
        ('def', 456),
        ('xyz', 789)
    ]

    def build(self):
        return self.data


class WhenNotOverridingDefaults:
    def given_a_builder(self):
        self.builder = MyBuilder()

    def when_i_call_build(self):
        self.result = self.builder.build()

    def it_should_have_all_the_defaults(self):
        assert self.result == {
            'abc': 123,
            'def': 456,
            'xyz': 789
        }


class WhenOverridingADefault:
    def given_a_builder_with_overridden_defaults(self):
        self.builder = MyBuilder().with_abc(-1).with_def(-2)

    def when_i_call_build(self):
        self.result = self.builder.build()

    def the_defaults_should_have_been_overridden(self):
        assert self.result == {
            'abc': -1,
            'def': -2,
            'xyz': 789
        }


class MyDict(dict):
    def __eq__(self, other):
        if not isinstance(other, MyDict):
            return False
        return super().__eq__(other)


class MyBuilderWithCustomDict(Builder):
    dict = MyDict

    defaults = [
        ('abc', 123),
        ('def', 456),
        ('xyz', 789)
    ]

    def build(self):
        return self.data


class WhenUsingACustomDict:
    def given_a_builder_which_overrides_dict(self):
        self.builder = MyBuilderWithCustomDict()

    def when_i_call_build(self):
        self.result = self.builder.build()

    def it_should_have_used_my_custom_dict_subclass(self):
        assert self.result == MyDict({
            'abc': 123,
            'def': 456,
            'xyz': 789
        })


class WhenOverridingAPropertyWhichDoesNotExist:
    def given_a_builder(self):
        self.builder = MyBuilder()

    def when_i_override_a_nonexistent_property(self):
        self.exception = catch(lambda name: getattr(self.builder, name), 'with_nonexistent')

    def it_should_throw(self):
        assert isinstance(self.exception, AttributeError)
