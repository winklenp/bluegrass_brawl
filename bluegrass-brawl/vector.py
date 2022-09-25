import math

class Vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def magSquared(self):
        return self.x*self.x+self.y*self.y

    def mag(self):
        return math.sqrt(self.magSquared())

    def dot(self, other):
        return self.x*other.x+self.y*other.y

    def cross(self,other):
        return self.x*other.y-self.y*other.x

    def add(self, other):
        return Vector(self.x+other.x,self.y+other.y)

    def addIp(self, other):
        self.x+=other.x
        self.y+=other.y

    def add(self, x,y):
        return Vector(self.x+x,self.y+y)

    def addIp(self,x,y):
        self.x+=x
        self.y+=y

    def sub(self, other):
        return Vector(self.x-other.x,self.y-other.y)

    def subIp(self, other):
        self.x-=other.x
        self.y-=other.y

    def mult(self, factor):
        return Vector(self.x*factor,self.y*factor)

    def multIp(self, factor):
        self.x*=factor
        self.y*=factor

    def unit(self):
        if self.magSquared()==0:
            return Vector(1,0)
        return self.mult(1/self.mag())

    def flipX(self):
        return Vector(-self.x,self.y)

    def flipXIp(self):
        self.x*=-1

    def flipY(self):
        return Vector(self.x,-self.y)

    def flipYIp(self):
        self.y*=-1

    def limitXIp(self,limit):
        if self.x<-limit:
            self.x=-limit
        if self.x>limit:
            self.x=limit
    def limitYIp(self,limit):
        if self.y<-limit:
            self.y=-limit
        if self.y>limit:
            self.y=limit


    def frictionIp(self, xLim, yLim):
        if self.x<0:
            self.x+=xLim
            if self.x>0:
                self.x=0
        elif self.x>0:
            self.x-=xLim
            if self.x<0:
                self.x=0
        if self.y<0:
            self.y+=yLim
            if self.y>0:
                self.y=0
        elif self.y>0:
            self.y-=yLim
            if self.y<0:
                self.y=0

    def set(self, other):
        self.x=other.x
        self.y=other.y