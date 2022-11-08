import sys
from PIL import Image,ImageOps

def main():
    if len(sys.argv) == 3:
        conversion(sys.argv[1],sys.argv[2])
    else:
        sys.exit()

def conversion(image_1,image_2):
    var_1 = Image.open(image_1)
    var_2 = Image.open(image_2)
    var_2 = ImageOps.fit(var_2,(500,500))
    w,h = var_1.size
    new = Image.new('RGBA',(w,h),(0,0,0,0))
    new.paste(var_2,(40,120))
    new.paste(var_1,(0,0),mask=var_1)
    new.save('new.png',format='png')
 

if __name__ == '__main__':
    main()