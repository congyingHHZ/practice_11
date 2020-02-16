class A:
    def __int__(self):
        print('A.init')
        self.driver = 'aaa'
        print('@driver  Test_A: ',self.driver)
    def a_fun(self):
        print('@A_FUN')


class TestB(A):
    # def __int__(self):
    #     print('@B_init')

    def test_b_fun(self):
        self.driver = 'bbbb'
        print('@driver  Test_B: ', self.driver)
