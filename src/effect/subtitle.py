from .effect import Effect
from ..video import Video
from ..operation import put_text

class Subtitle(Effect):
    def __init__(self,text, start_frame:int=0, end_frame:int=None, fontsize:int=None, color=(0,0,0), h_ratio:float =0.7, bg_color=(255,255,255)):
        super(Subtitle,self).__init__(start_frame=start_frame,end_frame=end_frame)
        self.text = text
        self.h_ratio = h_ratio
        self.color = color
        self.bg_color = bg_color
        self.fontsize = fontsize
        
    def effect(self,video:Video):

        h, w = video.shape

        if self.fontsize is None:
            fontsize = w//22
        else :
            fontsize = self.fontsize
        
        return put_text(video,self.text,self.start_frame,self.end_frame,fontsize=fontsize,color=self.color,center_xy=(w/2,h*self.h_ratio),bg_color=self.bg_color)

    