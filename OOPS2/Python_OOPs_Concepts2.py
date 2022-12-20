from OOPS2.Python_OOPs_Concepts import A

#obj = A()
#print(obj.__module__)

class ABC:
    p = 60
    _q = 50
    __r = 100

    def show_p_value(self):
        print("P Value :", ABC.p)

    def _show_q_Value(self):
        print("Q Value :", ABC._q)

    def __show_r_value(self):
        print("P Value :", ABC.__r)

if __name__ == '__main__':
    obj = ABC()
    print(obj.p)
    obj.show_p_value()
    print(obj._q)
    obj._show_q_Value()
    print(obj._ABC__r)



