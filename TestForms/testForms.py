from forms.forms import Form

vecLst = [[1, 0, 2, 0],  # (x0, y0, z0)
          [0, 1, 2, 0],  # (x1, y1, z1)
          [2, 0, 1, 0],]  # (x2, y2, z2)

# validation test
def test1():
    """ Simple test """
    dim = 2
    form = Form(vecLst, dim)
    print(form)
    
    # X, Y, Z format
    print()
    form.dim = 3
    print(form)
    
    # X%02d format
    print()
    form.dim = 4
    print(form)
    
    # self defined format
    print()
    form.dim = 4
    print(form.genFromWithHeader(["X", "Y", "Z", "W"]))





# print("test 1")
# test1()


print("test 2")

# test non-transpose case
vecLstNonTrans = [[1,2,3],
                  [0,0,1],
                  [0,1,0],]
dim = 2
formNonTrans = Form(vecLstNonTrans, dim, False)
print("form (non-transposed): dim=%d" % formNonTrans.getDim())
print(formNonTrans)
print()
formNonTrans.setDim(3)
print("form (non-transposed): dim=%d" % formNonTrans.getDim())
print(formNonTrans)

