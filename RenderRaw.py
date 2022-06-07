# Render RAW
# Add this script to your scene on a python tag
# this will switch the RS View to RAW when doing non-interactive  renders.

import c4d
import redshift

def main():
    pass

def message(msgType, data):
    # Check for final renders
    if msgType==c4d.MSG_MULTI_RENDERNOTIFICATION:
        redshiftRenderEngineId = 1036219
        my_render_data = data['doc'].GetActiveRenderData()
        videoPost = my_render_data.GetFirstVideoPost()

        while (videoPost):
            print (videoPost)
            if videoPost.CheckType(redshiftRenderEngineId):
                break
            videoPost = videoPost.GetNext()

        videoPost[c4d.REDSHIFT_RENDERER_COLOR_MANAGEMENT_OCIO_VIEW] =  r"Raw"
        videoPost[c4d.REDSHIFT_RENDERER_COLOR_MANAGEMENT_COMPENSATE_VIEW_TRANSFORM] = False
