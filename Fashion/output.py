import model
#path='/content/gdrive/My Drive/00a77f3d-a574-4013-a918-209e2b77f9851564426188252-1.jpg'
bot_pattern={0: 'Design Print', 1: 'Faded', 2: 'Geometric', 3: 'Solid'}
bot_item={0: 'Jeans', 1: 'Shorts', 2: 'TrackPants', 3: 'Trousers'}
bot_s_length={0: 'Above Knee', 1: 'Below Knee', 2: 'Cropped', 3: 'Knee Length', 4: 'Regular', 5: 'Three-Fourth Length'}
#up_pattern={0: 'Biker', 1: 'Checks Stripes', 2: 'Colourblocked', 3: 'Design Print', 4: 'Faded', 5: 'Geometric', 6: 'Polka Dots', 7: 'Sports', 8: 'Textured', 9: 'Woven'}
up_pattern={0: 'Design Print', 1: 'Faded', 2: 'Geometric', 3: 'Solid'}
up_item={0: 'Jackets', 1: 'Kurtas', 2: 'Sweatshirts'}
up_multicolor={0: 'N', 1: 'Y'}
up_s_length={0: 'Long Sleeves', 1: 'Short Sleeves', 2: 'Sleeveless', 3: 'Three-Quarter Sleeves'}
bot_multicolor={0: 'N', 1: 'Y'}
wear_type={0: 'Bottomwear', 1: 'Topwear'}
import pandas as pd
def up_Attributes(path):

    item= pattern = multicolor = sleeve=None
    df=pd.DataFrame(columns=['wear','item','pattern','multicolor', 'sleeve'])
    wear="Topwear"
   #if wear =='Topwear':

    item=model.get_up_item_type(path,up_item)
    pattern=model.get_up_pattern_type(path,up_pattern)
    multicolor= model.get_up_multicolor_type(path,up_multicolor)
    sleeve=model.get_up_sleeve_length(path,up_s_length)
    df=df.append(pd.Series([wear,item,pattern,multicolor,sleeve], index=['wear','item','pattern','multicolor', 'sleeve']), ignore_index=True)
    return df
def bot_Attributes(path):
    item= pattern = multicolor = sleeve=None
    df=pd.DataFrame(columns=['wear','item','pattern','multicolor', 'sleeve'])

    wear="Bottomwear"
    item=model.get_bot_item_type(path,bot_item)
    pattern=model.get_bot_pattern_type(path,bot_pattern)
    multicolor= model.get_bot_multicolor_type(path,bot_multicolor)
    sleeve=model.get_bot_sleeve_length(path,bot_s_length)
    df=df.append(pd.Series([wear,item,pattern,multicolor,sleeve], index=['wear','item','pattern','multicolor', 'sleeve']), ignore_index=True)
    return df
#print(attributes(path))
