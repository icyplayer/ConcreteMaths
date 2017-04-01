"""
Created on 2017年3月31日

@author: ipr
"""
import numpy as np

class Form(object):
    """
    X| x1 x2 x3 ... 
    ======================
    Y| y1 y2 y3 ...
    ======================
    Z| z1 z2 z3 ...
    ======================
    ...
    ======================
    """
    def __init__(self, vecLst, dim=2, needTranspose=True):
        """
        vecLst: list of list
        Example: dim = 3s
        vecLst = [
                    [x0,y0,z0],
                    [x1,y1,z1],
                    [x2,y2,z2],
                ]
        """
        self.vecLst = np.array(vecLst)
        self.dim = dim
        self.needTranspose = needTranspose
        if len(self.vecLst.shape) == 1:
            self.vecLst.shape = (len(vecLst), 1,)
    
    def setDim(self, newDim):
        if newDim > self.vecLst.shape[-1] or newDim < 0:
            raise ValueError("Invalid dim value: Out of range")
        self.dim = newDim
    
    def getDim(self):
        return self.dim
        
    def genForm(self, formHeaders=None, selfFormated=False):
        try:
            if self.needTranspose:
                vecNum, vecDim = self.vecLst.shape[0], self.vecLst.shape[-1]            
                if self.dim == vecDim:  # dim to be display equal to count of vars
                    trans = np.transpose(self.vecLst)
                elif self.dim < vecDim:  # truncated: self.dim < self.vecLst.shape[-1],  
                    trans = np.transpose(self.vecLst)[:self.dim]
                else:  # dim overrange: self.dim > vecDim
                    raise ValueError("dim out of range!")   
            else:  # self.needTranspose == False
                vecNum, vecDim = self.vecLst.shape[-1], self.vecLst.shape[0]  
                if self.dim == vecDim:
                    trans = self.vecLst
                elif self.dim < vecDim:
                    trans = self.vecLst[:self.dim]
                else:  # dim overrange: self.dim > vecDim
                    raise ValueError("dim out of range!") 
                                
        except ValueError as ie:
            print(str(ie))
            print("Truncate dim %d => %d..." % (self.dim, vecDim))
            self.dim = vecDim
            print("Truncated! Re-generate form")
            self.genFrom()
        finally:
            
            formLineLst = []
            if selfFormated and formHeaders:
                maxLen = max([len(s) for s in formHeaders])
                headSpan = max([maxLen, 3, 1]) + 3
                lineHeaderLst = formHeaders
            elif not selfFormated and self.dim <= 3:
                headSpan = 4 # self.dim <=3, use X/Y/Z as header
                if self.dim == 1:
                    lineHeaderLst = ["X"]
                elif self.dim == 2:
                    lineHeaderLst = ["X", "Y"]
                elif self.dim == 3:
                    lineHeaderLst = ["X", "Y", "Z"]
            else:
                headSpan = 6

            # Handle line's header
            separatorMid = "-" * (headSpan + vecNum*2)
            separatorHead = "=" * (headSpan + vecNum*2)
            for i in range(self.dim):
                # generate line's header
                if selfFormated:
                    fmt = "{0:{1}}"
                    if i < len(lineHeaderLst):
                        lineHeader = fmt.format(lineHeaderLst[i], headSpan-3) + " | "
                    else:
                        lineHeader = fmt.format("X%02d"%i, headSpan-3) + " | "
                elif self.dim <= 3:
                    lineHeader = lineHeaderLst[i] + " | "
                else:
                    lineHeader = "X%02d"%i + " | "
                # generate line string
                lineStr = lineHeader + str(trans[i])[1:-1]
                formLineLst.append(lineStr)
                if i == 0:
                    formLineLst.append(separatorHead)
                else:
                    formLineLst.append(separatorMid)
            return "\n".join(formLineLst)
            
    def __repr__(self):
        return self.genForm()
    
    def genFromWithHeader(self, formHeaders=["X", "Y", "Z"]):
        return self.genForm(formHeaders, True)
        
        
    